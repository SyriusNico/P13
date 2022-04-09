from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, View
from store.models import Orderline, Order, Product
from P13.local_settings import(
	AUTH_USER_MODEL,
	STRIPE_PUBLISHABLE_KEY,
	STRIPE_SECRET_KEY
)


import random
import string
import stripe


# Create your views here.
class CheckoutView(LoginRequiredMixin, TemplateView):
	template_name = 'payment/basket.html'

	def get_total(self,order_id):
		order = Order.objects.all().get(id=order_id)
		total = str(order.total_paid)
		total = total.replace(".","")
		total = int(total)
		return total

	def client_secret(self,order_id):
		total = self.get_total(order_id)
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

	def key_generator(self):
		letters = string.ascii_letters
		key = ''
		for i in range(3):
			key += ''.join(random.choice(letters) for i in range(2))
			key += str(random.randint(1,10))
		return key

	def post(self, request):
		# basket form
		if self.request.method == 'POST':
			user = request.user
			id_products = self.request.POST.getlist('product-id')
			qties = self.request.POST.getlist('quantity')
			# create order
			order = Order(customer=user, order_key=self.key_generator())
			order.save()
			# create order line
			index = 0
			for id_ in id_products:
				product = Product.objects.all().get(id=id_)
				line = Orderline(
					order=order,
					product=product,
					quantity=qties[index]
				)
				line.save()
				index += 1
			basket = Orderline.objects.filter(order=order.id)
			# get total price
			total = 0
			for b in basket:
				total += b.get_total_price()
			order.total_paid = total
			order.save()
			order_count = Orderline.objects.filter(order=order.id).count()

			# context to render
			context = {}
			context['order'] = order
			context['orderline'] = basket
			context['total'] = total
			context['count'] = order_count
			context['client_secret'] = self.client_secret(order.id)
			return self.render_to_response(context)
			
class SuccessView(TemplateView):
    template_name = "payment/success.html"

class CancelView(TemplateView):
    template_name = "payment/cancel.html"