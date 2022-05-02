from django.urls import path

from . import views

urlpatterns = [
	path('', views.HomePageView.as_view(), name='home'),
	path('dashboard/', views.DashBoardView.as_view(), name='dashboard'),
	path('board/order-history/', views.OrderHistoryView.as_view(), name='order-history'),
	path('contact/', views.ContactView.as_view(), name='contact'),
	path('about/', views.AboutView.as_view(), name='about')
]
