from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django_countries.fields import CountryField
from .models import User
from P13.local_settings import AUTH_USER_MODEL
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

class EditProfileForm(UserChangeForm):
	username = forms.CharField(label=("Nom d'utilisateur"), max_length=100)
	first_name = forms.CharField(label=("Prénom"), max_length=100)
	last_name = forms.CharField(label=("Nom"), max_length=100)

	class Meta:
		model = get_user_model()
		fields = ('username', 'first_name', 'last_name')

class EditMailForm(UserChangeForm):
	email = forms.EmailField(label=("Email"), max_length=200)

	class Meta:
		model = get_user_model()
		fields = ('email',)

class EditAddressForm(forms.ModelForm):
	fullname = forms.CharField(label=("Nom complet"), max_length=255)
	country = forms.CharField(label=("Pays"), max_length=100)
	phone_number = forms.CharField(label=("Numéro de téléphone"), max_length=15)
	address1 = forms.CharField(label=("Adresse ligne 1"), max_length=200)
	address2 = forms.CharField(label=("Adresse ligne 2"), max_length=200)
	postcode = forms.CharField(label=("Code postal"), max_length=5)
	city = forms.CharField(label=("Ville"), max_length=155) 

	class Meta:
		model = get_user_model() 
		fields = ('fullname', 'address1', 'address2', 'city', 'postcode', 'phone_number', 'country')

	def __init__(self, *args, **kwargs):
		super(EditAddressForm, self).__init__(*args, **kwargs)
		self.fields['fullname'].widget.attrs.update({'class': 'field'})
		self.fields['address1'].widget.attrs.update({'class': 'field'})
		self.fields['address2'].widget.attrs.update({'class': 'field'})
		self.fields['postcode'].widget.attrs.update({'class': 'field'})
		self.fields['city'].widget.attrs.update({'class': 'field'})
		self.fields['country'].widget.attrs.update({'class': 'field'})
		self.fields['phone_number'].widget.attrs.update({'class': 'field'})
