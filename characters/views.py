import functools
import json
import logging

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import CharacterForm, UserRegisterForm
from .image_utils import compress_character_image
from .models import Character
from .rules_data.builder_beschreibungen import (HINTERGRUND_BESCHREIBUNGEN,
                                                KLASSEN_BESCHREIBUNGEN,
                                                UNTERKLASSEN_BESCHREIBUNGEN)
from .rules_data.hintergruende import HINTERGRUND_DATEN
from .rules_data.klassen import KLASSEN_DATEN
from .rules_data.spezies import SPEZIES_DATEN
from .rules_data.waffen import WAFFEN_DATEN, WAFFEN_MEISTERUNGEN

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Konfigurationstabellen für die Charaktererstellung
# ---------------------------------------------------------------------------

# Stat-Priorität pro Klasse: Reihenfolge der Zuweisung des Standard-Arrays
# Standard-Array: [15, 14, 13, 12, 10, 8]
STANDARD_ARRAY = [15, 14, 13, 12, 10, 8]

ABILITY_NAMES = ('strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma')

CLASS_CONFIGS = {
    ('barbar',):                    (['strength', 'constitution', 'dexterity', 'wisdom', 'charisma', 'intelligence'], 'd12'),
    ('bard',):                      (['charisma', 'dexterity', 'constitution', 'wisdom', 'intelligence', 'strength'], 'd8'),
    ('kleriker', 'cleric'):         (['wisdom', 'constitution', 'strength', 'charisma', 'intelligence', 'dexterity'], 'd8'),
    ('druid',):                     (['wisdom', 'constitution', 'dexterity', 'intelligence', 'charisma', 'strength'], 'd8'),
    ('kämpfer', 'fighter'):         (['strength', 'constitution', 'dexterity', 'wisdom', 'intelligence', 'charisma'], 'd10'),
    ('mönch', 'monk'):              (['dexterity', 'wisdom', 'constitution', 'strength', 'intelligence', 'charisma'], 'd8'),
    ('paladin',):                   (['strength', 'charisma', 'constitution', 'wisdom', 'dexterity', 'intelligence'], 'd10'),
    ('waldläufer', 'ranger'):       (['dexterity', 'wisdom', 'constitution', 'strength', 'intelligence', 'charisma'], 'd10'),
    ('schurke', 'rogue'):           (['dexterity', 'intelligence', 'constitution', 'charisma', 'wisdom', 'strength'], 'd8'),
    ('zauberer', 'sorcerer'):       (['charisma', 'constitution', 'dexterity', 'wisdom', 'intelligence', 'strength'], 'd6'),
    ('hexenmeister', 'warlock'):    (['charisma', 'constitution', 'dexterity', 'wisdom', 'intelligence', 'strength'], 'd8'),
    ('magier', 'wizard'):           (['intelligence', 'constitution', 'dexterity', 'wisdom', 'charisma', 'strength'], 'd6'),
}

BACKGROUND_BONUSES = {
    ('adeliger', 'noble'):              ('strength', 'charisma'),
    ('akolyth', 'acolyte'):             ('wisdom', 'intelligence'),
    ('handwerker', 'artisan'):          ('strength', 'dexterity'),
    ('scharlatan', 'charlatan'):        ('charisma', 'dexterity'),
    ('krimineller', 'criminal'):        ('dexterity', 'intelligence'),
    ('unterhalter', 'entertainer'):     ('charisma', 'dexterity'),
    ('bauer', 'farmer', 'peasant'):     ('constitution', 'wisdom'),
    ('wache', 'guard'):                 ('strength', 'wisdom'),
    ('fremder', 'guide', 'outlander'):  ('wisdom', 'dexterity'),
    ('einsiedler', 'hermit'):           ('wisdom', 'constitution'),
    ('händler', 'merchant'):            ('charisma', 'intelligence'),
    ('weiser', 'sage'):                 ('intelligence', 'wisdom'),
    ('seefahrer', 'sailor'):            ('dexterity', 'wisdom'),
    ('gelehrter', 'scribe'):            ('intelligence', 'wisdom'),
    ('soldat', 'soldier'):              ('strength', 'constitution'),
    ('straßenkind', 'urchin', 'wayfarer'): ('dexterity', 'wisdom'),
}

