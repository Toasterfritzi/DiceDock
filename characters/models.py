from django.db import models
from django.contrib.auth.models import User
from .rules_data.spezies import SPEZIES_DATEN
from .rules_data.zauber import ZAUBER, ZAUBERLISTEN, ZAUBER_OHNE_KLASSEN
from .rules_data.zauberplaetze import ZAUBERPLATZ_TABELLE

_SPEZIES_DATEN_LOWER = {k.lower(): v for k, v in SPEZIES_DATEN.items()}



_PRECOMPUTED_SPELL_LISTS = {}

class Character(models.Model):
    """A D&D player character with stats, equipment, and personality."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='characters')

    # Grunddaten
    name = models.CharField('Name', max_length=100)
    level = models.IntegerField('Stufe', default=1)
    image = models.ImageField('Charakterbild', upload_to='character_images/', blank=True, null=True)
    character_class = models.CharField('Klasse', max_length=100)
    subclass = models.CharField('Unterklasse', max_length=100, blank=True)
    race = models.CharField('Volk', max_length=100)
    abstammung = models.CharField('Abstammung', max_length=100, blank=True)
    background = models.CharField('Hintergrund', max_length=100)
    alignment = models.CharField('Gesinnung', max_length=50, blank=True)

    # Attribute
    strength = models.IntegerField('Stärke', default=10)
    dexterity = models.IntegerField('Geschicklichkeit', default=10)
    constitution = models.IntegerField('Konstitution', default=10)
    intelligence = models.IntegerField('Intelligenz', default=10)
    wisdom = models.IntegerField('Weisheit', default=10)
    charisma = models.IntegerField('Charisma', default=10)
    available_stat_points = models.IntegerField('Verfügbare Attributspunkte', default=0)

    # Kampf & Leben
    armor_class = models.IntegerField('Rüstungsklasse', default=10)
    speed = models.FloatField('Bewegung (m)', default=9.0)
    max_hp = models.IntegerField('Maximale Trefferpunkte', default=10)
    current_hp = models.IntegerField('Aktuelle Trefferpunkte', default=10)
    temp_hp = models.IntegerField('Temporäre Trefferpunkte', default=0)
    hit_dice = models.CharField('Trefferwürfel', max_length=20, default='1d10')
    hit_dice_total = models.IntegerField('Trefferwürfel gesamt', default=1)

    # Ausrüstung & Währung
    equipment = models.TextField('Ausrüstung', blank=True)
    gold = models.IntegerField('Gold', default=0)
    silver = models.IntegerField('Silber', default=0)
    copper = models.IntegerField('Kupfer', default=0)

    # Strukturierte Daten (JSON)
    proficiencies = models.JSONField('Übungen', default=list, blank=True)
    weapons = models.JSONField('Waffen', default=list, blank=True)
    inventory = models.JSONField('Inventar', default=list, blank=True)
    spell_slots = models.JSONField('Zauberplätze', default=dict, blank=True)
    features = models.JSONField('Merkmale', default=list, blank=True)
    feats = models.JSONField('Talente', default=list, blank=True)
    saving_throw_proficiencies = models.JSONField('Rettungswurf-Übungen', default=list, blank=True)
    skill_proficiencies = models.JSONField('Fertigkeits-Übungen', default=list, blank=True)
    skill_expertises = models.JSONField('Fertigkeits-Expertisen', default=list, blank=True)
    tool_proficiencies = models.JSONField('Werkzeug-Übungen', default=list, blank=True)
    known_spells = models.JSONField('Bekannte Zauber', default=list, blank=True)

    # Erfahrung
    experience = models.IntegerField('Erfahrungspunkte', default=0)
    max_experience = models.IntegerField('EP für nächste Stufe', default=10000)

    # Persönlichkeit & Hintergrund
    personality_traits = models.TextField('Persönlichkeitsmerkmale', blank=True)
    ideals = models.TextField('Ideale', blank=True)
    bonds = models.TextField('Bindungen', blank=True)
    flaws = models.TextField('Makel', blank=True)
    backstory = models.TextField('Hintergrundgeschichte', blank=True)
    appearance = models.TextField('Aussehen', blank=True)

    class Meta:
        verbose_name = 'Charakter'
        verbose_name_plural = 'Charaktere'
        ordering = ['-level', 'name']

    def __str__(self):
        return f'{self.name} (Stufe {self.level} {self.race} {self.character_class})'

    # --- Attributs-Modifikatoren ---

    def _ability_modifier(self, score):
        """Berechnet den D&D-Modifikator: (Wert - 10) // 2."""
        return (score - 10) // 2

    @property
    def strength_mod(self):
        return self._ability_modifier(self.strength)

    @property
    def dexterity_mod(self):
        return self._ability_modifier(self.dexterity)

    @property
    def constitution_mod(self):
        return self._ability_modifier(self.constitution)

    @property
    def intelligence_mod(self):
        return self._ability_modifier(self.intelligence)

    @property
    def wisdom_mod(self):
        return self._ability_modifier(self.wisdom)

    @property
    def charisma_mod(self):
        return self._ability_modifier(self.charisma)

    @property
    def proficiency_bonus(self):
        """Übungsbonus basierend auf der Stufe (PHB-Tabelle)."""
        if self.level >= 17:
            return 6
        if self.level >= 13:
            return 5
        if self.level >= 9:
            return 4
        if self.level >= 5:
            return 3
        return 2

    def _get_klasse_data(self):
        if getattr(self, '_klasse_class_cache', None) == self.character_class:
            return self._klasse_data_cache

        from .rules_data.klassen import KLASSEN_DATEN
        result = None
        for k in KLASSEN_DATEN:
            if k.lower() in self.character_class.lower():
                result = KLASSEN_DATEN[k]
                break

        self._klasse_class_cache = self.character_class
        self._klasse_data_cache = result
        return result

    def get_features_for_level(self, level):
        """Gibt alle Klassen-Features für eine bestimmte Stufe zurück."""
        klasse = self._get_klasse_data()
        if not klasse:
            return []
        return klasse.get('features', {}).get(level, [])

    def get_all_features_up_to_level(self):
        """Gibt alle Klassen- UND Unterklassen-Features bis zur aktuellen Stufe zurück."""
        klasse = self._get_klasse_data()
        if not klasse:
            return []

        level = self.level
        all_features = []

        # Klassen-Features
        features_dict = klasse.get('features', {})
        for lvl in range(1, level + 1):
            if lvl in features_dict:
                for f in features_dict[lvl]:
                    all_features.append({'stufe': lvl, **f})

        # Unterklassen-Features
        subclass = self.subclass
        if subclass:
            unterklassen = klasse.get('unterklassen', {})

            # Direct lookup first
            uk_features = unterklassen.get(subclass)

            # Fallback to case-insensitive lookup
            if not uk_features:
                subclass_lower = subclass.lower()
                for uk_name, uk_data in unterklassen.items():
                    if uk_name.lower() == subclass_lower:
                        uk_features = uk_data
                        break

            if uk_features:
                for lvl in range(1, level + 1):
                    if lvl in uk_features:
                        for f in uk_features[lvl]:
                            all_features.append({'stufe': lvl, 'unterklasse': True, **f})

        return all_features

    def get_species_traits(self):
        """Gibt die Spezies-Merkmale zurück."""
        race_lower = self.race.lower()
        data = _SPEZIES_DATEN_LOWER.get(race_lower)
        if data:
            return data.get('merkmale', [])
        for name, data in _SPEZIES_DATEN_LOWER.items():
            if name in race_lower:
                return data.get('merkmale', [])
        return []

    # --- Zauber-Methoden ---

    def get_spell_slots_for_level(self):
        """Gibt die Zauberplätze für die aktuelle Stufe und den Zaubertyp zurück."""
        klasse = self._get_klasse_data()
        if not klasse:
            return {}
        zaubertyp = klasse.get('zaubertyp')
        if not zaubertyp:
            return {}
        tabelle = ZAUBERPLATZ_TABELLE.get(zaubertyp, {})
        if zaubertyp == 'paktmagie':
            pakt = tabelle.get(self.level, {})
            if pakt:
                return {'pakt_anzahl': pakt['anzahl'], 'pakt_grad': pakt['grad']}
            return {}
        return tabelle.get(self.level, {})

    def get_max_spell_grade(self):
        """Gibt den höchsten verfügbaren Zaubergrad zurück."""
        slots = self.get_spell_slots_for_level()
        if not slots:
            return 0
        if 'pakt_grad' in slots:
            return slots['pakt_grad']
        return max(slots.keys()) if slots else 0

    def get_available_spells(self):
        """Gibt alle für diese Klasse+Stufe verfügbaren Zauber zurück, gruppiert nach Grad."""
        klasse_name = self.character_class
        if klasse_name not in ZAUBERLISTEN:
            return {}

        if klasse_name not in _PRECOMPUTED_SPELL_LISTS:
            _PRECOMPUTED_SPELL_LISTS[klasse_name] = {
                grad: [{'name': n, **ZAUBER_OHNE_KLASSEN[n]} for n in namen]
                for grad, namen in ZAUBERLISTEN[klasse_name].items()
            }

        alle_zauber = _PRECOMPUTED_SPELL_LISTS[klasse_name]
        max_grad = self.get_max_spell_grade()

        return {
            grad: zauber_liste
            for grad, zauber_liste in alle_zauber.items()
            if grad <= max_grad or grad == 0
        }

    def get_known_spells_detail(self):
        """Gibt die Details der bekannten Zauber zurück, gruppiert nach Grad."""
        result = {}
        for name in self.known_spells:
            if name in ZAUBER:
                z = ZAUBER[name]
                grad = z['grad']
                result.setdefault(grad, []).append({
                    'name': name,
                    'schule': z.get('schule', ''),
                    'wirkzeit': z.get('wirkzeit', ''),
                    'reichweite': z.get('reichweite', ''),
                    'dauer': z.get('dauer', ''),
                    'beschreibung': z.get('beschreibung', ''),
                })
        for grad in result:
            result[grad].sort(key=lambda x: x['name'])
        return result

    # --- Abgeleitete Kampfwerte ---

    def get_unarmored_ac(self):
        """Berechnet die RK ohne Rüstung basierend auf Klasse."""
        klasse = self._get_klasse_data()
        base_class = self.character_class.lower() if self.character_class else ''

        if 'barbar' in base_class:
            return 10 + self.dexterity_mod + self.constitution_mod
        if 'mönch' in base_class or 'monk' in base_class:
            return 10 + self.dexterity_mod + self.wisdom_mod

        # Zauberer Drachenblut-Linie (Unterklasse ab Stufe 3)
        if 'zauberer' in base_class and self.subclass:
            if 'drachenblut' in self.subclass.lower() and self.level >= 3:
                return 13 + self.dexterity_mod

        # Barde Schule des Tanzes (Unterklasse ab Stufe 3)
        if 'bard' in base_class and self.subclass:
            if 'tanz' in self.subclass.lower() and self.level >= 3:
                return 10 + self.dexterity_mod + self.charisma_mod

        return 10 + self.dexterity_mod

    @property
    def has_spellcasting(self):
        """Gibt zurück, ob der Charakter zaubern kann (hat ein Zauberattribut)."""
        klasse = self._get_klasse_data()
        return bool(klasse and klasse.get('zauberattribut'))

    @property
    def spellcasting_ability_mod(self):
        """Gibt den Modifikator des Zauberattributs zurück."""
        if not self.has_spellcasting:
            return 0
        attr = self._get_klasse_data().get('zauberattribut')
        mapping = {
            'charisma': self.charisma_mod,
            'wisdom': self.wisdom_mod,
            'intelligence': self.intelligence_mod,
        }
        return mapping.get(attr, 0)

    @property
    def spell_save_dc(self):
        """Zauber-SG = 8 + Übungsbonus + Zauberattribut-Mod."""
        if not self.has_spellcasting:
            return 0
        return 8 + self.proficiency_bonus + self.spellcasting_ability_mod

    @property
    def spell_attack_bonus(self):
        """Zauber-Angriffswurf = Übungsbonus + Zauberattribut-Mod."""
        if not self.has_spellcasting:
            return 0
        return self.proficiency_bonus + self.spellcasting_ability_mod
