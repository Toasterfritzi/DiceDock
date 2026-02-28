import json
from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Character
from .forms import UserRegisterForm

class CharacterCreationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
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
        self.assertIn("Passwords do not match!", form.non_field_errors())

    def test_password_too_short(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'short',
            'password_confirm': 'short',
        }
        form = UserRegisterForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password', form.errors)
        # Check that the error message mentions length
        self.assertTrue(any("too short" in str(err) for err in form.errors['password']))

    def test_password_entirely_numeric(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': '1234567890',
            'password_confirm': '1234567890',
        }
        form = UserRegisterForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password', form.errors)
        self.assertTrue(any("entirely numeric" in str(err) for err in form.errors['password']))

    def test_password_too_common(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password123',
            'password_confirm': 'password123',
        }
        form = UserRegisterForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password', form.errors)
        self.assertTrue(any("too common" in str(err) for err in form.errors['password']))

    def test_password_too_similar_to_username(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testuser123',
            'password_confirm': 'testuser123',
        }
        form = UserRegisterForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password', form.errors)
        self.assertTrue(any("too similar" in str(err) for err in form.errors['password']))

class CharacterStatUpdateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='statuser', password='password123')
        self.client.login(username='statuser', password='password123')
        self.character = Character.objects.create(
            user=self.user,
            name='Stat Test Character',
            character_class='Warrior',
            strength=15,
            dexterity=14,
            constitution=13,
            intelligence=12,
            wisdom=10,
            charisma=8,
            level=1,
            max_hp=10,
            current_hp=10,
            armor_class=10,
            speed=30
        )

    def test_invalid_stat_update(self):
        response = self.client.post(
            reverse('update_character_stat', args=[self.character.pk]),
            data=json.dumps({'stat': 'invalid_stat', 'action': 'increase'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.content)
        self.assertFalse(response_data.get('success'))
        self.assertEqual(response_data.get('error'), 'Invalid stat')
