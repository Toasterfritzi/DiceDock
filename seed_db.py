import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dicedock_project.settings')
django.setup()

from django.contrib.auth.models import User
from characters.models import Character

user, created = User.objects.get_or_create(username='testuser')
if created:
    user.set_password('testpassword')
    user.save()

char, created = Character.objects.get_or_create(
    user=user,
    name='TestChar',
    defaults={
        'character_class': 'Kämpfer',
        'level': 1,
        'hit_dice': '1d10',
        'constitution': 14,
        'max_hp': 12,
        'current_hp': 12,
        'experience': 300
    }
)
print("Character created. ID:", char.id)
