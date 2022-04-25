from django.urls import path
from .views import CheckoutView, SuccessView, CancelView


urlpatterns = [
	path('checkout/', CheckoutView.as_view(), name='checkout'),
	path('success/', SuccessView.as_view(), name='success'),
	path('cancel/', CancelView.as_view(), name='cancel')
]
