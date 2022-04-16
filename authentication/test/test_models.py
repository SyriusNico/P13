from django.test import TestCase
from authentication.models import User


class UserModelsTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		User.objects.create(
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

	def test_user_is_instance(self):
		customer = User.objects.create(username='toto',password=('tototo12'))
		self.assertIsInstance(customer, User)

	def test_customer_is_user_instance(self):
		customer = 'User.objects.get(id=3)'
		self.assertNotIsInstance(customer, User)

	def test_customer_exist(self):
		customer = User.objects.get(id=1)
		self.assertNotEqual(customer.id, 4)

	def test_username_is_true(self):
		customer = User.objects.get(id=1)
		self.assertFalse( customer.username == 'Patrick')

	def test_username_label(self):
		customer = User.objects.get(id=1)
		field_label = customer._meta.get_field('username').verbose_name
		self.assertEquals(field_label, "Nom d'utilisateur")

	def test_address_label(self):
		customer = User.objects.get(id=1)
		field_label = customer._meta.get_field('address1').verbose_name
		self.assertEquals(field_label, 'address1')

	def test_fullname_max_length(self):
		customer = User.objects.get(id=1)
		max_length = customer._meta.get_field('fullname').max_length
		self.assertEquals(max_length, 255)

	def test_city_max_length(self):
		customer = User.objects.get(id=1)
		max_length = customer._meta.get_field('city').max_length
		self.assertEquals(max_length, 155)

	def test_object_name_is_username(self):
		customer = User.objects.get(id=1)
		expected_object_name = f'{customer.username}'
		self.assertEquals(expected_object_name, str(customer))

	def test_superuser_is_instance(self):
		customer = User.objects.create_superuser('toto@gmail.com', 'toto', 'toto123.')
		self.assertIsInstance(customer, User)

	def test_user_is_superuser(self):
		customer = User.objects.create_superuser('toto@gmail.com', 'toto', 'toto123.')
		field_label = customer._meta.get_field('is_superuser')
		self.assertTrue(field_label)

	def test_customer_manager_create_user(self):
		customer = User.objects.create_user('to@gmail.com', 'to', 'to123.')
		self.assertIsInstance(customer, User)