_MELEE_CLASSES = {'barbar', 'kämpfer', 'paladin', 'fighter'}
_AGILE_CLASSES = {'schurke', 'mönch', 'waldläufer', 'rogue', 'monk', 'ranger'}


def _match_keywords(text, keyword_table):
    """Sucht den ersten Treffer in einer keyword→value Tabelle."""
    text_lower = text.lower()
    for keywords, value in keyword_table.items():
        if any(kw in text_lower for kw in keywords):
            return value
    return None



def _parse_json_request(request):
    """Parst den JSON-Body der Anfrage und gibt (data, error_response) zurück."""
    try:
        data = json.loads(request.body)
        return data, None
    except (json.JSONDecodeError, ValueError):
        return None, JsonResponse(
            {'success': False, 'error': 'Ungültige Anfragedaten.'},
            status=400,
        )

def _apply_background_bonuses(character):
    """Wendet Hintergrund-Boni auf das Charakterobjekt an."""
    bonuses = _match_keywords(character.background, BACKGROUND_BONUSES)

    if bonuses:
        primary, secondary = bonuses
        setattr(character, primary, getattr(character, primary) + 2)
        setattr(character, secondary, getattr(character, secondary) + 1)
        return

    class_lower = character.character_class.lower()
    if class_lower in _MELEE_CLASSES:
        character.strength += 2
        character.constitution += 1
    elif class_lower in _AGILE_CLASSES:
        character.dexterity += 2
        character.wisdom += 1
    else:
        character.charisma += 2
        character.intelligence += 1



def _assign_equipment(character, equipment_preference):
    """Weist Startgold oder Standardausrüstung zu."""
    if equipment_preference == 'gold':
        character.gold = 100
        character.equipment = 'Nichts (Startgold gewählt)'
    else:
        character.gold = 0
        character.equipment = f'Standard-Ausrüstung für {character.character_class}'


def _assign_stats(character):
    """Weist das Standard-Array basierend auf der Klasse zu."""
    class_config = _match_keywords(character.character_class, CLASS_CONFIGS)
    if class_config:
        stat_order, hit_die = class_config
    else:
        stat_order = list(ABILITY_NAMES)
        hit_die = 'd8'

    for attr, value in zip(stat_order, STANDARD_ARRAY):
        setattr(character, attr, value)
    character.hit_dice = f'1{hit_die}'
    return hit_die


