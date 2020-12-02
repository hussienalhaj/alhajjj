from django.test import TestCase, Client
from django.urls import reverse
import ecomapp.models 
from mock import patch

class TestPriceConvertor(TestCase):

	def setUp(self):
		self.category1 = ecomapp.models.Category.objects.create(
					name = 'category1',
					slug = 'category-1'
				)
		self.brand1 = ecomapp.models.Brand.objects.create(
					name = 'brand1'
				)
		self.product1 = ecomapp.models.Product.objects.create(
					category = self.category1,
					brand = self.brand1,
					title = 'title1',
					slug = 'product-1',
					description = 'abc',
					image = 'macbook-pro-15',
					price = 10,
				)

		self.product2 = ecomapp.models.Product.objects.create(
					category = self.category1,
					brand = self.brand1,
					title = 'title1',
					slug = 'product-1',
					description = 'abc',
					image = 'macbook-pro-15',
					price = 10.1111111,
				)

	def test_dollar_convertor_10_5(self):
		self.product1.dollar_convertor()
		self.assertEquals(self.product1.price, 5)

	def test_dollar_convertor_10_1111111_5_05555555(self):
		self.product2.dollar_convertor()
		self.assertEquals(self.product2.price, 5.05555555)

	def test_dollar_convertor_with_mock_10_5(self):
		with patch('ecomapp.models.Product.dollar_convertor') as perm_mock:
			perm_mock.return_value = 5
			
			self.assertEquals(self.product1.dollar_convertor(), 5)

	def test_rub_convertor_10_20(self):
		self.product1.rub_convertor()
		self.assertEquals(self.product1.price, 20)

	def test_rub_convertor_10_1111111_20_2222222(self):
		self.product2.rub_convertor()
		self.assertEquals(self.product2.price, 20.2222222)

	def test_rub_convertor_with_mock_10_20(self):
		with patch('ecomapp.models.Product.rub_convertor') as perm_mock:
			perm_mock.return_value = 20
			
			self.assertEquals(self.product1.rub_convertor(), 20)
		