from django.core.management.base import BaseCommand
from ...models import Category, Product
from bs4 import BeautifulSoup

import requests
import random
import pprint

class PopulateData():

	def __init__(self):

		self.categories = [
			"chaussures",
			"sport-maillots-de-bain/maillots-de-bain",
			"vetements",
			"accessoires"
		]
		self.url = "https://www.fashiola.fr/homme/"

	def set_url(self, url):
		self.url = f"https://www.fashiola.fr/homme/{url}/"
		return self.url

	def get_data(self):
		last_page_content = 97
		for category in self.categories:
			url = self.set_url(category)
			response = requests.request("GET", url)
			soup = BeautifulSoup(response.content, 'html.parser')
			names = soup.find_all("h3", class_="title")
			brands = soup.find_all("span", class_="brand")
			prices = soup.find_all("span", class_="current")
			images = soup.find_all("div", class_="image")
			list_image = [image.img['src'] for image in images]
			categoryData = Category.objects.create(
				name=category, 
				image=list_image[0]
			)
			for product in range(len(names)):
				if product > last_page_content:
					break
				else:
					productData = Product(
						name = names[product].string,
						brand = brands[product].string,
						price = prices[product].string,
						stock = random.randrange(25, 200),
						image = list_image[product+1],
						category = categoryData
					)
					datas = productData.save()

class Command(BaseCommand):

	def handle(self, *args, **options):
		data = PopulateData()
		data.get_data()


