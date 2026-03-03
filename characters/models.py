from django.db import models
from django.contrib.auth.models import User
from .rules_data.spezies import SPEZIES_DATEN

_SPEZIES_DATEN_LOWER = {k.lower(): v for k, v in SPEZIES_DATEN.items()}


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
    background = models.CharField('Hintergrund', max_length=100)
    alignment = models.CharField('Gesinnung', max_length=50)

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
    speed = models.IntegerField('Bewegung', default=30)
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

    def get_features_for_level(self, level):
        """Gibt alle Klassen-Features für eine bestimmte Stufe zurück."""
        from .rules_data.klassen import KLASSEN_DATEN
        klasse = None
        for k in KLASSEN_DATEN:
            if k.lower() in self.character_class.lower():
                klasse = KLASSEN_DATEN[k]
                break
        if not klasse:
            return []
        return klasse.get('features', {}).get(level, [])

    def get_all_features_up_to_level(self):
        """Gibt alle Klassen-Features bis zur aktuellen Stufe zurück."""
        all_features = []
        for lvl in range(1, self.level + 1):
            features = self.get_features_for_level(lvl)
            for f in features:
                all_features.append({'stufe': lvl, **f})
        return all_features

    def get_species_traits(self):
        """Gibt die Spezies-Merkmale zurück."""
        race_lower = self.race.lower()
        # O(1) lookup
        data = _SPEZIES_DATEN_LOWER.get(race_lower)
        if data:
            return data.get('merkmale', [])

        # Fallback for substring matching (e.g. "Hochelf" where "elf" is in SPEZIES_DATEN)
        for name, data in _SPEZIES_DATEN_LOWER.items():
            if name in race_lower:
                return data.get('merkmale', [])
        return []
