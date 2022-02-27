from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
	pass

# class Address(models.Model):
# 	fullname = models.CharField("Nom complet", max_length=255)
# 	phone_number = models.CharField("Numéro de téléphone", max_length=15)
# 	adress1 = models.CharField("ligne 1", max_length=255)
# 	adress2 = models.CharField("ligne 2", max_length=255)
# 	zip_code = models.CharField("Code Postal", max_length=5)
# 	city = models.CharField("Ville", max_length=155)
