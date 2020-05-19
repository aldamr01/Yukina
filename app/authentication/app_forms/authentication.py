# Django
from django import forms
from django.contrib.auth.forms import PasswordResetForm


class AuthenticationForm(forms.Form):
    
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'max-length': 20
            }
        ),
        label= 'Username',
        required= True
    )
    password = forms.CharField(
        widget= forms.PasswordInput(),
        label= 'Password',
        required= True
    )
    
    class Meta:
        fields = ('username', 'password')