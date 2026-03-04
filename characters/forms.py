from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from .models import Character

from characters.rules_data.klassen import KLASSEN_DATEN
from characters.rules_data.hintergruende import HINTERGRUND_DATEN
from characters.rules_data.spezies import SPEZIES_DATEN

ALIGNMENT_CHOICES = [
    ('', '--- Wähle eine Gesinnung ---'),
    ('Rechtschaffen Gut', 'Rechtschaffen Gut'),
    ('Neutral Gut', 'Neutral Gut'),
    ('Chaotisch Gut', 'Chaotisch Gut'),
    ('Rechtschaffen Neutral', 'Rechtschaffen Neutral'),
    ('Neutral', 'Neutral'),
    ('Chaotisch Neutral', 'Chaotisch Neutral'),
    ('Rechtschaffen Böse', 'Rechtschaffen Böse'),
    ('Neutral Böse', 'Neutral Böse'),
    ('Chaotisch Böse', 'Chaotisch Böse'),
]

def get_class_choices():
    choices = [(name, name) for name in sorted(KLASSEN_DATEN.keys())]
    choices.insert(0, ('', '--- Wähle eine Klasse ---'))
    return choices

def get_subclass_choices():
    choices = []
    for name, data in KLASSEN_DATEN.items():
        if 'unterklassen' in data:
            for subclass_name in data['unterklassen'].keys():
                choices.append((subclass_name, subclass_name))
    choices = sorted(choices)
    choices.insert(0, ('', '--- Wähle eine Unterklasse (optional) ---'))
    return choices

def get_race_choices():
    choices = [(name, name) for name in sorted(SPEZIES_DATEN.keys())]
    choices.insert(0, ('', '--- Wähle ein Volk ---'))
    return choices

def get_background_choices():
    choices = [(name, name) for name in sorted(HINTERGRUND_DATEN.keys())]
    choices.insert(0, ('', '--- Wähle einen Hintergrund ---'))
    return choices



class UserRegisterForm(forms.ModelForm):
    """Registrierungsformular mit Passwort-Bestätigung und Validierung."""

    password = forms.CharField(
        label='Passwort',
        widget=forms.PasswordInput,
    )
    password_confirm = forms.CharField(
        label='Passwort bestätigen',
        widget=forms.PasswordInput,
    )


    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {
            'username': 'Benutzername',
            'email': 'E-Mail',
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm:
            if password != password_confirm:
                raise forms.ValidationError('Die Passwörter stimmen nicht überein!')

            # Passwort-Stärke prüfen
            user = User(
                username=cleaned_data.get('username'),
                email=cleaned_data.get('email'),
            )
            try:
                validate_password(password, user=user)
            except ValidationError as e:
                self.add_error('password', e)

        return cleaned_data


class CharacterForm(forms.ModelForm):
    """Formular zur Erstellung eines neuen Charakters."""

    EQUIPMENT_CHOICES = [
        ('equipment', 'Startausrüstung (Standardgegenstände für deine Klasse)'),
        ('gold', 'Startgold (Kaufe deine eigene Ausrüstung)'),
    ]

    equipment_preference = forms.ChoiceField(
        label='Ausrüstungswahl',
        choices=EQUIPMENT_CHOICES,
        widget=forms.RadioSelect,
        help_text='Wähle für den Start zwischen Ausrüstung oder Gold.',
    )

    level = forms.IntegerField(
        label='Aktuelle Stufe',
        min_value=1,
        max_value=20,
        initial=1,
        help_text='Die Stufe des Charakters (1-20).'
    )


    character_class = forms.ChoiceField(
        label='Klasse',
        choices=get_class_choices(),
        widget=forms.Select(attrs={
            'class': 'glass-input block w-full pl-10 pr-4 py-3 rounded-xl text-white placeholder-gray-500 focus:ring-0',
            'required': True,
        })
    )

    subclass = forms.ChoiceField(
        label='Unterklasse',
        choices=get_subclass_choices(),
        required=False,
        widget=forms.Select(attrs={
            'class': 'glass-input block w-full pl-10 pr-4 py-3 rounded-xl text-white placeholder-gray-500 focus:ring-0',
        })
    )

    race = forms.ChoiceField(
        label='Volk',
        choices=get_race_choices(),
        widget=forms.Select(attrs={
            'class': 'glass-input block w-full px-4 py-3 rounded-xl text-white placeholder-gray-500 focus:ring-0',
            'required': True,
        })
    )

    background = forms.ChoiceField(
        label='Hintergrund',
        choices=get_background_choices(),
        widget=forms.Select(attrs={
            'class': 'glass-input block w-full px-4 py-3 rounded-xl text-white placeholder-gray-500 focus:ring-0',
            'required': True,
        })
    )

    alignment = forms.ChoiceField(
        label='Gesinnung',
        choices=ALIGNMENT_CHOICES,
        required=False,
        widget=forms.Select(attrs={
            'class': 'glass-input block w-full px-4 py-3 rounded-xl text-white placeholder-gray-500 focus:ring-0',
        })
    )

    abstammung = forms.CharField(
        label='Abstammung',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'glass-input block w-full px-4 py-3 rounded-xl text-white placeholder-gray-500 focus:ring-0',
            'placeholder': 'z.B. Hochelf, Waldelf, etc. (falls anwendbar)',
        })
    )

    class Meta:
        model = Character
        fields = [
            'name', 'level', 'image', 'character_class', 'subclass', 'race',
            'abstammung', 'background', 'alignment', 'personality_traits', 'ideals',
            'bonds', 'flaws',
        ]
        labels = {
            'name': 'Name',
            'level': 'Aktuelle Stufe',
            'image': 'Charakterbild',
            'character_class': 'Klasse',
            'subclass': 'Unterklasse',
            'race': 'Volk',
            'background': 'Hintergrund',
            'alignment': 'Gesinnung',
            'personality_traits': 'Persönlichkeitsmerkmale',
            'ideals': 'Ideale',
            'bonds': 'Bindungen',
            'flaws': 'Makel',
        }
