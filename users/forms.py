from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # keeps the configurations in one place.
    # Setting the required fields by default=True
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
