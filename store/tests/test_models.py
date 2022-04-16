from django.test import TestCase
from authentication.models import User
from store.models import(
	Category, Product,
	Order, Orderline,
	Favorite
	)


class StoreModelsTest(TestCase):

	def setUp(self):
		self.user = User.objects.create(
			email = 'polo@gmail.com',
			username = 'Paul',
			password= 'toto123.',
			) 
		self.category = Category.objects.create(name='chaussures')
		self.product = Product.objects.create(name='Basket',price='15')
		self.order = Order.objects.create(customer=self.user)
		self.orderline = Orderline.objects.create(
			order=self.order,
			product=self.product,
			quantity=3
			)

	def test_product_is_instance(self):
		product = self.product
		self.assertIsInstance(product, Product)

	def test_category_is_category_instance(self):
		category = self.product
		chaussures = self.category
		self.assertNotIsInstance(category, Category)
		self.assertIsInstance(chaussures, Category)

	def test_order_customer_is_true(self):
		order = self.order
		user = self.user
		self.assertNotEqual( order.customer.username, 'Patrick')
		self.assertEqual(order.customer.username, 'Paul' )

	def test_orderline_quantity(self):
		orderline = self.orderline
		total = orderline.get_total_price()
		self.assertEquals(total, 45)
