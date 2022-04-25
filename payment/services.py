from store.models import Orderline, Order, Product

import random
import string


class Services():

	def create_orderline(self, ids, order, qties):
		index = 0
		for id_ in ids:
			product = Product.objects.all().get(id=id_)
			line = Orderline(
				order=order,
				product=product,
				quantity=qties[index]
			)
			line.save()
			index += 1

	def basket_price(self, id_):
		total = 0
		basket = Orderline.objects.filter(order=id_)
		for b in basket:
			total += b.get_total_price()
		return float(total), basket

	def key_generator(self):
		letters = string.ascii_letters
		key = ''
		for i in range(3):
			key += ''.join(random.choice(letters) for i in range(2))
			key += str(random.randint(1, 10))
		return key

	def get_total(self, order_id):
		order = Order.objects.all().get(id=order_id)
		total = str(order.total_paid)
		total = total.replace(".", "")
		total = int(total)
		return total
