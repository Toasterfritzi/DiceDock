from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from .models import Character


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

    class Meta:
        model = Character
        fields = [
            'name', 'level', 'image', 'character_class', 'subclass', 'race',
            'background', 'alignment', 'personality_traits', 'ideals',
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
