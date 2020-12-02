from django.test import TestCase, Client
from django.urls import reverse
from ecomapp.models import Category, Product, CartItem, Cart, Order, Brand


class TestModels(TestCase):

		def setUp(self):
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

			self.product2= Product.objects.create(
					category = self.category1,
					brand = self.brand1,
					title = 'title2',
					slug = 'product-2',
					description = 'abc',
					image = 'macbook-pro-15',
					price = 15,
				)

			self.cart_item1 = CartItem.objects.create(
					product = self.product1,
					qty = 1,
					item_total = 10.00
				)

			self.cart_item2 = CartItem.objects.create(
					product = self.product2
				)
			self.cart1 = Cart.objects.create(
					
				)

		#AC
		def test_add_to_cart_then_remove_from_cart_is_false(self):
			self.cart1.add_to_cart(self.product1.slug)
			self.cart1.remove_from_cart(self.product1.slug)
			self.assertFalse(self.cart1.items.all())

		#AD2
		def test_add_to_cart_if_item_in_cart(self):
			self.cart1.add_to_cart(self.product1.slug)
			self.cart1.add_to_cart(self.product1.slug)
			self.cart1.cart_total = self.cart1.count_total_price()
			self.assertEquals(self.cart1.cart_total, 10)

		#ACD
		def test_remove_from_cart_product1_is_successful(self):
			self.cart1.add_to_cart(self.product1.slug)
			self.cart1.remove_from_cart(self.product1.slug)
			self.cart1.cart_total = self.cart1.count_total_price()
			self.assertEquals(self.cart1.cart_total, 0)

		#CD
		def test_remove_from_cart_if_item_is_not_in_cart(self):
			self.cart1.remove_from_cart(self.product1.slug)
			self.cart1.cart_total = self.cart1.count_total_price()
			self.assertEquals(self.cart1.cart_total, 0)

		#AD
		def test_add_to_cart_count_total_price_10_is_10(self):
			self.cart1.add_to_cart(self.product1.slug)
			self.cart1.cart_total = self.cart1.count_total_price()
			self.assertEquals(self.cart1.cart_total, 10)

		def test_add_to_cart_count_total_price_for_some_changes(self):
			self.cart1.add_to_cart(self.product1.slug)
			self.cart1.remove_from_cart(self.product1.slug)
			self.cart1.cart_total = self.cart1.count_total_price()
			self.assertEquals(self.cart1.cart_total, 0)

		#AB
		def test_add_to_cart_change_qty_1_changes_to_3(self):
			self.cart1.add_to_cart(self.product1.slug)
			self.cart1.change_qty(3, self.cart_item1.product.id)
			self.assertEquals(self.cart1.cart_total, 30)

		#AB2
		def test_add_to_cart_change_qty_3_changes_to_2(self):
			self.cart1.add_to_cart(self.product1.slug)
			self.cart1.change_qty(3, self.cart_item1.product.id)
			self.cart1.change_qty(2, self.cart_item1.product.id)
			self.assertEquals(self.cart1.cart_total, 20)
