from django.test import TestCase
from authentication.models import User
from django.db.models.query import QuerySet
from store.models import Product, Order, Orderline
from ..services import Services

class ServicesFunctionTest(TestCase):

	def setUp(self):
		self.user = User.objects.create(username='toto',password='toto123.')
		self.product = Product.objects.create(name='chemise',price='15')
		self.order = Order.objects.create(customer=self.user,total_paid=30)
		self.orderline = Orderline.objects.create(
			order=self.order,
			product=self.product,
			quantity=2
		)
		self.user.save()
		self.product.save()
		self.order.save()
		self.orderline.save()
		self.services = Services()

	def test_get_total_function(self):
		order = Order.objects.filter(customer=self.user).first()
		total = self.services.get_total(order.id)
		self.assertEqual(total, 3000)

	def test_key_generator_return_a_random_key(self):
		first_key = self.services.key_generator()
		second_key = self.services.key_generator()
		self.assertNotEqual(first_key, second_key)

	def test_basket_price_is_a_float(self):
		basket = self.services.basket_price(1)
		self.assertNotEqual(type(basket[0]), float())

	def test_basket_price_is_a_queryset(self):
		basket = self.services.basket_price(2)
		self.assertIsInstance(basket[1], QuerySet) 

	def test_create_orderline_function(self):
		product = Product.objects.create(name='pantalon')
		ids = [product.id]
		self.services.create_orderline(ids, self.order, [4])
		orderline = Orderline.objects.filter(quantity=4).first()
		self.assertEqual(orderline.product, product)
		self.assertEqual(orderline.order, self.order)
		self.assertEqual(orderline.quantity, 4)