from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


def email_validator(value):
    taken_emails = User.objects.filter(email=value)
    if taken_emails:
        raise ValidationError(_('email is already taken'))


class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': _('repeat password')}))
    email = forms.EmailField(max_length=150, required=True, validators=[email_validator],
                             widget=forms.EmailInput(attrs={'placeholder': _('email')}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': _('first name')}),
            'last_name': forms.TextInput(attrs={'placeholder': _('last name')}),
            'password': forms.PasswordInput(attrs={'placeholder': _('password')}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError(_('passwords are not identical'))


class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': _('email')}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': _('password')}))
