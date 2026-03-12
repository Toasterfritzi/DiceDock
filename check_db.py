import os
import sys
import django

sys.path.append(r'c:\dicecock\DiceDock')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dicedock_project.settings')
django.setup()

from characters.forms import get_class_choices
from characters.models import Character

print("Class Choices:", get_class_choices())

for c in Character.objects.all():
    print(f"ID {c.id}: Name='{c.name}', Class='{c.character_class}', Subclass='{c.subclass}', Race='{c.race}'")

