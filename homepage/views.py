from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class HomePageView(TemplateView):
	template_name = 'homepage/home.html'

class DashBoardView(TemplateView):
	template_name = 'homepage/dashboard.html'