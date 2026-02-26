from django.db import models
from django.contrib.auth.models import User

class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Grunddaten
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=1)
    image = models.ImageField(upload_to='character_images/', blank=True, null=True)
    character_class = models.CharField(max_length=100)
    subclass = models.CharField(max_length=100, blank=True)
    race = models.CharField(max_length=100)
    background = models.CharField(max_length=100)
    alignment = models.CharField(max_length=50)
    
    # Werte (Stats)
    strength = models.IntegerField(default=10)
    dexterity = models.IntegerField(default=10)
    constitution = models.IntegerField(default=10)
    intelligence = models.IntegerField(default=10)
    wisdom = models.IntegerField(default=10)
    charisma = models.IntegerField(default=10)
    
    # Kampf & Leben
    armor_class = models.IntegerField(default=10)
    speed = models.IntegerField(default=30)
    max_hp = models.IntegerField(default=10)
    current_hp = models.IntegerField(default=10)
    temp_hp = models.IntegerField(default=0)
    hit_dice = models.CharField(max_length=20, default="1d10")
    hit_dice_total = models.IntegerField(default=1)
    
    # Ausrüstung & Gold
    equipment = models.TextField(blank=True, help_text="Inventar")
    gold = models.IntegerField(default=0)
    silver = models.IntegerField(default=0)
    copper = models.IntegerField(default=0)

    # New JSON Fields for richer data
    proficiencies = models.JSONField(default=list, blank=True)
    weapons = models.JSONField(default=list, blank=True)
    inventory = models.JSONField(default=list, blank=True)
    spell_slots = models.JSONField(default=dict, blank=True)

    # Experience
    experience = models.IntegerField(default=0)
    max_experience = models.IntegerField(default=10000)
    
    # Hintergrund & Flavor
    personality_traits = models.TextField(blank=True)
    ideals = models.TextField(blank=True)
    bonds = models.TextField(blank=True)
    flaws = models.TextField(blank=True)
    backstory = models.TextField(blank=True)
    appearance = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} (Level {self.level} {self.race} {self.character_class})"

    @property
    def strength_mod(self):
        return (self.strength - 10) // 2

    @property
    def dexterity_mod(self):
        return (self.dexterity - 10) // 2

    @property
    def constitution_mod(self):
        return (self.constitution - 10) // 2

    @property
    def intelligence_mod(self):
        return (self.intelligence - 10) // 2

    @property
    def wisdom_mod(self):
        return (self.wisdom - 10) // 2

    @property
    def charisma_mod(self):
        return (self.charisma - 10) // 2
