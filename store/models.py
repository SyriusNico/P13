from django.db import models
from P13.local_settings import AUTH_USER_MODEL


# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=120, null=True)
	image = models.URLField(max_length=255, null=True)

	def __str__(self):
		return self.name


class Product(models.Model):
	name = models.TextField()
	brand = models.CharField(max_length=120, null=True)
	price = models.CharField(max_length=120, null=True)
	sizes = models.TextField(null=True)
	stock = models.IntegerField(default=0)
	description = models.TextField(null=True)
	image = models.URLField(max_length=255, null=True)
	category = models.ForeignKey(
		Category,
		on_delete=models.CASCADE,
		null=True
	)

	class Meta:
		ordering = ['-id']

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('product-detail', args=[self.id,])


class Order(models.Model):
	customer = models.ForeignKey(
		AUTH_USER_MODEL, 
		on_delete=models.CASCADE, 
		related_name='order_user',
		null=True
	)
	fullname = models.CharField(max_length=255, null=True)
	address1 = models.CharField(max_length=150, null=True)
	address2 = models.CharField(max_length=150, null=True)
	postcode = models.CharField(max_length=5, null=True)
	city = models.CharField(max_length=155, null=True)
	state = models.CharField(max_length=155, null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	total_paid = models.DecimalField(max_digits=5, decimal_places=2, null=True)
	order_key = models.CharField(max_length=200)
	billing_status = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.id}"


class Orderline(models.Model):
	order = models.ForeignKey(
		Order,
		on_delete=models.CASCADE,
		null=True
	)
	product = models.ForeignKey(
		Product, 
		on_delete=models.CASCADE,
		null=True
	)
	quantity = models.IntegerField(default=1)
	ordered = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.id}"


	def get_total_price(self):
		price = self.product.price.replace(" €","")
		price = price.replace(",",".")
		price = float(price)
		return price * int(self.quantity)


class Favorite(models.Model):
	customer = models.ForeignKey(
		AUTH_USER_MODEL,
		on_delete=models.CASCADE
	)
	favorite = models.ForeignKey(Product, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.favorite}"