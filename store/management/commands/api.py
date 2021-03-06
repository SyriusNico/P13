from django.core.management.base import BaseCommand
from ...models import Category, Product
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import requests
import random


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

	def get_data(self, category):
		url = self.set_url(category)
		response = requests.request("GET", url)
		soup = BeautifulSoup(response.content, 'html.parser')
		names = soup.find_all("h3", class_="title")
		brands = soup.find_all("span", class_="brand")
		prices = soup.find_all("span", class_="current")
		sizes = self.get_sizes(category)
		images = soup.find_all("div", class_="image")
		descriptions = self.get_description(category)
		list_image = [image.img['src'] for image in images]
		categoryData = Category.objects.create(
			name=category,
			image=list_image[0]
		)

		for product in range(len(names)):

			try:
				productData = Product(
					name=names[product].string,
					brand=brands[product].string,
					price=prices[product].string,
					sizes=sizes[product],
					stock=random.randrange(25, 200),
					description=descriptions[product],
					image=list_image[product + 1],
					category=categoryData
				)
				productData.save()
			except IndexError:
				pass

	def get_description(self, category):
		option = webdriver.ChromeOptions()
		option.add_argument("headless")
		option.add_argument("--no-sandbox")
		option.add_argument("--disable-dev-shm-usage")
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
		driver.close()
		return descriptions

	def get_sizes(self, category):
		option = webdriver.ChromeOptions()
		option.add_argument("headless")
		option.add_argument("--no-sandbox")
		option.add_argument("--disable-dev-shm-usage")		
		driver = webdriver.Chrome(
			service=Service(ChromeDriverManager().install()),
			options=option
		)
		driver.get(self.set_url(category))
		informations = driver.find_elements(By.CLASS_NAME, "info")
		sizes = []
		for information in informations:
			url = information.get_attribute("data-x")
			if url is None:
				pass
			else:
				response = requests.request("GET", url)
				soup = BeautifulSoup(response.content, 'html.parser')
				size = soup.find_all("a", class_="size")
				size = [one_size.string for one_size in size]
				sizes.append(size)
		driver.close()
		return sizes


class Command(BaseCommand):

	def handle(self, *args, **options):
		data = PopulateData()
		for category in data.categories:
			data.get_data(category)
