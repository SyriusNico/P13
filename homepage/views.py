from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from store.models import Order, Orderline, Favorite, Product

class HomePageView(TemplateView):
	template_name = 'homepage/home.html'

class DashBoardView(TemplateView):
	template_name = 'homepage/dashboard.html'

class OrderHistoryView(ListView):
	template_name = 'homepage/order-history.html'
	model = Order

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		user_orders = Order.objects.filter(customer=self.request.user.id)
		orders = []
		for user_order in user_orders:
			orderline = user_order.orderline_set.all()
			for line in orderline:
				print(line)
				orders.append(line)
		context['orders'] = orders
		return context

class AddressView(TemplateView):
	template_name = 'homepage/address.html'


class AddFavoriteView(TemplateView):
	template_name = None
	model = Favorite

	def post(self,request):
		if self.request.method == 'POST':
			product = Product.objects.filter(
				name=self.request.POST.get('product')
			).first()
			favorite = Favorite.objects.create(
				customer=self.request.user,
				favorite=product
			)
		return redirect(request.META['HTTP_REFERER'])

class WishListView(ListView):
	template_name = 'homepage/wishlist.html'
	model = Favorite
	context_object_name = 'favorites'