def _calculate_hp(character, hit_die, tp_bonus=0):
    """Berechnet die maximalen und aktuellen Trefferpunkte."""
    try:
        hit_die_value = int(hit_die.strip()[1:])
    except (ValueError, IndexError):
        hit_die_value = 8  # Fallback

    con_mod = character._ability_modifier(character.constitution)
    base_hp = hit_die_value + con_mod + tp_bonus
    hp_per_level = (hit_die_value // 2) + 1 + con_mod + tp_bonus

    if character.level > 1:
        character.max_hp = base_hp + (hp_per_level * (character.level - 1))
    else:
        character.max_hp = base_hp
    character.current_hp = character.max_hp

def _apply_class_data(character):
    # --- Klassen-Daten laden ---
    klasse_data = None
    for k, v in KLASSEN_DATEN.items():
        if k.lower() in character.character_class.lower():
            klasse_data = v
            break

    # --- Rettungswurf-Übungen aus Klasse ---
    if klasse_data:
        character.saving_throw_proficiencies = klasse_data.get('rettungswuerfe', [])


def _apply_background_data(character):
    # --- Fertigkeits-Übungen aus Hintergrund ---
    bg_data = HINTERGRUND_DATEN.get(character.background)
    skill_profs = []
    if bg_data:
        skill_profs = list(bg_data.get('fertigkeiten', []))
        # Herkunftstalent (Origin Feat) zuweisen
        talent = bg_data.get('talent', '')
        if talent:
            character.feats = [talent]
        # Werkzeug-Übung zuweisen
        werkzeug = bg_data.get('werkzeug', '')
        if werkzeug:
            character.tool_proficiencies = [werkzeug]
    character.skill_proficiencies = skill_profs


def _apply_species_data(character):
    # --- Spezies-Daten: Geschwindigkeit & TP-Bonus ---
    spezies_data = None
    race_lower = character.race.lower()
    for sname, sdata in SPEZIES_DATEN.items():
        if sname.lower() == race_lower or sname.lower() in race_lower:
            spezies_data = sdata
            break

    if spezies_data:
        character.speed = spezies_data.get('geschwindigkeit', 9.0)
        # Waldelf-Sonderfall: 10,5m (in Abstammung gespeichert)
        if character.abstammung:
            abstammung_lower = character.abstammung.lower()
            if 'waldelf' in abstammung_lower:
                character.speed = 10.5
    else:
        character.speed = 9.0

    return spezies_data.get('tp_bonus', 0) if spezies_data else 0


def _apply_experience_data(character):
    # --- XP-Schwellen ---
    xp_thresholds = {
        1: 0, 2: 300, 3: 900, 4: 2700, 5: 6500,
        6: 14000, 7: 23000, 8: 34000, 9: 48000, 10: 64000,
        11: 85000, 12: 100000, 13: 120000, 14: 140000, 15: 165000,
        16: 195000, 17: 225000, 18: 265000, 19: 305000, 20: 355000,
    }
    character.experience = xp_thresholds.get(character.level, 0)
    if character.level >= 20:
        character.max_experience = character.experience
    else:
        character.max_experience = xp_thresholds.get(character.level + 1, 355000)


def _apply_combat_and_magic_data(character, hit_die, tp_bonus):
    # --- Trefferpunkte ---
    _calculate_hp(character, hit_die, tp_bonus)

    # --- Rüstungsklasse (klassenspezifisch) ---
    character.armor_class = character.get_unarmored_ac()

    # --- ASI-Punkte ---
    asi_levels = _get_asi_levels(character.character_class)
    character.available_stat_points = sum(2 for l in asi_levels if l <= character.level)

    # --- Trefferwürfel ---
    character.hit_dice_total = character.level

    # --- Zauberplätze und bekannte Zauber ---
    character.spell_slots = character.get_spell_slots_for_level()
    available = character.get_available_spells()
    all_spell_names = []
    for grad, spells in available.items():
        for s in spells:
            all_spell_names.append(s['name'])
    character.known_spells = all_spell_names


def _apply_all_rules(character, hit_die):
    """Wendet alle regelbasierten Werte auf einen neuen Charakter an.

    Muss nach Stat-Zuweisung und Hintergrund-Boni aufgerufen werden.
    """
    _apply_class_data(character)
    _apply_background_data(character)
    tp_bonus = _apply_species_data(character)
    _apply_experience_data(character)
    _apply_combat_and_magic_data(character, hit_die, tp_bonus)



# ---------------------------------------------------------------------------
# ASI-Stufen pro Klasse
# ---------------------------------------------------------------------------

_FIGHTER_ASI_LEVELS = {4, 6, 8, 12, 14, 16, 19}
_ROGUE_ASI_LEVELS = {4, 8, 10, 12, 16, 19}
_DEFAULT_ASI_LEVELS = {4, 8, 12, 16, 19}


def _get_asi_levels(class_name):
    """Gibt die ASI-Stufen für eine Klasse zurück."""
    lower = class_name.lower()
    if 'kämpfer' in lower or 'fighter' in lower:
        return _FIGHTER_ASI_LEVELS
    if 'schurke' in lower or 'rogue' in lower:
        return _ROGUE_ASI_LEVELS
    return _DEFAULT_ASI_LEVELS


# ---------------------------------------------------------------------------
# Views
# ---------------------------------------------------------------------------

def register(request):
    """Neuen Benutzer registrieren."""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'characters/register.html', {'form': form})


@login_required
def dashboard(request):
    """Übersicht aller Charaktere des angemeldeten Benutzers."""
    characters = Character.objects.filter(user=request.user).only(
        'id', 'name', 'level', 'image', 'race', 'character_class',
        'current_hp', 'max_hp',
    )
    return render(request, 'characters/dashboard.html', {'characters': characters})


