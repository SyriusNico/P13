from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView
from store.models import Order, Product


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
			orders.append(orderline)
		context['orders'] = user_orders
		context['articles'] = orders
		return context


class ContactView(TemplateView):
	template_name = 'homepage/contact.html'


class AboutView(TemplateView):
	template_name = 'homepage/about.html'
