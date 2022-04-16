from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from authentication.models import User

import time


class PaymentSeleniumTests(StaticLiveServerTestCase):

	def setUp(self):
		self.option = webdriver.ChromeOptions()
		self.option.add_argument("start-maximized")
		self.selenium = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
		self.selenium.implicitly_wait(10)

	def tearDown(self):
		self.selenium.close() 

	def test_payment(self):
		self.selenium.get(f"{self.live_server_url}/authentication/login/")
		time.sleep(2)
		username = self.selenium.find_element_by_xpath('//*[@id="id_username"]')
		username.send_keys('Polo')
		time.sleep(2)
		print('utilisateur')
		pwd = self.selenium.find_element_by_xpath('//*[@id="id_password"]')
		pwd.send_keys('max12345.')
		print(pwd)
		time.sleep(2)
		print('mdp')
		valid_text = self.selenium.find_element_by_xpath('//*[@id="valid-text"]')
		valid_text.click()
		# wear_category = self.selenium.find_element(By.ID, 'vetements').click()
		# jacket = self.selenium.find_element_by_name('description')
		# if jacket.getAttribute('value') == 1633:
		# 	jacket.click()
		# add = self.selenium.find_element(By.CLASS_NAME, 'add-to-cart').click()
		# basket = self.selenium.find_element(By.ID, 'basket').click()
		# order = self.selenium.find_element_by_name('order').click()
		# card_number = self.selenium.find_element_by_name('number')
		# card_number.send_keys('4242424242424242')
		# expiry = self.selenium.find_element_by_name('expiry')
		# expiry.send_keys('1224')
		# cvc = self.selenium.find_element_by_name('cvc')
		# cvc.send_keys('123')
		# submit = self.selenium.find_element(By.ID, 'submit')
		# self.assertIn('success', self.selenium.page_source)
		time.sleep(10)