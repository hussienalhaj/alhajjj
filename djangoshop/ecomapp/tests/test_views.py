from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
import json
from ecomapp.models import Category, Product, CartItem, Cart, Order, Brand
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


class TestViews(TestCase):

	def setUp(self):
		self.client = Client()
		self.category1 = Category.objects.create(
					name = 'category1',
					slug = 'category-1'
				)
		self.brand1 = Brand.objects.create(
					name = 'brand1'
				)

		self.product1 = Product.objects.create(
					category = self.category1,
					brand = self.brand1,
					title = 'title1',
					slug = 'product-1',
					description = 'abc',
					image = 'macbook-pro-15',
					price = 10,
				)
		self.cart_item1 = CartItem.objects.create(
					product = self.product1,
					qty = 1,
					item_total = 10.00
				)


	def test_base_view_GET_return_base_html(self):
		response = self.client.get(reverse('base'))
		self.assertTemplateUsed(response, 'base.html')

	def test_product_view_GET_return_product_html(self):
		
		response = self.client.get(reverse('product_detail', args=['product-1']))
		self.assertTemplateUsed(response, 'product.html')


	def test_category_view_GET_return_product_html(self):
		response = self.client.get(reverse('category_detail', args=['category-1']))
		self.assertTemplateUsed(response, 'category.html')


	def test_add_to_cart_view_GET_return_status_200(self):
		self.cart1 = Cart.objects.create(
					#items = cart_item1
				)
		self.cart1.save()

		response = self.client.get(reverse('add_to_cart'),{'product_slug':'product-1'})

		self.assertEquals(response.status_code, 200)

	def test_remove_from_cart_view_GET_return_status_200(self):

		response = self.client.get(reverse('remove_from_cart'),{'product_slug':'product-1'})

		self.assertEquals(response.status_code, 200)

