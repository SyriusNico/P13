from django.contrib import admin
from .models import Product, OrderLine, Category, Order
# Register your models here.


admin.site.register(Product)
admin.site.register(OrderLine)
admin.site.register(Category)
admin.site.register(Order)
