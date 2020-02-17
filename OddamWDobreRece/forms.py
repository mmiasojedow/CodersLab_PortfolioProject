from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def email_validator(value):
    taken_emails = User.objects.filter(email=value)
    if taken_emails:
        raise ValidationError('Podany Email jest już zajęty')


class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Imię'}))
    surname = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'placeholder': 'Nazwisko'}))
    email = forms.EmailField(max_length=150, required=True, validators=[email_validator],
                             widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Powtórz hasło'}))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('Hasła nie są identyczne')