@login_required
def create_character(request):
    """Bestehenden Charakter mit Stufe importieren und Werte automatisch berechnen."""
    if request.method == 'POST':
        form = CharacterForm(request.POST, request.FILES)
        if form.is_valid():
            character = form.save(commit=False)
            if character.image:
                character.image = compress_character_image(character.image)
            character.user = request.user

            # Ausrüstung oder Gold
            _assign_equipment(character, form.cleaned_data.get('equipment_preference'))

            # Stat-Zuweisung basierend auf Klasse (Standard-Array)
            hit_die = _assign_stats(character)

            # Hintergrund-Boni
            _apply_background_bonuses(character)

            # Stufenbasierte Grundwerte
            character.level = form.cleaned_data.get('level', 1)

            # Alle Regeln anwenden (Übungen, RK, TP, Speed, Zauber etc.)
            _apply_all_rules(character, hit_die)

            character.save()

            # Features bis zur aktuellen Stufe (inkl. Unterklasse)
            character.features = character.get_all_features_up_to_level()
            character.save()

            return redirect('character_detail', pk=character.pk)
    else:
        form = CharacterForm()
    return render(request, 'characters/character_form.html', {'form': form})


@login_required
def character_detail(request, pk):
    """Charakterbogen anzeigen."""
    character = get_object_or_404(Character, pk=pk, user=request.user)

    waffen_json = json.dumps(WAFFEN_DATEN, ensure_ascii=False)
    meisterung_json = json.dumps(WAFFEN_MEISTERUNGEN, ensure_ascii=False)

    # Zauber-Daten
    spell_slots = character.get_spell_slots_for_level()
    known_spells_detail = character.get_known_spells_detail()

    return render(request, 'characters/character_detail.html', {
        'character': character,
        'waffen_json': waffen_json,
        'meisterung_json': meisterung_json,
        'spell_slots': spell_slots,
        'known_spells_detail': known_spells_detail,
    })



def _get_new_subclass_features(character, new_level):
    new_subclass_features = []
    if character.subclass:
        klasse_data = character._get_klasse_data()
        if klasse_data:
            unterklassen = klasse_data.get('unterklassen', {})
            for uk_name, uk_data in unterklassen.items():
                if uk_name.lower() == character.subclass.lower() or uk_name == character.subclass:
                    new_subclass_features = uk_data.get(new_level, [])
                    break
    return new_subclass_features

