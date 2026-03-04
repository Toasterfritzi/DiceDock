import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dicedock_project.settings")
django.setup()

from django.contrib.auth.models import User
from characters.models import Character

user = User.objects.create_user(username='testuser', password='password123')
character = Character.objects.create(
    user=user,
    name="Testcharakter",
    character_class="Kämpfer",  # Gültiger D&D 5.5e Klassenname (deutsch)
    race="Mensch",              # Gültiger Spezies-Name (deutsch)
    level=1,
    experience=0,
    max_experience=300,        # XP-Schwelle für Stufe 2 (Stufe 3: 900, Stufe 4: 2700 usw.)
    strength=15, dexterity=12, constitution=14, intelligence=10, wisdom=10, charisma=12
)
print("Created test user and character.")
