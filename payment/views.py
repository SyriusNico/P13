from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from store.models import OrderLine, Order, Product
from P13.local_settings import AUTH_USER_MODEL

# Create your views here.
class CheckoutView(LoginRequiredMixin, TemplateView):
	template_name = 'payment/checkout.html'

	def post(self, request):
		id_products = self.request.POST.getlist('product-id')
		qties = self.request.POST.getlist('quantity')
		print(id_products)
		print(qties)
		context = {}
		index = 0
		total = 0
		basket = OrderLine.objects.filter(customer=request.user.id)
		for b in basket:
			total += b.get_total_price()
		for id_ in id_products:
			product = Product.objects.all().get(id=id_)
			line = OrderLine(
				customer=request.user,
				product=product,
				quantity=qties[index]
			)
			line.save()
			index += 1
		order_count = OrderLine.objects.filter(customer=request.user.id).count()
		context['order'] = basket
		context['total'] = total
		context['count'] = order_count
		return self.render_to_response(context)