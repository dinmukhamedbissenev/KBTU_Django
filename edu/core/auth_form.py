# forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User  # Import your custom user model

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User  # Specify your custom user model
        fields = ['username', 'password']
