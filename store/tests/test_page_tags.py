from django.test import TestCase, Client
from django.template import Context, Template


class PageTagsTest(TestCase):

	def setUp(self):
		self.client = Client()

	def test_rendered(self):
		context = Context({'page_obj': 'page'})
		template_to_render = Template(
			'{% load page_tags %}'
			'{% if page_obj.has_previous %}'
		    '<li><a href="?{% param_replace page=1 %}">&laquo; Début</a></li>'
			'{% endif %}'
		)
		rendered_template = template_to_render.render(context)
		# self.assertInHTML('<a href="page=1">', rendered_template)

	# def test_page_tags_redirect_to_next_page(self):
	# 	reponse = self.client.get('/store/products/?category=vetements&page=2/')
	# 	print(reponse)