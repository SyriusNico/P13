from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from authentication.models import User
from store.models import Product, Order, Orderline


class PaymentTestView(TestCase):

	def setUp(self):
		self.client = Client()
		self.factory = RequestFactory()
		self.user = User.objects.create(username='toto', password='toto123.')
		self.product = Product.objects.create(name='chemise', price='15')
		self.order = Order.objects.create(customer=self.user, total_paid=30)
		self.orderline = Orderline.objects.create(
			order=self.order,
			product=self.product,
			quantity=2
		)
		self.user.save()
		self.product.save()
		self.order.save()
		self.orderline.save()

	def test_basket_accessible_by_name(self):
		response = self.client.get(reverse('checkout'))
		self.assertEqual(response.status_code, 302)

	def test_success_accessible_by_name(self):
		response = self.client.get(reverse('success'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'payment/success.html')

	def test_cancel_accessible_by_name(self):
		response = self.client.get(reverse('cancel'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'payment/cancel.html')

	def test_home_view_url_exists_at_desired_location(self):
		response = self.client.get('/payment/checkout/')
		self.assertEqual(response.status_code, 302)

	def test_dashboard_view_url_exists_at_desired_location(self):
		response = self.client.get('/payment/success/')
		self.assertEqual(response.status_code, 200)

	def test_wishlist_view_url_exists_at_desired_location(self):
		response = self.client.get('/payment/cancel/')
		self.assertEqual(response.status_code, 200)

	def test_success_view_content(self):
		response = self.client.get(reverse('success'))
		self.assertIn(b'<p class="success-msg">', response.content)

	def test_checkout_view_post_no_data(self):
		response = self.client.post(reverse('checkout'))
		self.assertEqual(response.status_code, 302)
		self.assertEqual(Order.objects.all().count(), 1)
