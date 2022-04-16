from django.test import TestCase, Client, RequestFactory
from django.http import JsonResponse, HttpResponse
from django.urls import reverse
from authentication.models import User
from store.models import Product, Category
	

class StoreTestView(TestCase):

	def setUp(self):
		self.user = User.objects.create(
			email = 'polo@gmail.com',
			username = 'Paul',
			fullname = 'Paul Newman',
			country = 'Fr',
			phone_number = '0123111222333',
			address1 = '12 rue Liberté',
			address2 = 'impasse',
			postcode = '33150',
			city = 'Cenon',
			password= 'toto123.',
			) 
		self.product = Product.objects.create(
			name = 'Jean',
			brand = 'Super'
			)
		self.category = Category.objects.create(name='chaussures')
		self.client = Client()
		self.factory = RequestFactory()
		
	def test_products_accessible_by_name(self):
		response = self.client.get(reverse('products')+'?category=CHAUSSURES' )
		self.assertEqual(response.status_code, 200)

	def test_product_by_brand_accessible_by_name(self):
		response = self.client.get(reverse('bybrand')+'?brand=Super')
		self.assertEqual(response.status_code, 200)

	def test_categories_accessible_by_name(self):
		response = self.client.get(reverse('category'))
		self.assertEqual(response.status_code, 200)

	def test_cart_accessible_by_name(self):
		response = self.client.get(reverse('cart'))
		self.assertEqual(response.status_code, 200)

	def test_products_view_url_exists_at_desired_location(self):
		response = self.client.get('/store/products/?category=chaussures')
		self.assertEqual(response.status_code, 200)

	def test_product_by_brand_view_url_exists_at_desired_location(self):
		response = self.client.get('/store/productbybrand/?brand=Balmain')
		self.assertEqual(response.status_code, 200)

	def test_ajax_view_jsonify_object(self):
		product = Product.objects.filter(name='Jean')
		json_response = JsonResponse(str(product), safe=False)
		self.assertEqual(json_response.status_code, 200)
