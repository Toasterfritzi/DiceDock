from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import Character

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm:
            if password != password_confirm:
                raise forms.ValidationError("Passwords do not match!")

            # Validate password strength
            user = User(username=cleaned_data.get('username'), email=cleaned_data.get('email'))
            try:
                validate_password(password, user=user)
            except ValidationError as e:
                self.add_error('password', e)

        return cleaned_data

class CharacterForm(forms.ModelForm):
    EQUIPMENT_CHOICES = [
        ('equipment', 'Startausrüstung (Standard items for your class)'),
        ('gold', 'Startgold (Buy your own items)')
    ]
    equipment_preference = forms.ChoiceField(
        choices=EQUIPMENT_CHOICES, 
        widget=forms.RadioSelect,
        help_text="Wähle für den Start zwischen Ausrüstung oder Gold."
    )

    class Meta:
        model = Character
        fields = [
            'name', 'image', 'character_class', 'subclass', 'race', 
            'background', 'alignment', 'personality_traits', 'ideals', 
            'bonds', 'flaws'
        ]
