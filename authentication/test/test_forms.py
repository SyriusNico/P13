from django.test import TestCase
from authentication import forms


class AuthenticationFormTest(TestCase):

	def test_login_form_label(self):
		form = forms.LoginForm()
		self.assertTrue(
			form.fields['username'].label == "Nom d'utilisateur" and 
			form.fields['password'].label == "Mot de passe"
		)

	def test_register_form_label(self):
		form = forms.RegisterForm()
		self.assertTrue(
			form.fields['username'].label == "Nom d'utilisateur" and
			form.fields['email'].label == "Email" and
			form.fields['password1'].label == "Mot de passe" and
			form.fields['password2'].label == "Confirmer le mot de passe"
		)

	def test_edit_profile_form_label(self):
		form = forms.EditProfileForm()
		self.assertTrue(
			form.fields['username'].label == "Nom d'utilisateur" and
			form.fields['first_name'].label == "Prénom" and
			form.fields['last_name'].label == "Nom"
		)

	def test_edit_email_form_label(self):
		form = forms.EditMailForm()
		self.assertTrue(form.fields['email'].label == "Email")

	def test_edit_address_form_label(self):
		form = forms.EditAddressForm()
		self.assertTrue(
			form.fields['fullname'].label == "Nom complet" and
			form.fields['country'].label == "Pays" and
			form.fields['phone_number'].label == "Numéro de téléphone" and
			form.fields['address1'].label == "Adresse ligne 1" and
			form.fields['address2'].label == "Adresse ligne 2" and
			form.fields['postcode'].label == "Code postal" and
			form.fields['city'].label == "Ville"
		)

	def test_login_form_is_valid(self):
		form = forms.LoginForm(data={'username': 3.5,
									 'password':' '})
		self.assertFalse(form.is_valid())

	def test_register_form_is_valid(self):
		form = forms.RegisterForm(data={
			'username': 3.5,
			'email': 455,
			'password1':' ',
			'password2':'r'
		})
		self.assertFalse(form.is_valid())

	def test_edit_profile_form_is_valid(self):
		form = forms.EditProfileForm(data={'username': 'polo',
									 	   'first_name': 'Paul',
									 	   'last_name': 'Newman' })
		self.assertTrue(form.is_valid())

	def test_edit_address_form_is_valid(self):
		form = forms.EditAddressForm(data={'fullname': 'Paul Newman',
										   'country': 'Fr',
									 	   'phone_number': '0590123410', 
									 	   'address1': '12 rue Lilolou',
									 	   'address2': 'yoyo',
									 	   'postcode': '97139',
									 	   'city': 'toto'})
		self.assertTrue(form.is_valid())