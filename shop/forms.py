
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core import validators


class CustomerRegistrationForm(UserCreationForm):

    telephone_number = forms.IntegerField(label='phone number / Username')
    address = forms.CharField(max_length=30, label='Place of Residence')


    class Meta:
        model = User
        fields = ['telephone_number', 'address']
        widgets = {
            'address': forms.TextInput(attrs={'required': True}),
            'contact_number': forms.NumberInput(attrs={'required': True}),
        }


class LoginForm(forms.Form):
    telephone = UsernameField(
        widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Telephone Number'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'password'}))

    class Meta:
        model = User
