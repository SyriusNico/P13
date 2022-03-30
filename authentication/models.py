from django.db import models
from django.contrib.auth.models import ( 
	AbstractUser, 
	UserManager, 
	PermissionsMixin
)
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as lazy_


class CustomAccountManager(UserManager):

	def create_superuser(self, email, username, password, **other_fields):

		other_fields.setdefault('is_staff', True)
		other_fields.setdefault('is_superuser', True)
		other_fields.setdefault('is_active', True)

		if other_fields.get('is_staff') is not True:
			raise ValueError(
				'Le super utilisateur doit être assigné à is_staff=True.')
		if other_fields.get('is_superuser') is not True:
			raise ValueError(
				'Le super utilisateur doit être assigné à is_superuser=True.')

		return self.create_user(email, username, password, **other_fields)

	def create_user(self, email, username, password, **other_fields):

		if not email:
			raise ValueError(lazy_('Vous devez fournir une adresse email'))

		email = self.normalize_email(email)
		user = self.model(username=username,**other_fields)
		user.set_password(password)
		user.save()
		return user


class User(AbstractUser, PermissionsMixin):
	
	email = models.EmailField(lazy_('adresse mail'), unique=True)
	username = models.CharField("Nom d'utilisateur",max_length=150, unique=True)
	country = CountryField()
	phone_number = models.CharField(max_length=15, blank=True)
	address1 = models.CharField(max_length=150, blank=True)
	address2 = models.CharField(max_length=150, blank=True)
	postcode = models.CharField(max_length=5, blank=True)
	city = models.CharField(max_length=155, blank=True)	

	objects = CustomAccountManager()

	USERNAME_FIELD = 'username'
	EMAIL_FIELD = 'email'
	REQUIRED_FIELDS = ['email']

	class Meta:
		verbose_name = "Accounts"
		verbose_name_plural = "Accounts"

	def __str__(self):
		return self.username
