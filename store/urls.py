from django.urls import path
from .views import ProductView, CategoryView


urlpatterns = [
	path('products/', ProductView.as_view(), name='products'),
	path('categories/', CategoryView.as_view(), name='category'),
]