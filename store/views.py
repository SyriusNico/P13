from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Product, Category

# Create your views here.
class ProductView(ListView):
	template_name = 'store/products.html'
	model = Product
	paginate_by = 12
	paginate_orphans = 2


	def get_category(self):
		query = self.request.GET.get('category')
		return query

	def get_context_data(self, *, product_list=None, **kwargs):
		"""Get the context for this view."""
		product_list = self.model.objects.all().filter(
			category__name=self.get_category()
		)
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
				'categories' : categories
			}
		else:
			context = {
				'paginator': None,
				'page_obj': None,
				'is_paginated': False,
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
