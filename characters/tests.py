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

class CharacterModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='modeltestuser', password='password123')

    def test_ability_score_modifiers(self):
        # Create a character with mixed stats
        char = Character(
            user=self.user,
            name="Stat Test Character",
            strength=10,       # (10 - 10) // 2 = 0
            dexterity=12,      # (12 - 10) // 2 = 1
            constitution=15,   # (15 - 10) // 2 = 2
            intelligence=9,    # (9 - 10) // 2 = -1
            wisdom=8,          # (8 - 10) // 2 = -1
            charisma=20        # (20 - 10) // 2 = 5
        )

        self.assertEqual(char.strength_mod, 0)
        self.assertEqual(char.dexterity_mod, 1)
        self.assertEqual(char.constitution_mod, 2)
        self.assertEqual(char.intelligence_mod, -1)
        self.assertEqual(char.wisdom_mod, -1)
        self.assertEqual(char.charisma_mod, 5)

    def test_update_character_stat_no_points(self):
        # Create a character with 0 available points
        char = Character.objects.create(
            user=self.user,
            name="No Points Character",
            strength=10,
            dexterity=10,
            constitution=10,
            intelligence=10,
            wisdom=10,
            charisma=10,
            available_stat_points=0
        )

        # Login
        self.client = Client()
        self.client.login(username='modeltestuser', password='password123')

        # Try to increase strength
        import json
        response = self.client.post(f'/character/{char.pk}/update_stat/',
                                    data=json.dumps({'stat': 'strength', 'action': 'increase'}),
                                    content_type='application/json')

        # Check response
        self.assertEqual(response.status_code, 400)

        # Check JSON content
        response_data = json.loads(response.content)
        self.assertFalse(response_data.get('success'))
        self.assertEqual(response_data.get('error'), 'Keine verfügbaren Attributspunkte vorhanden.')

        # Check stat did not increase
        char.refresh_from_db()
        self.assertEqual(char.strength, 10)
        self.assertEqual(char.available_stat_points, 0)
