from django.urls import path
from .views import (
	ProductView,
	CategoryView,
	ProductByBrandView,
	AjaxView,
	CartView
)

urlpatterns = [
	path('products/', ProductView.as_view(), name='products'),
	path('products/describe', AjaxView.as_view(), name='ajax'),
	path('productbybrand/', ProductByBrandView.as_view(), name='bybrand'),
	path('categories/', CategoryView.as_view(), name='category'),
	path('cart/', CartView.as_view(), name='cart')
]
