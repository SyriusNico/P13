from django.core.management.base import BaseCommand
from ...models import Category, Product
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import requests
import random
import time
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
		last_page_content = 95
		for category in self.categories:
			url = self.set_url(category)
			response = requests.request("GET", url)
			soup = BeautifulSoup(response.content, 'html.parser')
			names = soup.find_all("h3", class_="title")
			brands = soup.find_all("span", class_="brand")
			prices = soup.find_all("span", class_="current")
			images = soup.find_all("div", class_="image")
			descriptions = self.get_description(category)
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
						description = descriptions[product+1],
						image = list_image[product+1],
						category = categoryData
					)
					datas = productData.save()

	def get_description(self, category):
		option = webdriver.ChromeOptions()
		option.add_argument("headless")
		driver = webdriver.Chrome(
			service=Service(ChromeDriverManager().install()),
			options=option
		)
		driver.get(self.set_url(category))
		informations = driver.find_elements(By.CLASS_NAME, "info")
		descriptions = []
		for information in informations:
			url = information.get_attribute("data-x")
			if url is None:
				pass
			else:
				response = requests.request("GET", url)
				soup = BeautifulSoup(response.content, 'html.parser')
				description = soup.find("p", class_="description").string
				descriptions.append(description)
		return descriptions


class Command(BaseCommand):

	def handle(self, *args, **options):
		data = PopulateData()
		data.get_data()
