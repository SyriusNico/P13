from django.urls import path
from .views import (
    RegisterView, PasswordsChangeView,
    UsernameChangeView, AccountDetailView,
    MailChangeView, AddressView
)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('password/', PasswordsChangeView.as_view(), name='password-change'),
    path('username-change/', UsernameChangeView.as_view(), name='username-change'),
    path('mail-change/', MailChangeView.as_view(), name='mail-change'),
    path('account-detail/', AccountDetailView.as_view(), name='account-detail'),
    path('address/', AddressView.as_view(), name='address'),
]
