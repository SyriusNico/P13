from django.contrib import admin
from .models import Product, Orderline, Category, Order, Favorite
# Register your models here.


admin.site.register(Product)
admin.site.register(Orderline)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Favorite)
