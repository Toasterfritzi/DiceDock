import json
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
            'level': 1,
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
            'level': 1,
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
        self.assertIn("Die Passwörter stimmen nicht überein!", form.non_field_errors())

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

from django.urls import reverse

class DashboardViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='dashboarduser', password='password123')
        self.other_user = User.objects.create_user(username='otheruser', password='password123')

        self.char1 = Character.objects.create(
            user=self.user,
            name="Hero One",
            character_class="Warrior",
            race="Human",
            level=1,
            strength=15, dexterity=12, constitution=14, intelligence=10, wisdom=10, charisma=12
        )
        self.char2 = Character.objects.create(
            user=self.user,
            name="Hero Two",
            character_class="Mage",
            race="Elf",
            level=2,
            strength=8, dexterity=14, constitution=12, intelligence=16, wisdom=10, charisma=10
        )

        self.other_char = Character.objects.create(
            user=self.other_user,
            name="Villain One",
            character_class="Rogue",
            race="Goblin",
            level=3,
            strength=10, dexterity=16, constitution=12, intelligence=10, wisdom=8, charisma=14
        )

    def test_dashboard_access_logged_in(self):
        self.client.login(username='dashboarduser', password='password123')
        response = self.client.get(reverse('dashboard'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'characters/dashboard.html')

        # Verify characters in context
        characters_in_context = list(response.context['characters'])
        self.assertEqual(len(characters_in_context), 2)
        self.assertIn(self.char1, characters_in_context)
        self.assertIn(self.char2, characters_in_context)
        self.assertNotIn(self.other_char, characters_in_context)

    def test_dashboard_access_logged_out(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(reverse('login')))

class CoinUpdateTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.character = Character.objects.create(
            user=self.user,
            name='Test Character',
            race='Mensch',
            character_class='Kämpfer',
            gold=10,
            silver=5,
            copper=0
        )
        self.url = reverse('update_character_coin', args=[self.character.pk])
        self.client.login(username='testuser', password='testpassword')

    def test_increase_coin(self):
        response = self.client.post(
            self.url,
            data=json.dumps({'coin': 'gold', 'action': 'increase'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertEqual(data['new_value'], 11)
        self.character.refresh_from_db()
        self.assertEqual(self.character.gold, 11)

    def test_decrease_coin(self):
        response = self.client.post(
            self.url,
            data=json.dumps({'coin': 'silver', 'action': 'decrease'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertEqual(data['new_value'], 4)
        self.character.refresh_from_db()
        self.assertEqual(self.character.silver, 4)

    def test_decrease_coin_below_zero(self):
        response = self.client.post(
            self.url,
            data=json.dumps({'coin': 'copper', 'action': 'decrease'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 'Münzanzahl kann nicht unter 0 sinken.')
        self.character.refresh_from_db()
        self.assertEqual(self.character.copper, 0)
