import logging

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import CharacterForm, UserRegisterForm
from .models import Character

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Konfigurationstabellen für die Charaktererstellung
# ---------------------------------------------------------------------------

# Stat-Priorität pro Klasse: Reihenfolge der Zuweisung des Standard-Arrays
# Standard-Array: [15, 14, 13, 12, 10, 8]
# Schlüssel: (deutsche Keywords, englische Keywords) → (Attribut-Reihenfolge, Trefferwürfel)
STANDARD_ARRAY = [15, 14, 13, 12, 10, 8]

ABILITY_NAMES = ('strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma')

CLASS_CONFIGS = {
    # keywords → (stat priority order, hit die)
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

# Hintergrund-Boni: keywords → (primäres Attribut +2, sekundäres Attribut +1)
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

# Klassen-basierter Fallback für unbekannte Hintergründe
_MELEE_CLASSES = {'barbar', 'kämpfer', 'paladin', 'fighter'}
_AGILE_CLASSES = {'schurke', 'mönch', 'waldläufer', 'rogue', 'monk', 'ranger'}


def _match_keywords(text, keyword_table):
    """Sucht den ersten Treffer in einer keyword→value Tabelle."""
    text_lower = text.lower()
    for keywords, value in keyword_table.items():
        if any(kw in text_lower for kw in keywords):
            return value
    return None


def _apply_background_bonuses(character):
    """Wendet Hintergrund-Boni auf das Charakterobjekt an."""
    bonuses = _match_keywords(character.background, BACKGROUND_BONUSES)

    if bonuses:
        primary, secondary = bonuses
        setattr(character, primary, getattr(character, primary) + 2)
        setattr(character, secondary, getattr(character, secondary) + 1)
        return

    # Fallback: Boni basierend auf Klassentyp
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
    """Neuen Charakter erstellen mit automatischer Werte-Berechnung."""
    if request.method == 'POST':
        form = CharacterForm(request.POST, request.FILES)
        if form.is_valid():
            character = form.save(commit=False)
            character.user = request.user

            # Ausrüstung oder Gold
            if form.cleaned_data.get('equipment_preference') == 'gold':
                character.gold = 100
                character.equipment = 'Nichts (Startgold gewählt)'
            else:
                character.gold = 0
                character.equipment = f'Standard-Ausrüstung für {character.character_class}'

            # Stat-Zuweisung basierend auf Klasse (Standard-Array)
            class_config = _match_keywords(character.character_class, CLASS_CONFIGS)
            if class_config:
                stat_order, hit_die = class_config
            else:
                stat_order = list(ABILITY_NAMES)
                hit_die = 'd8'

            for attr, value in zip(stat_order, STANDARD_ARRAY):
                setattr(character, attr, value)
            character.hit_dice = f'1{hit_die}'

            # Hintergrund-Boni
            _apply_background_bonuses(character)

            # Stufe-1 Grundwerte
            character.level = 1
            character.experience = 0
            character.max_experience = 300  # EP für Stufe 2

            # Maximale TP: Maximum des Trefferwürfels + KON-Modifikator
            hit_die_value = int(hit_die[1:])  # 'd10' → 10
            con_mod = character._ability_modifier(character.constitution)
            character.max_hp = hit_die_value + con_mod

            # Völker-spezifische TP-Boni
            race_lower = character.race.lower()
            if 'zwerg' in race_lower or 'dwarf' in race_lower:
                character.max_hp += 1

            character.current_hp = character.max_hp

            # Rüstungsklasse (ohne Rüstung) = 10 + GES-Modifikator
            character.armor_class = 10 + character._ability_modifier(character.dexterity)

            # Bewegungsrate
            character.speed = 30
            if 'waldelf' in race_lower or 'wood elf' in race_lower:
                character.speed = 35
            elif 'goliath' in race_lower:
                character.speed = 35

            character.save()
            return redirect('character_detail', pk=character.pk)
    else:
        form = CharacterForm()
    return render(request, 'characters/character_form.html', {'form': form})


@login_required
def character_detail(request, pk):
    """Charakterbogen anzeigen."""
    character = get_object_or_404(Character, pk=pk, user=request.user)
    return render(request, 'characters/character_detail.html', {'character': character})


@login_required
def character_levelup(request, pk):
    """Stufenaufstieg durchführen."""
    character = get_object_or_404(Character, pk=pk, user=request.user)
    new_level = character.level + 1

    # Features für die neue Stufe aus den Regeldaten laden
    new_features = character.get_features_for_level(new_level)

    if request.method == 'POST':
        character.level = new_level

        # TP-Erhöhung: Durchschnitt des Trefferwürfels + KON-Modifikator
        try:
            hit_die_value = int(character.hit_dice.split('d')[1])
            hp_increase = (hit_die_value // 2) + 1 + character.constitution_mod

            # Volk-spezifische TP-Boni
            race_lower = character.race.lower()
            if 'zwerg' in race_lower or 'dwarf' in race_lower:
                hp_increase += 1

            character.max_hp += hp_increase
            character.current_hp = character.max_hp
        except (ValueError, IndexError):
            logger.warning(
                'Ungültiges Trefferwürfel-Format "%s" für Charakter %s (ID: %s)',
                character.hit_dice, character.name, character.pk,
            )

        # Attributsverbesserung (ASI) prüfen
        asi_levels = _get_asi_levels(character.character_class)
        if character.level in asi_levels:
            character.available_stat_points += 2

        # Features zur Feature-Liste hinzufügen
        current_features = character.features or []
        for feat in new_features:
            current_features.append({
                'stufe': character.level,
                'name': feat['name'],
                'beschreibung': feat['beschreibung'],
            })
        character.features = current_features

        # Trefferwürfel-Anzahl aktualisieren
        character.hit_dice_total = character.level

        character.save()
        return redirect('character_detail', pk=character.pk)

    return render(request, 'characters/character_levelup.html', {
        'character': character,
        'new_level': new_level,
        'new_features': new_features,
    })


@login_required
@require_POST
def update_character_stat(request, pk):
    """AJAX-Endpunkt: Einzelnes Attribut erhöhen oder senken."""
    character = get_object_or_404(Character, pk=pk, user=request.user)

    try:
        import json
        data = json.loads(request.body)
    except (json.JSONDecodeError, ValueError):
        return JsonResponse(
            {'success': False, 'error': 'Ungültige Anfragedaten.'},
            status=400,
        )

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
