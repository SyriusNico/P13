from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth import get_user_model

class LoginForm(forms.Form):

    username = forms.CharField(label=("Nom d'utilisateur"))
    password = forms.CharField(label=("Mot de passe"))

class RegisterForm(UserCreationForm):
    username = forms.CharField(label=("Nom d'utilisateur"), max_length=30)
    email = forms.EmailField(label=("Email"), max_length=200)
    password1 = forms.CharField(label=("Mot de passe"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=("Confirmer le mot de passe"),
        widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')