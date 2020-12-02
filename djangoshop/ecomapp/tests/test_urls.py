from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ecomapp.views import (base_view,
 	category_view,
  	product_view,
  	cart_view,
  	add_to_cart_view,
   	remove_from_cart_view,
   	change_item_qty, 
   	checkout_view,
   	order_create_view,
   	make_order_view,
   	account_view,
   	registration_view,
   	login_view)


class TestUrls(SimpleTestCase):

	def test_base_url_is_resolved(self):
		url = reverse('base')
		print(resolve(url))
		self.assertEquals(resolve(url).func, base_view)


	def test_add_to_cart_url_is_resolved(self):
		url = reverse('add_to_cart')
		print(resolve(url))
		self.assertEquals(resolve(url).func,add_to_cart_view)


	def test_remove_from_cart_url_is_resolved(self):
		url = reverse('remove_from_cart')
		print(resolve(url))
		self.assertEquals(resolve(url).func,remove_from_cart_view)


	def test_checkout_url_is_resolved(self):
		url = reverse('checkout')
		print(resolve(url))
		self.assertEquals(resolve(url).func,checkout_view)


	def test_cart_url_is_resolved(self):
		url = reverse('cart')
		print(resolve(url))
		self.assertEquals(resolve(url).func,cart_view)


	def test_order_url_is_resolved(self):
		url = reverse('create_order')
		print(resolve(url))
		self.assertEquals(resolve(url).func,order_create_view)


	def test_make_order_url_is_resolved(self):
		url = reverse('make_order')
		print(resolve(url))
		self.assertEquals(resolve(url).func,make_order_view)


	def test_account_url_is_resolved(self):
		url = reverse('account')
		print(resolve(url))
		self.assertEquals(resolve(url).func,account_view)


	def test_registration_url_is_resolved(self):
		url = reverse('registration')
		print(resolve(url))
		self.assertEquals(resolve(url).func,registration_view)


	def test_login_url_is_resolved(self):
		url = reverse('login')
		print(resolve(url))
		self.assertEquals(resolve(url).func,login_view)


	def test_change_item_qty_url_is_resolved(self):
		url = reverse('change_item_qty')
		print(resolve(url))
		self.assertEquals(resolve(url).func,change_item_qty)


	def test_product_url_is_resolved(self):
		url = reverse('product_detail', args=['some-slug'])
		print(resolve(url))
		self.assertEquals(resolve(url).func,product_view)

	def test_category_url_is_resolved(self):
		url = reverse('category_detail', args=['some-slug'])
		print(resolve(url))
		self.assertEquals(resolve(url).func,category_view)


