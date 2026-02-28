from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Character

class CharacterCreationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client = Client()
        self.client.login(username='testuser', password='password123')

    def test_character_creation_form_submission(self):
        response = self.client.post('/create/', {
            'name': 'Test Character',
            'character_class': 'Warrior',
            'subclass': 'Champion',
            'race': 'Human',
            'background': 'Soldier',
            'alignment': 'Neutral Good',
            'personality_traits': 'Brave',
            'ideals': 'Honor',
            'bonds': 'Kingdom',
            'flaws': 'Stubborn',
            'strength': 15,
            'dexterity': 12,
            'constitution': 14,
            'intelligence': 10,
            'wisdom': 10,
            'charisma': 12,
            'equipment_preference': 'equipment',
        })

        # Check redirect (success)
        if response.status_code != 302:
            print(response.content.decode()) # Debugging if fails

        self.assertEqual(response.status_code, 302)

        # Check character was created
        self.assertTrue(Character.objects.filter(name='Test Character').exists())

        char = Character.objects.get(name='Test Character')
        self.assertEqual(char.user, self.user)
        self.assertEqual(char.character_class, 'Warrior')
        self.assertEqual(char.strength, 17)
        # Check equipment handling logic (based on views.py logic)
        self.assertEqual(char.gold, 0)
        self.assertTrue("Standard-Ausrüstung" in char.equipment)

    def test_character_creation_gold_option(self):
        response = self.client.post('/create/', {
            'name': 'Gold Character',
            'character_class': 'Rogue',
            'race': 'Elf',
            'background': 'Criminal',
            'alignment': 'Chaotic Neutral',
            'strength': 10,
            'dexterity': 10,
            'constitution': 10,
            'intelligence': 10,
            'wisdom': 10,
            'charisma': 10,
            'equipment_preference': 'gold',
        })

        # Check redirect (success)
        self.assertEqual(response.status_code, 302)

        char = Character.objects.get(name='Gold Character')
        self.assertEqual(char.gold, 100)
        self.assertTrue("Startgold gewählt" in char.equipment)

from .forms import UserRegisterForm

class UserRegisterFormTest(TestCase):
    def test_passwords_match(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'StrongPassword123!',
            'password_confirm': 'StrongPassword123!',
        }
        form = UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_passwords_mismatch(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'StrongPassword123!',
            'password_confirm': 'StrongPassword321!',
        }
        form = UserRegisterForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("Passwords do not match!", form.errors.get("password_confirm", []))
