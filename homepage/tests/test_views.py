from django.test import TestCase, Client, RequestFactory
from django.urls import reverse


class HomePageTestView(TestCase):

	def setUp(self):
		self.client = Client()
		
	def test_home_accessible_by_name(self):
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 200)

	def test_dashboard_accessible_by_name(self):
		response = self.client.get(reverse('dashboard'))
		self.assertEqual(response.status_code, 200)

	def test_order_history_accessible_by_name(self):
		response = self.client.get(reverse('order-history'))
		self.assertEqual(response.status_code, 200)

	def test_wishlist_accessible_by_name(self):
		response = self.client.get(reverse('wishlist'))
		self.assertEqual(response.status_code, 200)

	def test_home_view_url_exists_at_desired_location(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)

	def test_dashboard_view_url_exists_at_desired_location(self):
		response = self.client.get('/dashboard/')
		self.assertEqual(response.status_code, 200)

	def test_wishlist_view_url_exists_at_desired_location(self):
		response = self.client.get('/wishlist/')
		self.assertEqual(response.status_code, 200)