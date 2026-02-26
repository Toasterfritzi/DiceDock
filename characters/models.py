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
    
    # Ausrüstung & Gold
    equipment = models.TextField(blank=True, help_text="Inventar")
    gold = models.IntegerField(default=0)
    
    # Hintergrund & Flavor
    personality_traits = models.TextField(blank=True)
    ideals = models.TextField(blank=True)
    bonds = models.TextField(blank=True)
    flaws = models.TextField(blank=True)
    backstory = models.TextField(blank=True)
    appearance = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} (Level {self.level} {self.race} {self.character_class})"
