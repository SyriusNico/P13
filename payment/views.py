from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


# Create your views here.
class CheckoutView(LoginRequiredMixin, TemplateView):
	template_name = 'payment/checkout.html'

	def post(self, request):
		print(self.request.POST.get('user'))
		print(self.request.POST.getlist('product-name'))
		print(self.request.POST.getlist('quantity'))
		context = {}
		return self.render_to_response(context)