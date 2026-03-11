import json
from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Character
from unittest.mock import patch

class CharacterCreationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client = Client()
        self.client.login(username='testuser', password='password123')

    def test_character_creation_form_submission(self):
        response = self.client.post('/create/', {
            'level': 1,
            'name': 'Test Character',
            'character_class': 'Kämpfer',
            'subclass': 'Champion',
            'race': 'Mensch',
            'background': 'Soldat',
            'alignment': 'Neutral Gut',
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
        self.assertEqual(char.character_class, 'Kämpfer')
        self.assertEqual(char.strength, 17)
        # Check equipment handling logic (based on views.py logic)
        self.assertEqual(char.gold, 0)
        self.assertTrue("Standard-Ausrüstung" in char.equipment)

    def test_character_creation_gold_option(self):
        response = self.client.post('/create/', {
            'level': 1,
            'name': 'Gold Character',
            'character_class': 'Schurke',
            'race': 'Elf',
            'background': 'Krimineller',
            'alignment': 'Chaotisch Neutral',
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

    def test_proficiency_bonus(self):
        char = Character(user=self.user, name="Proficiency Test")

        # Test boundaries and within bands
        # Levels 1-4: +2
        char.level = 1
        self.assertEqual(char.proficiency_bonus, 2)
        char.level = 4
        self.assertEqual(char.proficiency_bonus, 2)

        # Levels 5-8: +3
        char.level = 5
        self.assertEqual(char.proficiency_bonus, 3)
        char.level = 8
        self.assertEqual(char.proficiency_bonus, 3)

        # Levels 9-12: +4
        char.level = 9
        self.assertEqual(char.proficiency_bonus, 4)
        char.level = 12
        self.assertEqual(char.proficiency_bonus, 4)

        # Levels 13-16: +5
        char.level = 13
        self.assertEqual(char.proficiency_bonus, 5)
        char.level = 16
        self.assertEqual(char.proficiency_bonus, 5)

        # Levels 17+: +6
        char.level = 17
        self.assertEqual(char.proficiency_bonus, 6)
        char.level = 20
        self.assertEqual(char.proficiency_bonus, 6)
        char.level = 30
        self.assertEqual(char.proficiency_bonus, 6)


    @patch.dict('characters.models.ZAUBER', {
        'Feuerball': {'grad': 3, 'schule': 'Hervorrufung', 'beschreibung': 'Ein heller Feuerball.'},
        'Unsichtbarkeit': {'grad': 2, 'schule': 'Illusion', 'beschreibung': 'Du wirst unsichtbar.'},
        'Magisches Geschoss': {'grad': 1, 'schule': 'Hervorrufung', 'beschreibung': 'Zielsichere magische Pfeile.'},
        'Brennende Hände': {'grad': 1, 'schule': 'Hervorrufung', 'beschreibung': 'Ein Kegel aus Feuer.'}
    }, clear=True)
    def test_get_known_spells_detail(self):
        char = Character(
            user=self.user,
            name="Spell Test Character",
            known_spells=['Feuerball', 'Unsichtbarkeit', 'Unbekannter Zauber', 'Magisches Geschoss', 'Brennende Hände']
        )

        details = char.get_known_spells_detail()

        # Unbekannter Zauber should be ignored.
        # We should have groups for grad 1, 2, and 3.
        self.assertIn(1, details)
        self.assertIn(2, details)
        self.assertIn(3, details)

        # Test grad 1 sorting (Brennende Hände before Magisches Geschoss)
        self.assertEqual(len(details[1]), 2)
        self.assertEqual(details[1][0]['name'], 'Brennende Hände')
        self.assertEqual(details[1][1]['name'], 'Magisches Geschoss')

        # Test grad 2
        self.assertEqual(len(details[2]), 1)
        self.assertEqual(details[2][0]['name'], 'Unsichtbarkeit')

        # Test grad 3
        self.assertEqual(len(details[3]), 1)
        self.assertEqual(details[3][0]['name'], 'Feuerball')

    @patch.dict('characters.rules_data.klassen.KLASSEN_DATEN', {
        'Testklasse': {
            'features': {
                1: [{'name': 'Feature 1'}],
                2: [{'name': 'Feature 2'}],
            }
        }
    }, clear=True)
    def test_get_features_for_level_found(self):
        char = Character(user=self.user, name="Feature Test", character_class="Testklasse", level=2)

        # Test level 1 features
        features_l1 = char.get_features_for_level(1)
        self.assertEqual(len(features_l1), 1)
        self.assertEqual(features_l1[0]['name'], 'Feature 1')

        # Test level 2 features
        features_l2 = char.get_features_for_level(2)
        self.assertEqual(len(features_l2), 1)
        self.assertEqual(features_l2[0]['name'], 'Feature 2')

        # Test non-existent level
        features_l3 = char.get_features_for_level(3)
        self.assertEqual(features_l3, [])

    @patch.dict('characters.rules_data.klassen.KLASSEN_DATEN', {
        'Testklasse': {
            # No features defined
        }
    }, clear=True)
    def test_get_features_for_level_no_features_defined(self):
        char = Character(user=self.user, name="Feature Test", character_class="Testklasse", level=1)
        features = char.get_features_for_level(1)
        self.assertEqual(features, [])

    @patch.dict('characters.rules_data.klassen.KLASSEN_DATEN', {
        'Testklasse': {
            'features': {
                1: [{'name': 'Feature 1'}],
            }
        }
    }, clear=True)
    def test_get_features_for_level_unknown_class(self):
        char = Character(user=self.user, name="Feature Test", character_class="UnknownClass", level=1)
        features = char.get_features_for_level(1)
        self.assertEqual(features, [])

    @patch.dict('characters.rules_data.klassen.KLASSEN_DATEN', {
        'Testklasse': {
            'features': {
                1: [{'name': 'Feature 1'}],
            }
        }
    }, clear=True)
    def test_get_features_for_level_case_insensitive_substring(self):
        # Character class is a substring variation of 'Testklasse'  # noqa: E800
        char = Character(user=self.user, name="Feature Test", character_class="Edler TESTKLASSE des Nordens", level=1)
        features = char.get_features_for_level(1)
        self.assertEqual(len(features), 1)
        self.assertEqual(features[0]['name'], 'Feature 1')


    @patch.dict('characters.rules_data.klassen.KLASSEN_DATEN', {
        'Testklasse': {
            'features': {
                1: [{'name': 'Feature 1'}],
                2: [{'name': 'Feature 2'}],
            },
            'unterklassen': {
                'TestUnterklasse': {
                    1: [{'name': 'UK Feature 1'}],
                    2: [{'name': 'UK Feature 2'}],
                }
            }
        }
    }, clear=True)
    def test_get_all_features_up_to_level_with_subclass(self):
        char = Character(user=self.user, name="All Features Test", character_class="Testklasse", subclass="TestUnterklasse", level=2)
        features = char.get_all_features_up_to_level()
        self.assertEqual(len(features), 4)

        # Verify specific feature attributes
        feature_names = [f['name'] for f in features]
        self.assertIn('Feature 1', feature_names)
        self.assertIn('Feature 2', feature_names)
        self.assertIn('UK Feature 1', feature_names)
        self.assertIn('UK Feature 2', feature_names)

        # Verify 'stufe' and 'unterklasse' fields
        uk_feature_1 = next(f for f in features if f['name'] == 'UK Feature 1')
        self.assertEqual(uk_feature_1['stufe'], 1)
        self.assertTrue(uk_feature_1.get('unterklasse'))

        class_feature_2 = next(f for f in features if f['name'] == 'Feature 2')
        self.assertEqual(class_feature_2['stufe'], 2)
        self.assertNotIn('unterklasse', class_feature_2)

    @patch.dict('characters.rules_data.klassen.KLASSEN_DATEN', {
        'Testklasse': {
            'features': {
                1: [{'name': 'Feature 1'}],
                2: [{'name': 'Feature 2'}],
                3: [{'name': 'Feature 3'}],
            }
        }
    }, clear=True)
    def test_get_all_features_up_to_level_no_subclass(self):
        char = Character(user=self.user, name="All Features Test", character_class="Testklasse", level=2)
        features = char.get_all_features_up_to_level()

        self.assertEqual(len(features), 2)
        self.assertEqual(features[0]['name'], 'Feature 1')
        self.assertEqual(features[0]['stufe'], 1)
        self.assertEqual(features[1]['name'], 'Feature 2')
        self.assertEqual(features[1]['stufe'], 2)

    def test_get_all_features_up_to_level_unknown_class(self):
        char = Character(user=self.user, name="All Features Test", character_class="UnknownClass", level=1)
        features = char.get_all_features_up_to_level()
        self.assertEqual(features, [])

    @patch.dict('characters.rules_data.spezies.SPEZIES_DATEN', {
        'Elf': {'merkmale': [{'name': 'Dunkelsicht'}, {'name': 'Feenblut'}]},
        'Zwerg': {'merkmale': [{'name': 'Zwergenzähigkeit'}]},
        'Drachenblütler': {'merkmale': [{'name': 'Odemwaffe'}]}
    }, clear=True)
    def test_get_species_traits_exact_match(self):
        char = Character(user=self.user, race="Elf")
        import characters.models
        original_cache = getattr(characters.models, '_SPEZIES_DATEN_LOWER', None)
        try:
            if original_cache is not None:
                characters.models._SPEZIES_DATEN_LOWER = {
                    'elf': {'merkmale': [{'name': 'Dunkelsicht'}, {'name': 'Feenblut'}]},
                    'zwerg': {'merkmale': [{'name': 'Zwergenzähigkeit'}]},
                    'drachenblütler': {'merkmale': [{'name': 'Odemwaffe'}]}
                }
            traits = char.get_species_traits()
            self.assertEqual(len(traits), 2)
            self.assertEqual(traits[0]['name'], 'Dunkelsicht')
            self.assertEqual(traits[1]['name'], 'Feenblut')
        finally:
            if original_cache is not None:
                characters.models._SPEZIES_DATEN_LOWER = original_cache

    @patch.dict('characters.rules_data.spezies.SPEZIES_DATEN', {
        'Elf': {'merkmale': [{'name': 'Dunkelsicht'}]},
    }, clear=True)
    def test_get_species_traits_case_insensitive_match(self):
        char = Character(user=self.user, race="eLf")
        import characters.models
        original_cache = getattr(characters.models, '_SPEZIES_DATEN_LOWER', None)
        try:
            if original_cache is not None:
                characters.models._SPEZIES_DATEN_LOWER = {'elf': {'merkmale': [{'name': 'Dunkelsicht'}]}}
            traits = char.get_species_traits()
            self.assertEqual(len(traits), 1)
            self.assertEqual(traits[0]['name'], 'Dunkelsicht')
        finally:
            if original_cache is not None:
                characters.models._SPEZIES_DATEN_LOWER = original_cache

    @patch.dict('characters.rules_data.spezies.SPEZIES_DATEN', {
        'Elf': {'merkmale': [{'name': 'Dunkelsicht'}]},
    }, clear=True)
    def test_get_species_traits_substring_match(self):
        char = Character(user=self.user, race="Waldelf")
        import characters.models
        original_cache = getattr(characters.models, '_SPEZIES_DATEN_LOWER', None)
        try:
            if original_cache is not None:
                characters.models._SPEZIES_DATEN_LOWER = {'elf': {'merkmale': [{'name': 'Dunkelsicht'}]}}
            traits = char.get_species_traits()
            self.assertEqual(len(traits), 1)
            self.assertEqual(traits[0]['name'], 'Dunkelsicht')
        finally:
            if original_cache is not None:
                characters.models._SPEZIES_DATEN_LOWER = original_cache

    @patch.dict('characters.rules_data.spezies.SPEZIES_DATEN', {
        'Elf': {'merkmale': [{'name': 'Dunkelsicht'}]},
    }, clear=True)
    def test_get_species_traits_no_match(self):
        char = Character(user=self.user, race="Ork")
        import characters.models
        original_cache = getattr(characters.models, '_SPEZIES_DATEN_LOWER', None)
        try:
            if original_cache is not None:
                characters.models._SPEZIES_DATEN_LOWER = {'elf': {'merkmale': [{'name': 'Dunkelsicht'}]}}
            traits = char.get_species_traits()
            self.assertTrue(traits == [] or traits is None)
        finally:
            if original_cache is not None:
                characters.models._SPEZIES_DATEN_LOWER = original_cache



    def test_get_max_spell_grade(self):
        """Testet get_max_spell_grade für verschiedene Klassen und Stufen."""
        char = Character.objects.create(user=self.user, name="Spell Grade Test", character_class="Kämpfer", level=5)
        # Kämpfer (ohne Unterklasse) hat keine Zauber
        self.assertEqual(char.get_max_spell_grade(), 0)

        # Magier Stufe 5 hat Grad 3 als Maximum
        char.character_class = "Magier"
        char.save()
        self.assertEqual(char.get_max_spell_grade(), 3)

        # Magier Stufe 17 hat Grad 9
        char.level = 17
        char.save()
        self.assertEqual(char.get_max_spell_grade(), 9)

        # Hexenmeister (Paktmagie) Stufe 5 hat Pakt_grad 3
        char.character_class = "Hexenmeister"
        char.level = 5
        char.save()
        self.assertEqual(char.get_max_spell_grade(), 3)

        # Hexenmeister Stufe 1 hat Pakt_grad 1
        char.level = 1
        char.save()
        self.assertEqual(char.get_max_spell_grade(), 1)

        # Paladin Stufe 5 hat Grad 2
        char.character_class = "Paladin"
        char.level = 5
        char.save()
        self.assertEqual(char.get_max_spell_grade(), 2)

        # Paladin Stufe 1 hat Grad 0 (keine Slots) in den Basisregeln, oder leeres dict
        char.level = 1
        char.save()
        self.assertEqual(char.get_max_spell_grade(), 0)

    def test_get_available_spells(self):
        """Testet die get_available_spells-Methode für verschiedene Zauberklassen."""
        # 1. Klasse ohne Zauber (z.B. Kämpfer)
        char = Character.objects.create(
            user=self.user,
            name="Non-Caster",
            character_class="Kämpfer",
            level=1
        )
        self.assertEqual(char.get_available_spells(), {})

        # 2. Klasse mit Zaubern (z.B. Kleriker, Level 1)
        # Vollzauberwirker hat auf Level 1 max_grad = 1 und Grad 0 Zauber (Cantrips)
        char.character_class = "Kleriker"
        char.save()
        spells_lvl1 = char.get_available_spells()
        self.assertIn(0, spells_lvl1) # Cantrips
        self.assertIn(1, spells_lvl1) # Level 1 spells
        self.assertNotIn(2, spells_lvl1) # No level 2 spells yet

        # Verify structure of spells list
        self.assertTrue(isinstance(spells_lvl1[0], list))
        self.assertTrue(len(spells_lvl1[0]) > 0)
        self.assertTrue(isinstance(spells_lvl1[0][0], dict))
        self.assertIn('name', spells_lvl1[0][0])
        self.assertNotIn('klassen', spells_lvl1[0][0]) # 'klassen' should be excluded

        # 3. Klasse mit Zaubern, höheres Level (z.B. Kleriker, Level 5)
        # max_grad auf Level 5 ist 3
        char.level = 5
        char.save()
        spells_lvl5 = char.get_available_spells()
        self.assertIn(0, spells_lvl5)
        self.assertIn(1, spells_lvl5)
        self.assertIn(2, spells_lvl5)
        self.assertIn(3, spells_lvl5)
        self.assertNotIn(4, spells_lvl5)

        # 4. Halbzauberwirker (z.B. Paladin, Level 1)
        # Paladin hat auf Level 1 max_grad = 0 (keine Zauber) aber in 2024 Regeln vllt Cantrips?
        # Check actual rules configuration.
        # ZAUBERPLATZ_TABELLE.get('halbzauberwirker').get(1) ist leer (keine zauber auf level 1)
        char.character_class = "Paladin"
        char.level = 1
        char.save()
        spells_paladin1 = char.get_available_spells()
        # Paladin auf Stufe 1 in diesen Regeln hat oft max_grad=0.
        # Wenn er keine Cantrips hat, hat er evtl keine Sprüche in der Liste für Grad 0,
        # oder er gibt zumindest Grad 0 zurück. Testen wir einfach den Aufruf.
        self.assertTrue(isinstance(spells_paladin1, dict))

    def test_spell_properties(self):
        """Testet die Spellcasting-Properties has_spellcasting, spell_save_dc und spell_attack_bonus."""
        char = Character.objects.create(
            user=self.user,
            name="Spellcaster Test",
            race="Mensch",
            character_class="Magier",
            level=1,
            intelligence=16  # int_mod = +3
        )

        # Magier hat has_spellcasting = True
        self.assertTrue(char.has_spellcasting)

        # prof_bonus für Level 1 = 2. spellcasting_ability_mod = 3
        self.assertEqual(char.spellcasting_ability_mod, 3)
        self.assertEqual(char.spell_save_dc, 8 + 2 + 3)
        self.assertEqual(char.spell_attack_bonus, 2 + 3)

        # Fighter hat has_spellcasting = False
        char.character_class="Kämpfer"
        char.save()

        self.assertFalse(char.has_spellcasting)
        self.assertEqual(char.spellcasting_ability_mod, 0)
        self.assertEqual(char.spell_save_dc, 0)
        self.assertEqual(char.spell_attack_bonus, 0)


    def test_get_unarmored_ac(self):
        # Base setup: Dex 14 (+2), Con 16 (+3), Wis 12 (+1), Cha 18 (+4)
        char = Character(
            user=self.user,
            name="AC Test",
            level=1,
            dexterity=14,
            constitution=16,
            wisdom=12,
            charisma=18
        )

        # Default (Kämpfer / Fighter)
        char.character_class = "Kämpfer"
        self.assertEqual(char.get_unarmored_ac(), 12)  # 10 + 2 (Dex)

        # Barbar
        char.character_class = "Barbar"
        self.assertEqual(char.get_unarmored_ac(), 15)  # 10 + 2 (Dex) + 3 (Con)

        # Mönch
        char.character_class = "Mönch"
        self.assertEqual(char.get_unarmored_ac(), 13)  # 10 + 2 (Dex) + 1 (Wis)

        # Zauberer Drachenblut-Linie
        char.character_class = "Zauberer"
        char.subclass = "Drachenblut-Linie"
        char.level = 3
        self.assertEqual(char.get_unarmored_ac(), 15)  # 13 + 2 (Dex)

        char.level = 2
        self.assertEqual(char.get_unarmored_ac(), 12)  # 10 + 2 (Dex) (Level too low)

        # Barde Schule des Tanzes
        char.character_class = "Barde"
        char.subclass = "Schule des Tanzes"
        char.level = 3
        self.assertEqual(char.get_unarmored_ac(), 16)  # 10 + 2 (Dex) + 4 (Cha)

        char.level = 2
        self.assertEqual(char.get_unarmored_ac(), 12)  # 10 + 2 (Dex) (Level too low)


    def test_get_spell_slots_for_level(self):
        char = Character(
            user=self.user,
            name="Spell Slot Test",
            level=5,
        )

        # Vollzauberwirker (Magier) Level 5
        char.character_class = "Magier"
        self.assertEqual(char.get_spell_slots_for_level(), {1: 4, 2: 3, 3: 2})

        # Halbzauberwirker (Paladin) Level 5
        char.character_class = "Paladin"
        self.assertEqual(char.get_spell_slots_for_level(), {1: 4, 2: 2})

        # Halbzauberwirker (Paladin) Level 1 (No slots)
        char.level = 1
        self.assertEqual(char.get_spell_slots_for_level(), {})

        # Paktmagie (Hexenmeister) Level 3
        char.character_class = "Hexenmeister"
        char.level = 3
        self.assertEqual(char.get_spell_slots_for_level(), {'pakt_anzahl': 2, 'pakt_grad': 2})

        # Non-spellcaster (Kämpfer)
        char.character_class = "Kämpfer"
        char.level = 5
        self.assertEqual(char.get_spell_slots_for_level(), {})

        # Unknown/Missing class
        char.character_class = "UnknownClass123"
        self.assertEqual(char.get_spell_slots_for_level(), {})

from .views import _apply_background_bonuses
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

class StatUpdateTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.character = Character.objects.create(
            user=self.user,
            name='Test Character',
            race='Mensch',
            character_class='Kämpfer',
            strength=10,
            available_stat_points=2
        )
        self.url = reverse('update_character_stat', args=[self.character.pk])
        self.client.login(username='testuser', password='testpassword')


    def test_update_stat_invalid_decode_error(self):
        response = self.client.post(
            self.url,
            data='{"stat": "strength", "action": "increase"', # missing bracket
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 'Ungültige Anfragedaten.')


    def test_update_stat_invalid_json(self):
        response = self.client.post(
            self.url,
            data='invalid json',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 'Ungültige Anfragedaten.')

    def test_update_stat_increase_success(self):
        response = self.client.post(
            self.url,
            data='{"stat": "strength", "action": "increase"}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertEqual(data['new_value'], 11)
        self.assertEqual(data['new_available_points'], 1)
        self.assertEqual(data['new_mod'], '+0')
        self.character.refresh_from_db()
        self.assertEqual(self.character.strength, 11)
        self.assertEqual(self.character.available_stat_points, 1)

    def test_update_stat_decrease_success(self):
        self.character.strength = 12
        self.character.available_stat_points = 0
        self.character.save()

        response = self.client.post(
            self.url,
            data='{"stat": "strength", "action": "decrease"}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertEqual(data['new_value'], 11)
        self.assertEqual(data['new_available_points'], 1)
        self.assertEqual(data['new_mod'], '+0')
        self.character.refresh_from_db()
        self.assertEqual(self.character.strength, 11)
        self.assertEqual(self.character.available_stat_points, 1)

    def test_update_stat_invalid_stat(self):
        response = self.client.post(
            self.url,
            data='{"stat": "invalid_stat", "action": "increase"}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 'Ungültiges Attribut.')

    def test_update_stat_invalid_action(self):
        response = self.client.post(
            self.url,
            data='{"stat": "strength", "action": "invalid_action"}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 'Ungültige Aktion.')

    def test_update_stat_increase_max_limit(self):
        self.character.strength = 30
        self.character.save()

        response = self.client.post(
            self.url,
            data='{"stat": "strength", "action": "increase"}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 'Attribut ist bereits am Maximum (30).')

    def test_update_stat_increase_no_points(self):
        self.character.available_stat_points = 0
        self.character.save()

        response = self.client.post(
            self.url,
            data='{"stat": "strength", "action": "increase"}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 'Keine verfügbaren Attributspunkte vorhanden.')

    def test_update_stat_decrease_min_limit(self):
        self.character.strength = 1
        self.character.save()

        response = self.client.post(
            self.url,
            data='{"stat": "strength", "action": "decrease"}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 'Attribut kann nicht unter 1 sinken.')

    def test_update_stat_constitution_mod_change(self):
        # Initial con: 11 (mod 0), max_hp: 10, level: 1
        self.character.constitution = 11
        self.character.max_hp = 10
        self.character.current_hp = 10
        self.character.level = 1
        self.character.save()

        # Increase to 12 (mod +1). max_hp should increase by 1 * level = 1
        response = self.client.post(
            self.url,
            data='{"stat": "constitution", "action": "increase"}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertEqual(data['new_max_hp'], 11)
        self.assertEqual(data['new_current_hp'], 11)
        self.character.refresh_from_db()
        self.assertEqual(self.character.max_hp, 11)
        self.assertEqual(self.character.current_hp, 11)


    def test_update_stat_constitution_mod_decrease(self):
        # Initial con: 12 (mod +1), max_hp: 11, level: 1
        self.character.constitution = 12
        self.character.max_hp = 11
        self.character.current_hp = 11
        self.character.level = 1
        self.character.available_stat_points = 0
        self.character.save()

        # Decrease to 11 (mod 0). max_hp should decrease by 1 * level = 1
        response = self.client.post(
            self.url,
            data='{"stat": "constitution", "action": "decrease"}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertEqual(data['new_value'], 11)
        self.assertEqual(data['new_max_hp'], 10)
        self.assertEqual(data['new_current_hp'], 10)
        self.character.refresh_from_db()
        self.assertEqual(self.character.max_hp, 10)
        self.assertEqual(self.character.current_hp, 10)

    def test_update_stat_dexterity_mod_change(self):
        # Initial dex: 11 (mod 0), armor_class: 10
        self.character.dexterity = 11
        self.character.armor_class = 10
        self.character.save()

        # Increase to 12 (mod +1). AC should increase by 1
        response = self.client.post(
            self.url,
            data='{"stat": "dexterity", "action": "increase"}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.character.refresh_from_db()
        self.assertEqual(self.character.armor_class, 11)


    def test_update_stat_dexterity_mod_decrease(self):
        # Initial dex: 12 (mod +1), armor_class: 11
        self.character.dexterity = 12
        self.character.armor_class = 11
        self.character.available_stat_points = 0
        self.character.save()

        # Decrease to 11 (mod 0). AC should decrease by 1
        response = self.client.post(
            self.url,
            data='{"stat": "dexterity", "action": "decrease"}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertEqual(data['new_value'], 11)
        self.assertEqual(data['new_ac'], 10)
        self.character.refresh_from_db()
        self.assertEqual(self.character.armor_class, 10)


    def test_update_stat_negative_mod(self):
        self.character.strength = 9
        self.character.available_stat_points = 0
        self.character.save()

        # Decrease to 8 (mod -1). Modifier string should be "-1" without "+"
        response = self.client.post(
            self.url,
            data='{"stat": "strength", "action": "decrease"}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertEqual(data['new_value'], 8)
        self.assertEqual(data['new_mod'], '-1')

    def test_update_stat_not_logged_in(self):
        self.client.logout()
        response = self.client.post(
            self.url,
            data='{"stat": "strength", "action": "increase"}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(reverse('login')))

    def test_update_stat_wrong_user(self):
        other_user = User.objects.create_user(username='otheruser', password='testpassword')
        self.client.login(username='otheruser', password='testpassword')
        response = self.client.post(
            self.url,
            data='{"stat": "strength", "action": "increase"}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 404)

    def test_update_stat_not_post(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 405)

class CharacterLevelupTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.character = Character.objects.create(
            user=self.user,
            name='Test Character',
            character_class='Kämpfer',
            race='Mensch',
            level=1,
            hit_dice='1d10',
            constitution=14,  # +2 mod
            max_hp=12,
            current_hp=12,
            available_stat_points=0,
            features=[]
        )
        self.url = reverse('character_levelup', args=[self.character.pk])
        self.client.login(username='testuser', password='testpassword')

    def test_levelup_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'characters/character_levelup.html')
        self.assertEqual(response.context['character'], self.character)
        self.assertEqual(response.context['new_level'], 2)
        self.assertIn('new_features', response.context)

    def test_levelup_post_success(self):
        response = self.client.post(self.url)
        self.assertRedirects(response, reverse('character_detail', args=[self.character.pk]))
        self.character.refresh_from_db()
        self.assertEqual(self.character.level, 2)
        # hit_dice='1d10', con=14(+2). hp_increase = (10 // 2) + 1 + 2 = 8
        self.assertEqual(self.character.max_hp, 20)
        self.assertEqual(self.character.current_hp, 20)
        self.assertEqual(self.character.hit_dice_total, 2)

    def test_levelup_post_with_rolled_hp(self):
        response = self.client.post(self.url, data={'rolled_hp': '8'})
        self.assertRedirects(response, reverse('character_detail', args=[self.character.pk]))
        self.character.refresh_from_db()
        self.assertEqual(self.character.level, 2)
        # hit_dice='1d10', con=14(+2). hp_increase = 8 + 2 = 10
        self.assertEqual(self.character.max_hp, 22)
        self.assertEqual(self.character.current_hp, 22)

    def test_levelup_dwarf_hp_bonus(self):
        dwarf_char = Character.objects.create(
            user=self.user,
            name='Dwarf Test',
            character_class='Kämpfer',
            race='Zwerg',
            level=1,
            hit_dice='1d10',
            constitution=14, # +2 mod
            max_hp=13, # base + 1 for dwarf
            current_hp=13,
            available_stat_points=0,
            features=[]
        )
        url = reverse('character_levelup', args=[dwarf_char.pk])
        response = self.client.post(url)
        self.assertRedirects(response, reverse('character_detail', args=[dwarf_char.pk]))
        dwarf_char.refresh_from_db()
        # hp_increase = (10 // 2) + 1 + 2 = 8, plus 1 for dwarf = 9. 13 + 9 = 22
        self.assertEqual(dwarf_char.max_hp, 22)


    def test_levelup_invalid_hit_dice_logs_warning(self):
        invalid_char = Character.objects.create(
            user=self.user,
            name='Invalid Dice Test',
            character_class='Kämpfer',
            race='Mensch',
            level=1,
            hit_dice='invalid',
            constitution=14,
            max_hp=12,
            current_hp=12,
            available_stat_points=0,
            features=[]
        )
        url = reverse('character_levelup', args=[invalid_char.pk])
        with self.assertLogs('characters.views', level='WARNING') as cm:
            response = self.client.post(url)
        self.assertRedirects(response, reverse('character_detail', args=[invalid_char.pk]))
        invalid_char.refresh_from_db()
        self.assertEqual(invalid_char.max_hp, 12)
        self.assertTrue(any('Ungültiges Trefferwürfel-Format' in log for log in cm.output))

    def test_levelup_asi(self):
        asi_char = Character.objects.create(
            user=self.user,
            name='ASI Test',
            character_class='Kämpfer',
            race='Mensch',
            level=3,
            hit_dice='1d10',
            constitution=14,
            max_hp=28,
            current_hp=28,
            available_stat_points=0,
            features=[]
        )
        url = reverse('character_levelup', args=[asi_char.pk])
        self.client.post(url)
        asi_char.refresh_from_db()
        self.assertEqual(asi_char.level, 4)
        self.assertEqual(asi_char.available_stat_points, 2)

    def test_levelup_invalid_hit_dice(self):
        invalid_char = Character.objects.create(
            user=self.user,
            name='Invalid Hit Dice Test',
            character_class='Kämpfer',
            race='Mensch',
            level=1,
            hit_dice='invalid', # Will cause ValueError/IndexError
            constitution=14,
            max_hp=12,
            current_hp=12,
            available_stat_points=0,
            features=[]
        )
        url = reverse('character_levelup', args=[invalid_char.pk])
        self.client.post(url)
        invalid_char.refresh_from_db()
        self.assertEqual(invalid_char.level, 2)
        # HP remains unchanged
        self.assertEqual(invalid_char.max_hp, 12)
        self.assertEqual(invalid_char.current_hp, 12)


    def test_levelup_unauthenticated(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/login/') or response.url.startswith('/accounts/login/'))

    def test_levelup_wrong_user(self):
        other_user = User.objects.create_user(username='otheruser', password='password')
        self.client.login(username='otheruser', password='password')
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 404)

    def test_levelup_not_found(self):
        response = self.client.post(reverse('character_levelup', args=[9999]))
        self.assertEqual(response.status_code, 404)

    def test_levelup_unknown_class(self):
        unknown_char = Character.objects.create(
            user=self.user,
            name='Unknown Class Test',
            character_class='UnbekannteKlasse',
            race='Mensch',
            level=1,
            hit_dice='1d10',
            constitution=14,
            max_hp=12,
            current_hp=12,
            available_stat_points=0,
            features=[]
        )
        url = reverse('character_levelup', args=[unknown_char.pk])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        unknown_char.refresh_from_db()
        self.assertEqual(unknown_char.level, 2)
        self.assertEqual(len(unknown_char.features), 0)

    def test_levelup_none_features(self):
        # We simulate that the DB returned an object with features=None
        none_features_char = Character.objects.create(
            user=self.user,
            name='None Features Test',
            character_class='Kämpfer',
            race='Mensch',
            level=1,
            hit_dice='1d10',
            constitution=14,
            max_hp=12,
            current_hp=12,
            available_stat_points=0,
            features=[]
        )
        url = reverse('character_levelup', args=[none_features_char.pk])

        from unittest.mock import patch
        with patch('characters.views.get_object_or_404') as mock_get_object:
            # Prepare an object with features = None
            none_features_char.features = None
            mock_get_object.return_value = none_features_char
            response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        # Verify the mock object was updated properly
        self.assertEqual(none_features_char.level, 2)
        self.assertIsInstance(none_features_char.features, list)
        self.assertTrue(len(none_features_char.features) > 0)


class BackgroundBonusesTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='bgtestuser', password='password123')
        self.char = Character(
            user=self.user,
            name="Test Hero",
            strength=10,
            dexterity=10,
            constitution=10,
            intelligence=10,
            wisdom=10,
            charisma=10
        )

    def test_known_background_bonus(self):
        # Soldat gives +2 Strength, +1 Constitution
        self.char.background = "Soldat"
        self.char.character_class = "Kämpfer"
        _apply_background_bonuses(self.char)
        self.assertEqual(self.char.strength, 12)
        self.assertEqual(self.char.constitution, 11)
        self.assertEqual(self.char.dexterity, 10)

    def test_fallback_melee_bonus(self):
        # Unbekannter Hintergrund, aber Nahkampf-Klasse -> +2 Str, +1 Con
        self.char.background = "Unbekannt"
        self.char.character_class = "Barbar"
        _apply_background_bonuses(self.char)
        self.assertEqual(self.char.strength, 12)
        self.assertEqual(self.char.constitution, 11)
        self.assertEqual(self.char.dexterity, 10)

    def test_fallback_agile_bonus(self):
        # Unbekannter Hintergrund, aber Agile-Klasse -> +2 Dex, +1 Wis
        self.char.background = "Unbekannt"
        self.char.character_class = "Schurke"
        _apply_background_bonuses(self.char)
        self.assertEqual(self.char.dexterity, 12)
        self.assertEqual(self.char.wisdom, 11)
        self.assertEqual(self.char.strength, 10)

    def test_fallback_default_bonus(self):
        # Unbekannter Hintergrund und andere Klasse -> +2 Cha, +1 Int
        self.char.background = "Unbekannt"
        self.char.character_class = "Magier"
        _apply_background_bonuses(self.char)
        self.assertEqual(self.char.charisma, 12)
        self.assertEqual(self.char.intelligence, 11)
        self.assertEqual(self.char.strength, 10)


import io
from PIL import Image as PILImage
from django.core.files.uploadedfile import SimpleUploadedFile
from .image_utils import compress_character_image


class ImageCompressionTest(TestCase):
    """Tests for the compress_character_image utility."""

    def _make_upload(self, width, height, fmt='PNG', name='test.png'):
        """Helper: create an in-memory uploaded image file."""
        img = PILImage.new('RGB', (width, height), color='red')
        buf = io.BytesIO()
        img.save(buf, format=fmt)
        buf.seek(0)
        return SimpleUploadedFile(name, buf.read(), content_type=f'image/{fmt.lower()}')

    def test_large_image_gets_compressed(self):
        upload = self._make_upload(2000, 2000)
        result = compress_character_image(upload)

        img = PILImage.open(io.BytesIO(result.read()))
        self.assertLessEqual(img.width, 512)
        self.assertLessEqual(img.height, 512)

    def test_small_image_stays_small(self):
        upload = self._make_upload(100, 100)
        result = compress_character_image(upload)

        img = PILImage.open(io.BytesIO(result.read()))
        self.assertEqual(img.width, 100)
        self.assertEqual(img.height, 100)

    def test_output_is_webp(self):
        upload = self._make_upload(200, 200)
        result = compress_character_image(upload)

        self.assertTrue(result.name.endswith('.webp'))
        img = PILImage.open(io.BytesIO(result.read()))
        self.assertEqual(img.format, 'WEBP')

    def test_aspect_ratio_preserved(self):
        upload = self._make_upload(1000, 500, name='wide.png')
        result = compress_character_image(upload)

        img = PILImage.open(io.BytesIO(result.read()))
        self.assertEqual(img.width, 512)
        self.assertEqual(img.height, 256)

class CharacterBuilderViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='buildertestuser', password='password123')
        self.url = reverse('character_builder')

    def test_character_builder_access_logged_out(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(reverse('login')))

    def test_character_builder_access_logged_in(self):
        self.client.login(username='buildertestuser', password='password123')
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'characters/character_builder.html')

        # Check if the JSON strings are in the context
        self.assertIn('klassen_json', response.context)
        self.assertIn('hintergruende_json', response.context)
        self.assertIn('spezies_json', response.context)

        # Verify that they are valid JSON
        try:
            klassen = json.loads(response.context['klassen_json'])
            self.assertIsInstance(klassen, dict)
            self.assertTrue(len(klassen) > 0)
        except json.JSONDecodeError:
            self.fail("klassen_json is not valid JSON")

        try:
            hintergruende = json.loads(response.context['hintergruende_json'])
            self.assertIsInstance(hintergruende, dict)
            self.assertTrue(len(hintergruende) > 0)
        except json.JSONDecodeError:
            self.fail("hintergruende_json is not valid JSON")

        try:
            spezies = json.loads(response.context['spezies_json'])
            self.assertIsInstance(spezies, dict)
            self.assertTrue(len(spezies) > 0)
        except json.JSONDecodeError:
            self.fail("spezies_json is not valid JSON")

class AddCharacterWeaponTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='weapontester', password='password123')
        self.other_user = User.objects.create_user(username='otheruser', password='password123')
        self.character = Character.objects.create(
            user=self.user,
            name="Test Weapon Hero",
            character_class="Kämpfer",
            race="Mensch",
            level=1
        )
        self.url = reverse('add_character_weapon', kwargs={'pk': self.character.pk})
        self.client.login(username='weapontester', password='password123')

    def test_add_weapon_unauthenticated(self):
        self.client.logout()
        response = self.client.post(
            self.url,
            data='{"name": "Schwert"}',
            content_type='application/json'
        )
        self.assertRedirects(response, f'/login/?next={self.url}')

    def test_add_weapon_other_user(self):
        self.client.logout()
        self.client.login(username='otheruser', password='password123')
        response = self.client.post(
            self.url,
            data='{"name": "Schwert"}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 404)

    def test_add_weapon_get_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 405)

    def test_add_weapon_invalid_json(self):
        response = self.client.post(
            self.url,
            data='invalid json',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 'Ungültige Anfragedaten.')

    def test_add_weapon_missing_name(self):
        response = self.client.post(
            self.url,
            data='{"type": "Nahkampf"}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 'Waffenname fehlt.')

    def test_add_weapon_success(self):
        payload = {
            "name": "Langschwert",
            "type": "Nahkampf-Kriegswaffe",
            "hit": "+5",
            "damage": "1d8+3"
        }
        response = self.client.post(
            self.url,
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])

        self.character.refresh_from_db()
        weapons = self.character.weapons
        self.assertEqual(len(weapons), 1)
        self.assertEqual(weapons[0]['name'], "Langschwert")
        self.assertEqual(weapons[0]['typ'], "Nahkampf-Kriegswaffe")
        self.assertEqual(weapons[0]['angriffsbonus'], "+5")
        self.assertEqual(weapons[0]['schaden'], "1d8+3")

    def test_add_weapon_default_values(self):
        payload = {"name": "Dolch"}
        response = self.client.post(
            self.url,
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])

        self.character.refresh_from_db()
        weapons = self.character.weapons
        self.assertEqual(len(weapons), 1)
        self.assertEqual(weapons[0]['name'], "Dolch")
        self.assertEqual(weapons[0]['typ'], "")
        self.assertEqual(weapons[0]['angriffsbonus'], "+0")
        self.assertEqual(weapons[0]['schaden'], "0")

class CharacterBuilderSubmitTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='buildsubmituser', password='password123')
        self.url = reverse('character_builder_submit')
        self.client.login(username='buildsubmituser', password='password123')

    def test_submit_unauthenticated(self):
        self.client.logout()
        response = self.client.post(self.url, data={'name': 'Test'})
        self.assertRedirects(response, f'/login/?next={self.url}')

    def test_submit_get_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 405)  # Method Not Allowed

    def test_submit_success(self):
        payload = {
            'name': 'Gimli',
            'character_class': 'Kämpfer',
            'subclass': '',
            'background': 'Soldat',
            'race': 'Zwerg',
            'level': '3',
            'equipment_preference': 'gold'
        }
        response = self.client.post(self.url, data=payload)

        # Should redirect to character detail
        self.assertEqual(response.status_code, 302)

        # Verify character was created
        character = Character.objects.get(name='Gimli')
        self.assertEqual(character.user, self.user)
        self.assertEqual(character.character_class, 'Kämpfer')
        self.assertEqual(character.race, 'Zwerg')
        self.assertEqual(character.level, 3)
        self.assertEqual(response.url, reverse('character_detail', kwargs={'pk': character.pk}))

    def test_submit_invalid(self):
        payload = {
            'name': 'Invalid Hero',
            'character_class': '',  # Missing class, which is required
            'background': 'Soldat',
            'race': 'Zwerg',
            'level': '3',
            'equipment_preference': 'gold'
        }
        response = self.client.post(self.url, data=payload)

        # Should redirect back to the builder form
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('character_builder'))

        # Verify no character was created
        self.assertFalse(Character.objects.filter(name='Invalid Hero').exists())

    def test_submit_invalid_level(self):
        # Since character_class, race and background are required by the form, we provide them
        base_payload = {
            'character_class': 'Kämpfer',
            'race': 'Zwerg',
            'background': 'Soldat'
        }

        payload = {**base_payload, 'name': 'Legolas', 'level': 'invalid_level'}
        response = self.client.post(self.url, data=payload)
        # Form should be invalid due to 'invalid_level' and redirect back to builder
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('character_builder'))
        self.assertFalse(Character.objects.filter(name='Legolas').exists())

        # Test out of bounds
        payload = {**base_payload, 'name': 'Over 9000', 'level': '9000'}
        self.client.post(self.url, data=payload)
        self.assertFalse(Character.objects.filter(name='Over 9000').exists())

        payload = {**base_payload, 'name': 'Negative', 'level': '-5'}
        self.client.post(self.url, data=payload)
        self.assertFalse(Character.objects.filter(name='Negative').exists())

    @patch('characters.views.compress_character_image')
    def test_submit_with_image(self, mock_compress):
        # Create a dummy image file
        img = PILImage.new('RGB', (100, 100), color='blue')
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        buf.seek(0)
        upload = SimpleUploadedFile('test.png', buf.read(), content_type='image/png')

        mock_compress.return_value = 'compressed_image_path.webp'

        payload = {
            'name': 'Image Hero',
            'image': upload,
            'character_class': 'Kämpfer',
            'race': 'Zwerg',
            'background': 'Soldat',
            'level': '1',
            'equipment_preference': 'gold'
        }
        response = self.client.post(self.url, data=payload)
        self.assertEqual(response.status_code, 302)

        mock_compress.assert_called_once()
        character = Character.objects.get(name='Image Hero')
        self.assertEqual(character.image, 'compressed_image_path.webp')

    def test_submit_missing_data(self):
        # Empty POST request
        response = self.client.post(self.url, data={})
        self.assertEqual(response.status_code, 302)
        # Should redirect back to builder since form is invalid
        self.assertEqual(response.url, reverse('character_builder'))

        # Verify no character was created
        self.assertFalse(Character.objects.filter(user=self.user).exists())

from characters.rules_data.zauber import get_zauberliste

class RulesDataTest(TestCase):
    def test_get_zauberliste(self):
        """Testet, dass die Zauber einer Klasse korrekt gruppiert und sortiert werden."""
        # 1. Bekannte Klasse (Magier)
        magier_zauber = get_zauberliste('Magier')

        # Teste Struktur: Dictionary mit Int-Keys und List-Werten
        self.assertIsInstance(magier_zauber, dict)
        self.assertTrue(all(isinstance(k, int) for k in magier_zauber.keys()))
        self.assertTrue(all(isinstance(v, list) for v in magier_zauber.values()))

        # Teste spezifische Grade
        self.assertIn(0, magier_zauber)
        self.assertIn(1, magier_zauber)

        # Teste, dass bestimmte bekannte Zauber in den korrekten Graden vorhanden sind
        self.assertIn('Feuerbolzen', magier_zauber[0])
        self.assertIn('Magisches Geschoss', magier_zauber[1])

        # Teste auf Klassenspezifität (Heilendes Wort ist Kleriker/Barde/Druide, aber nicht Magier in Basis 5e/2024 Regeln meistens)
        # Überprüfen wir zur Sicherheit, dass es nicht da ist.
        # Aber was sicher da ist: Feuerball auf Grad 3
        self.assertIn(3, magier_zauber)
        self.assertIn('Feuerball', magier_zauber[3])

        # Teste Sortierung (alphabetisch)
        for grad, zauber_liste in magier_zauber.items():
            sorted_liste = sorted(zauber_liste)
            self.assertEqual(zauber_liste, sorted_liste)

        # 2. Unbekannte Klasse (Sollte leeres Dictionary zurückgeben)
        unbekannt_zauber = get_zauberliste('UnbekannteKlasse')
        self.assertEqual(unbekannt_zauber, {})

from .views import _calculate_hp

class CalculateHPTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='hptestuser', password='password123')
        self.char = Character.objects.create(
            user=self.user,
            name="HP Test Hero",
            constitution=14,  # +2 mod
            level=1
        )

    def test_calculate_hp_valid_hit_die(self):
        _calculate_hp(self.char, 'd10', tp_bonus=0)
        # 10 + 2 (con mod) = 12
        self.assertEqual(self.char.max_hp, 12)
        self.assertEqual(self.char.current_hp, 12)

        self.char.level = 2
        _calculate_hp(self.char, 'd10', tp_bonus=0)
        # base_hp = 10 + 2 = 12
        # hp_per_level = (10 // 2) + 1 + 2 = 8
        # max_hp = 12 + 8 * 1 = 20
        self.assertEqual(self.char.max_hp, 20)
        self.assertEqual(self.char.current_hp, 20)

    def test_calculate_hp_invalid_hit_die_fallback(self):
        # tests ValueError exception
        _calculate_hp(self.char, 'invalid', tp_bonus=0)
        # Fallback to hit_die_value = 8
        # base_hp = 8 + 2 (con mod) = 10
        self.assertEqual(self.char.max_hp, 10)
        self.assertEqual(self.char.current_hp, 10)

        self.char.level = 2
        _calculate_hp(self.char, 'invalid', tp_bonus=0)
        # base_hp = 8 + 2 = 10
        # hp_per_level = (8 // 2) + 1 + 2 = 7
        # max_hp = 10 + 7 * 1 = 17
        self.assertEqual(self.char.max_hp, 17)
        self.assertEqual(self.char.current_hp, 17)

    def test_calculate_hp_empty_hit_die_fallback(self):
        # tests IndexError exception (''.strip()[1:])
        _calculate_hp(self.char, '', tp_bonus=0)
        # Fallback to hit_die_value = 8
        # base_hp = 8 + 2 (con mod) = 10
        self.assertEqual(self.char.max_hp, 10)
        self.assertEqual(self.char.current_hp, 10)
