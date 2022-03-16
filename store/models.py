from django.db import models
from P13.local_settings import AUTH_USER_MODEL

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=120, null=True)
    image = models.URLField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=120, null=True)
    price = models.CharField(max_length=120, null=True)
    sizes = models.CharField(max_length=255, null=True)
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
        return f"{self.product.name} ({self.quantity})"

    def get_quantity(self):
        quantity = sum()

class Cart(models.Model):
    customer = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.customer.username





# class Address(models.Model):
# 	fullname = models.CharField("Nom complet", max_length=255)
# 	phone_number = models.CharField("Numéro de téléphone", max_length=15)
# 	adress1 = models.CharField("ligne 1", max_length=255)
# 	adress2 = models.CharField("ligne 2", max_length=255)
# 	zip_code = models.CharField("Code Postal", max_length=5)
# 	city = models.CharField("Ville", max_length=155)


