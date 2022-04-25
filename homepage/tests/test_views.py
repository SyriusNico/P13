from django.test import TestCase, Client
from django.urls import reverse
from authentication.models import User
from store.models import Product, Order, Favorite


class HomePageTestView(TestCase):

	def setUp(self):
		self.user = User.objects.create(
			email='polo@gmail.com',
			username='Paul',
			fullname='Paul Newman',
			country='Fr',
			phone_number='0123111222333',
			address1='12 rue Liberté',
			address2='impasse',
			postcode='33150',
			city='Cenon',
			password='toto123.',
		)
		self.product = Product.objects.create(
			name='Jean'
		)
		self.client = Client()
		self.favorite = Favorite.objects.create(
			customer=self.user,
			favorite=self.product
		)

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

	def test_wishlist_context_is_not_none(self):
		response = self.client.get(reverse('wishlist'))
		self.assertIsNotNone(response.context['favorites'])

	def test_order_history_context(self):
		response = self.client.get(reverse('order-history'))
		self.assertIsNotNone(response.context['orders'])

	def test_home_view_url_exists_at_desired_location(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)

	def test_dashboard_view_url_exists_at_desired_location(self):
		response = self.client.get('/dashboard/')
		self.assertEqual(response.status_code, 200)

	def test_wishlist_view_url_exists_at_desired_location(self):
		response = self.client.get('/wishlist/')
		self.assertEqual(response.status_code, 200)

	def test_order_history_context_data(self):
		order = Order.objects.create(customer=self.user)
		response = self.client.get('/board/order-history/', {'orders': order})
		self.assertEqual(response.status_code, 200)