def _apply_levelup_hp_increase(character, rolled_hp=None):
    try:
        hit_die_value = int(character.hit_dice.split('d')[1])
        if rolled_hp is not None:
            hp_increase = rolled_hp + character.constitution_mod
        else:
            hp_increase = (hit_die_value // 2) + 1 + character.constitution_mod

        race_lower = character.race.lower()
        for sname, sdata in SPEZIES_DATEN.items():
            if sname.lower() == race_lower or sname.lower() in race_lower:
                tp_bonus = sdata.get('tp_bonus', 0)
                if tp_bonus:
                    hp_increase += tp_bonus
                break

        character.max_hp += hp_increase
        character.current_hp = character.max_hp
    except (ValueError, IndexError):
        logger = logging.getLogger(__name__)
        logger.warning(
            'Ungültiges Trefferwürfel-Format "%s" für Charakter %s (ID: %s)',
            character.hit_dice, character.name, character.pk,
        )

def _append_new_features(character, new_features, new_subclass_features):
    current_features = character.features or []
    for feat in new_features:
        current_features.append({
            'stufe': character.level,
            'name': feat['name'],
            'beschreibung': feat['beschreibung'],
        })
    for feat in new_subclass_features:
        current_features.append({
            'stufe': character.level,
            'unterklasse': True,
            'name': feat['name'],
            'beschreibung': feat['beschreibung'],
        })
    character.features = current_features

@login_required
def character_levelup(request, pk):
    """Stufenaufstieg durchführen."""
    character = get_object_or_404(Character, pk=pk, user=request.user)

    new_level = character.level + 1

    # Features für die neue Stufe aus den Regeldaten laden (Klasse + Unterklasse)
    new_features = character.get_features_for_level(new_level)

    # Unterklassen-Features für die neue Stufe laden
    new_subclass_features = _get_new_subclass_features(character, new_level)

    try:
        hit_die_value = int(character.hit_dice.split('d')[1])
    except (ValueError, IndexError):
        hit_die_value = 0

    if request.method == 'POST':
        character.level = new_level

        rolled_hp_str = request.POST.get('rolled_hp')
        rolled_hp = None
        if rolled_hp_str and rolled_hp_str.isdigit():
            rolled_hp = int(rolled_hp_str)

        # TP-Erhöhung: Eingegebener Wert oder Durchschnitt des Trefferwürfels + KON-Modifikator
        _apply_levelup_hp_increase(character, rolled_hp)

        # Attributsverbesserung (ASI) prüfen
        asi_levels = _get_asi_levels(character.character_class)
        if character.level in asi_levels:
            character.available_stat_points += 2

        # Klassen-Features zur Feature-Liste hinzufügen
        _append_new_features(character, new_features, new_subclass_features)

        # Trefferwürfel-Anzahl aktualisieren
        character.hit_dice_total = character.level

        # Rüstungsklasse neu berechnen (für Klassen die von Stufe abhängen)
        character.armor_class = character.get_unarmored_ac()

        # Zauberplätze und bekannte Zauber aktualisieren
        character.spell_slots = character.get_spell_slots_for_level()
        available = character.get_available_spells()
        all_spell_names = []
        for grad, spells in available.items():
            for s in spells:
                all_spell_names.append(s['name'])
        character.known_spells = all_spell_names

        character.save()
        return redirect('character_detail', pk=character.pk)

    return render(request, 'characters/character_levelup.html', {
        'character': character,
        'new_level': new_level,
        'new_features': new_features,
        'new_subclass_features': new_subclass_features,
        'hit_die_value': hit_die_value,
    })


@login_required
@require_POST
def update_character_stat(request, pk):
    """AJAX-Endpunkt: Einzelnes Attribut erhöhen oder senken."""
    character = get_object_or_404(Character, pk=pk, user=request.user)

    data, error_response = _parse_json_request(request)
    if error_response:
        return error_response

    stat = data.get('stat')
    action = data.get('action')

    if stat not in ABILITY_NAMES:
        return JsonResponse(
            {'success': False, 'error': 'Ungültiges Attribut.'},
            status=400,
        )

    if action not in ('increase', 'decrease'):
        return JsonResponse(
            {'success': False, 'error': 'Ungültige Aktion.'},
            status=400,
        )

    current_value = getattr(character, stat)
    old_con_mod = character.constitution_mod
    old_dex_mod = character.dexterity_mod

    if action == 'increase':
        if current_value >= 30:
            return JsonResponse(
                {'success': False, 'error': 'Attribut ist bereits am Maximum (30).'},
                status=400,
            )
        if character.available_stat_points <= 0:
            return JsonResponse(
                {'success': False, 'error': 'Keine verfügbaren Attributspunkte vorhanden.'},
                status=400,
            )
        setattr(character, stat, current_value + 1)
        character.available_stat_points -= 1
    else:  # decrease
        if current_value <= 1:
            return JsonResponse(
                {'success': False, 'error': 'Attribut kann nicht unter 1 sinken.'},
                status=400,
            )
        setattr(character, stat, current_value - 1)
        character.available_stat_points += 1

    # Abgeleitete Werte aktualisieren, wenn sich Modifikatoren ändern
    new_con_mod = character.constitution_mod
    new_dex_mod = character.dexterity_mod

    if old_con_mod != new_con_mod:
        hp_diff = (new_con_mod - old_con_mod) * character.level
        character.max_hp += hp_diff
        character.current_hp += hp_diff

    if old_dex_mod != new_dex_mod:
        character.armor_class += (new_dex_mod - old_dex_mod)

    character.save()

    # Modifikator-Anzeige formatieren
    new_mod = getattr(character, f'{stat}_mod')
    mod_display = f'+{new_mod}' if new_mod >= 0 else str(new_mod)

    return JsonResponse({
        'success': True,
        'new_value': getattr(character, stat),
        'new_mod': mod_display,
        'new_max_hp': character.max_hp,
        'new_current_hp': character.current_hp,
        'new_ac': character.armor_class,
        'new_available_points': character.available_stat_points,
    })


# ---------------------------------------------------------------------------
# Charakter-Builder (Wizard)
# ---------------------------------------------------------------------------

@functools.lru_cache(maxsize=1)
def _get_builder_json_data():
    """Cached static JSON data for character builder."""
    # Klassen-Daten für das Frontend aufbereiten
    klassen_json = {}
    for name, data in KLASSEN_DATEN.items():
        beschr = KLASSEN_BESCHREIBUNGEN.get(name, {})
        unterklassen = {}
        for uk_name in data.get('unterklassen', {}):
            uk_beschr = UNTERKLASSEN_BESCHREIBUNGEN.get(uk_name, {})
            # Alle Features der Unterklasse (alle Stufen)
            uk_features = data['unterklassen'][uk_name]
            alle_features = {}
            for lvl in sorted(uk_features.keys()):
                alle_features[str(lvl)] = [
                    {'name': f['name'], 'beschreibung': f.get('beschreibung', '')}
                    for f in uk_features[lvl]
                ]
            unterklassen[uk_name] = {
                'beschreibung': uk_beschr.get('beschreibung', ''),
                'bild': uk_beschr.get('bild', ''),
                'features': alle_features,
            }

        # Alle Klassen-Features für Detail-Ansicht
        alle_klassen_features = {}
        for lvl, feats in data.get('features', {}).items():
            alle_klassen_features[str(lvl)] = [
                {'name': f['name'], 'beschreibung': f.get('beschreibung', '')}
                for f in feats
            ]

        klassen_json[name] = {
            'beschreibung': beschr.get('beschreibung', ''),
            'vorteile': beschr.get('vorteile', []),
            'bild': beschr.get('bild', ''),
            'trefferwuerfel': data.get('trefferwuerfel', 'd8'),
            'rettungswuerfe': data.get('rettungswuerfe', []),
            'ruestungen': data.get('ruestungen', []),
            'waffen': data.get('waffen', []),
            'zauberattribut': data.get('zauberattribut'),
            'features': alle_klassen_features,
            'unterklassen': unterklassen,
        }

    # Hintergrund-Daten für das Frontend
    hintergruende_json = {}
    for name, data in HINTERGRUND_DATEN.items():
        beschr = HINTERGRUND_BESCHREIBUNGEN.get(name, {})
        attr = data.get('attribute', {})
        a_map = {
            'strength': 'Stärke', 'dexterity': 'Geschicklichkeit',
            'constitution': 'Konstitution', 'intelligence': 'Intelligenz',
            'wisdom': 'Weisheit', 'charisma': 'Charisma',
        }
        hintergruende_json[name] = {
            'beschreibung': beschr.get('beschreibung', ''),
            'bild': beschr.get('bild', ''),
            'primaer': a_map.get(attr.get('primary', ''), ''),
            'sekundaer': a_map.get(attr.get('secondary', ''), ''),
            'talent': data.get('talent', ''),
            'fertigkeiten': data.get('fertigkeiten', []),
            'werkzeug': data.get('werkzeug', ''),
        }

    # Spezies-Daten für das Frontend
    spezies_json = {}
    for name, data in SPEZIES_DATEN.items():
        merkmale = [
            {'name': m['name'], 'beschreibung': m.get('beschreibung', '')}
            for m in data.get('merkmale', [])
        ]
        abstammungen = {}
        for ab_name, ab_traits in data.get('abstammungen', {}).items():
            abstammungen[ab_name] = [
                {'name': t['name'], 'beschreibung': t.get('beschreibung', '')}
                for t in ab_traits
            ]
        spezies_json[name] = {
            'groesse': data.get('groesse', 'Mittel'),
            'geschwindigkeit': data.get('geschwindigkeit', 30),
            'merkmale': merkmale,
            'tp_bonus': data.get('tp_bonus', 0),
            'abstammungen': abstammungen,
        }

    return {
        'klassen_json': json.dumps(klassen_json, ensure_ascii=False),
        'hintergruende_json': json.dumps(hintergruende_json, ensure_ascii=False),
        'spezies_json': json.dumps(spezies_json, ensure_ascii=False),
    }

@login_required
def character_builder(request):
    """Interaktiver Charakter-Builder – liefert alle Regeldaten als JSON an das Template."""
    context = _get_builder_json_data()
    return render(request, 'characters/character_builder.html', context)


@login_required
@require_POST
def character_builder_submit(request):
    """Verarbeitet die Daten aus dem Charakter-Builder Wizard."""
    data = request.POST
    character = Character(user=request.user)

    # Grunddaten
    character.name = data.get('name', 'Unbenannt')
    character.character_class = data.get('character_class', '')
    character.subclass = data.get('subclass', '')
    character.background = data.get('background', '')
    character.race = data.get('race', 'Mensch')
    character.abstammung = data.get('abstammung', '')
    character.alignment = data.get('alignment', '')
    character.personality_traits = data.get('personality_traits', '')
    character.ideals = data.get('ideals', '')
    character.bonds = data.get('bonds', '')
    character.flaws = data.get('flaws', '')

    # Level
    try:
        character.level = max(1, min(20, int(data.get('level', 1))))
    except (ValueError, TypeError):
        character.level = 1

    # Ausrüstung oder Gold
    _assign_equipment(character, data.get('equipment_preference'))

    # Bild (komprimiert auf max. 512×512 WebP)
    if 'image' in request.FILES:
        character.image = compress_character_image(request.FILES['image'])

    # Stat-Zuweisung basierend auf Klasse
    hit_die = _assign_stats(character)

    # Hintergrund-Boni
    _apply_background_bonuses(character)

    # Alle Regeln anwenden (Übungen, RK, TP, Speed, Zauber etc.)
    _apply_all_rules(character, hit_die)

    character.save()

    # Features bis zur aktuellen Stufe (inkl. Unterklasse)
    character.features = character.get_all_features_up_to_level()
    character.save()

    return redirect('character_detail', pk=character.pk)


@login_required
@require_POST
def update_character_coin(request, pk):
    """AJAX-Endpunkt: Einzelnes Münz-Attribut erhöhen oder senken."""
    character = get_object_or_404(Character, pk=pk, user=request.user)

    data, error_response = _parse_json_request(request)
    if error_response:
        return error_response

    coin = data.get('coin')
    action = data.get('action')

    if coin not in ('gold', 'silver', 'copper'):
        return JsonResponse(
            {'success': False, 'error': 'Ungültige Münze.'},
            status=400,
        )

    if action not in ('increase', 'decrease'):
        return JsonResponse(
            {'success': False, 'error': 'Ungültige Aktion.'},
            status=400,
        )

    current_value = getattr(character, coin)

    if action == 'increase':
        setattr(character, coin, current_value + 1)
    else:  # decrease
        if current_value <= 0:
            return JsonResponse(
                {'success': False, 'error': 'Münzanzahl kann nicht unter 0 sinken.'},
                status=400,
            )
        setattr(character, coin, current_value - 1)

    character.save()

    return JsonResponse({
        'success': True,
        'new_value': getattr(character, coin),
    })


@login_required
@require_POST
def add_character_weapon(request, pk):
    """AJAX-Endpunkt: Waffe zum Charakter hinzufügen."""
    character = get_object_or_404(Character, pk=pk, user=request.user)

    data, error_response = _parse_json_request(request)
    if error_response:
        return error_response

    weapon_name = data.get('name')
    weapon_type = data.get('type')
    hit = data.get('hit')
    damage = data.get('damage')

    if not weapon_name:
        return JsonResponse({'success': False, 'error': 'Waffenname fehlt.'}, status=400)

    new_weapon = {
        'name': weapon_name,
        'typ': weapon_type or '',
        'angriffsbonus': hit or '+0',
        'schaden': damage or '0'
    }

    current_weapons = character.weapons or []
    current_weapons.append(new_weapon)
    character.weapons = current_weapons
    character.save()

    return JsonResponse({'success': True, 'weapons': character.weapons})
