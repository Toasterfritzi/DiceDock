import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dicedock_project.settings")
django.setup()

from django.contrib.auth.models import User
from characters.models import Character

user = User.objects.create_user(username='testuser', password='password123')
character = Character.objects.create(
    user=user,
    name="Test Character",
    character_class="Warrior",
    race="Human",
    level=1,
    experience=0,
    max_experience=300,
    strength=15, dexterity=12, constitution=14, intelligence=10, wisdom=10, charisma=12
)
print("Created test user and character.")
