from django.test import TestCase, Client
from django.urls import reverse
from authentication.models import User


class AuthenticationTestView(TestCase):
	def setUp(self):
		self.client = Client()
		self.user = User.objects.create(username='testuser')
		self.user.set_password('secret')
		self.user.save()

	def test_user_login_view_url(self):
		response = self.client.get(reverse('login'))
		self.assertEqual(response.status_code, 200)

	def test_user_register_view_url(self):
		response = self.client.get(reverse('register'))
		self.assertEqual(response.status_code, 200)

	def test_password_change_view_url(self):
		response = self.client.get(reverse('password-change'))
		self.assertEqual(response.status_code, 302)

	def test_account_detail_view_url(self):
		response = self.client.get(reverse('account-detail'))
		self.assertEqual(response.status_code, 200)

