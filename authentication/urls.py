from django.urls import path

from .views import RegisterView, DashBoardView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', DashBoardView.as_view(), name='dashboard')
]