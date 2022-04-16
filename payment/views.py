from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, View
from store.models import Orderline, Order, Product
from P13.local_settings import(
	AUTH_USER_MODEL,
	STRIPE_PUBLISHABLE_KEY,
	STRIPE_SECRET_KEY
)
from .services import Services

import stripe


# Create your views here.
class CheckoutView(LoginRequiredMixin, TemplateView):
	template_name = 'payment/basket.html'
	services = Services()

	def client_secret(self,order_id):
		total = self.services.get_total(order_id)
		stripe.api_key = STRIPE_SECRET_KEY
		intent = stripe.PaymentIntent.create(
			currency="eur",
			amount=total,
			payment_method_types=["card"],
			metadata={
				'order_id':self.request.GET.get('order_id')
			}
		)
		return intent.client_secret

	def post(self, request):
		# basket form
		if self.request.method == 'POST':
			user = request.user
			id_products = self.request.POST.getlist('product-id')
			qties = self.request.POST.getlist('quantity')
			# create order
			order = Order(
				customer=user, 
				order_key=self.services.key_generator()
			)
			order.save()
			self.services.create_orderline(id_products, order, qties)
			basket = self.services.basket_price(order.id)
			order.total_paid = basket[0]
			order.save()
			order_count = Orderline.objects.filter(order=order.id).count()
			# context to render
			context = {}
			context['order'] = order
			context['orderline'] = basket[1]
			context['total'] = basket[0]
			context['count'] = order_count
			context['client_secret'] = self.client_secret(order.id)
			return self.render_to_response(context)
			
class SuccessView(TemplateView):
    template_name = "payment/success.html"

class CancelView(TemplateView):
    template_name = "payment/cancel.html"