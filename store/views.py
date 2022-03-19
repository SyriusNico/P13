from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.views.generic import( 
	ListView, 
	DetailView, 
	TemplateView, 
	)
from django.core.paginator import Paginator, EmptyPage
from .models import Product, Category

import pprint


class ProductView(ListView):
	template_name = 'store/products.html'
	model = Product
	paginate_by = 12
	paginate_orphans = 2

	def get_category(self):
		query = self.request.GET.get('category')
		return query

	def filter_duplicates(self, filtered_list):
		brands = set([product.brand for product in filtered_list])
		checklist = brands.add
		unique_brandlist = set(product.brand for product in filtered_list if product.brand in brands or checklist(x))		
		return list(unique_brandlist)

	def get_context_data(self, *, product_list=None, **kwargs):
		"""Get the context for this view."""
		product_list = self.model.objects.all().filter(
			category__name=self.get_category()
		)
		brands = self.filter_duplicates(product_list)
		categories = Category.objects.all()
		queryset = product_list if product_list is not None else self.product_list
		page_size = self.get_paginate_by(queryset)
		context_object_name = self.get_context_object_name(queryset)
		if page_size:
			paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, page_size)
			context = {
				'paginator': paginator,
				'page_obj': page,
				'is_paginated': is_paginated,
				'product_list': queryset,
				'brands' : brands,
				'product_category' : product_list[:1],
				'categories' : categories
			}
		else:
			context = {
				'paginator': None,
				'page_obj': None,
				'is_paginated': False,
				'brands' : brands,
				'product_list': queryset,
				'categories' : categories
			}
		if context_object_name is not None:
			context[context_object_name] = queryset
		context.update(kwargs)
		return super().get_context_data(**context)


class CategoryView(ListView):
	template_name = 'store/category.html'
	model = Category

	def get_context_data(self, *, categories=None, **kwargs):
		"""Get the context for this view."""
		categories = self.model.objects.all()
		queryset = categories if categories is not None else self.categories
		page_size = self.get_paginate_by(queryset)
		context_object_name = self.get_context_object_name(queryset)
		if page_size:
			paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, page_size)
			context = {
				'paginator': paginator,
				'page_obj': page,
				'is_paginated': is_paginated,
				'categories': queryset
			}
		else:
			context = {
				'paginator': None,
				'page_obj': None,
				'is_paginated': False,
				'categories': queryset
			}
		if context_object_name is not None:
			context[context_object_name] = queryset
		context.update(kwargs)
		return super().get_context_data(**context)

class ProductByBrandView(ListView):
	template_name = 'store/product_by_brand.html'
	model = Product
	paginate_by = 10
	paginate_orphans = 2

	def get_brand(self):
		query = self.request.GET.get('brand')
		return query

	def filter_duplicates(self, filtered_list):
		brands = set([product.brand for product in filtered_list])
		checklist = brands.add
		unique_brandlist = set(product.brand for product in filtered_list if product.brand in brands or checklist(x))		
		return list(unique_brandlist)

	def get_context_data(self, *, product_list=None, **kwargs):
		"""Get the context for this view."""
		product_list = self.model.objects.all()
		product_by_brand = self.model.objects.all().filter(
			brand=self.get_brand()
		)
		brands = self.filter_duplicates(product_list)
		categories = Category.objects.all()
		queryset = product_by_brand
		page_size = self.get_paginate_by(queryset)
		context_object_name = self.get_context_object_name(queryset)
		if page_size:
			paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, page_size)
			context = {
				'paginator': paginator,
				'page_obj': page,
				'is_paginated': is_paginated,
				'product_list': queryset,
				'brands' : brands,
				'categories' : categories
			}
		else:
			context = {
				'paginator': None,
				'page_obj': None,
				'is_paginated': False,
				'brands' : brands,
				'product_list': queryset,
				'categories' : categories
			}
		if context_object_name is not None:
			context[context_object_name] = queryset
		context.update(kwargs)
		return super().get_context_data(**context)


class ProductDetailView(DetailView):
	context_object_name = 'product'
	# queryset = Product.objects.all()

	def get_object(self):
		id_ = self.kwargs.get('id')
		return get_object_or_404(Product, id=id_)

# 	def jsonify_content(self):
# 		products = Product.objects.all()
# 		product = products.filter(id=self.request.GET.get('description'))		
# 		return JsonResponse({'product':list(product.values())})

# 	def get_context_data(self, **kwargs):
# 		"""Call the base implementation first to get a context"""
# 		context = super().get_context_data(**kwargs)
# 		product_json = self.jsonify_content()
# 		context['json_product'] = product_json
# 		return context

class AjaxView(TemplateView):
	template_name = None

	def product_json(self):
		products = Product.objects.all()
		product = products.filter(id=self.request.GET.get('description'))
		product = list(product.values())
		product[0]['sizes'] = product[0]['sizes'].split(",")
		print(product)		
		return JsonResponse(product, safe=False)

	def get(self, *args, **kwargs):
		# is_ajax = self.request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
		if self.request.method == "GET":
			return self.product_json()
		return JsonResponse({"success":False}, status=400)

class CartView(TemplateView):
	template_name = 'store/cart.html'

	# def post(self, *args, **kwargs):
	# 	if self.request.method == 'POST':
	# 		order = {
	# 			'id_' : self.request.POST.get('product'),
	# 			'user_' : self.request.POST.get('user'),
	# 			'quantity' : self.request.POST.get('quantity')
	# 		}
	# 		return JsonResponse(order, safe=False)