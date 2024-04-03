from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Account


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = Account
        fields = ["email", "name", "username", "password1", "password2"]
