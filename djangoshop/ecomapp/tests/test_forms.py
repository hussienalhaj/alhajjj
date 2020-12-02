from django.test import TestCase
from ecomapp.forms import LoginForm, RegistrationForm, OrderForm
from parameterized import parameterized


class TestRegistrationFormsOnUsernameIfTrue(TestCase):

	
	form = RegistrationForm(data={
		'username': 'uqq',
		'password': 'xdvgy4321',
		'password_check': 'xdvgy4321'
		})

	form1 = RegistrationForm(data={
		'username': 'u'*30,
		'password': 'xdvgy4321',
		'password_check': 'xdvgy4321'
		})

	form2 = RegistrationForm(data={
		'username': 'u'*7,
		'password': 'xdvgy4321',
		'password_check': 'xdvgy4321'
		})

	form3 = RegistrationForm(data={
		'username': 'u'*15,
		'password': 'xdvgy4321',
		'password_check': 'xdvgy4321'
		})

	@parameterized.expand([[form],[form1], [form2], [form3]])

	
	def test_username_registration_form_valid_data_true(self, lst):

		self.assertTrue(lst.is_valid())


class TestRegistrationFormsOnUsernameIfFalse(TestCase):

	form4 = RegistrationForm(data={
		'username': 'uq',
		'password': 'xdvgy4321',
		'password_check': 'xdvgy4321'
		})

	form5 = RegistrationForm(data={
		'username': 'u'*31,
		'password': 'xdvgy4321',
		'password_check': 'xdvgy4321'
		})

	form6 = RegistrationForm(data={
		'username': 'u'*50,
		'password': 'xdvgy4321',
		'password_check': 'xdvgy4321'
		})
	form7 = RegistrationForm(data={
		'username': 'u',
		'password': 'xdvgy4321',
		'password_check': 'xdvgy4321'
		})


	@parameterized.expand([[form4], [form5], [form6], [form7]])

	
	def test_username_registration_form_not_valid_data_false(self, lst):

		self.assertFalse(lst.is_valid())


class TestRegistrationFormsOnPasswordIfTrue(TestCase):

	
	form = RegistrationForm(data={
		'username': 'uqq',
		'password': 'xdvgy432',
		'password_check': 'xdvgy432'
		})

	form1 = RegistrationForm(data={
		'username': 'uqq',
		'password': 'xdvgy4321xdvgy4321',
		'password_check': 'xdvgy4321xdvgy4321'
		})

	form2 = RegistrationForm(data={
		'username': 'uqq',
		'password': 'xdvgy432111',
		'password_check': 'xdvgy432111'
		})

	form3 = RegistrationForm(data={
		'username': 'uqq',
		'password': 'xdvgy43211xdvgy43211xdvgy43211',
		'password_check': 'xdvgy43211xdvgy43211xdvgy43211'
		})

	@parameterized.expand([[form],[form1], [form2], [form3]])

	
	def test_password_registration_form_valid_data_true(self, lst):

		self.assertTrue(lst.is_valid())


class TestRegistrationFormsOnPasswordIfFalse(TestCase):

	form4 = RegistrationForm(data={
		'username': 'uqq',
		'password': 'xdvgy43',
		'password_check': 'xdvgy43'
		})

	form5 = RegistrationForm(data={
		'username': 'uqq',
		'password': 'xdv',
		'password_check': 'xdv'
		})

	form6 = RegistrationForm(data={
		'username': 'uqq',
		'password': 'xdvgy43211xdvgy43211xdvgy432111',
		'password_check': 'xdvgy43211xdvgy43211xdvgy432111'
		})
	form7 = RegistrationForm(data={
		'username': 'u',
		'password': 'xdv'*50,
		'password_check': 'xdv'*50
		})


	@parameterized.expand([[form4], [form5], [form6], [form7]])

	
	def test_password_registration_form_not_valid_data_false(self, lst):

		self.assertFalse(lst.is_valid())



class TestRegistrationFormsOnPasswordCheckIfTrue(TestCase):

	
	form = RegistrationForm(data={
		'username': 'uqq',
		'password': 'xdvgy432',
		'password_check': 'xdvgy432'
		})

	form1 = RegistrationForm(data={
		'username': 'uqq',
		'password': 'xdvgy4321xdvgy4321',
		'password_check': 'xdvgy4321xdvgy4321'
		})

	form2 = RegistrationForm(data={
		'username': 'uqq',
		'password': 'xdvgy432111',
		'password_check': 'xdvgy432111'
		})

	form3 = RegistrationForm(data={
		'username': 'uqq',
		'password': 'xdvgy43211xdvgy43211xdvgy43211',
		'password_check': 'xdvgy43211xdvgy43211xdvgy43211'
		})

	@parameterized.expand([[form],[form1], [form2], [form3]])

	
	def test_password_check_registration_form_valid_data_true(self, lst):

		self.assertTrue(lst.is_valid())


class TestRegistrationFormsOnPasswordCheckIfFalse(TestCase):

	form4 = RegistrationForm(data={
		'username': 'uqq',
		'password': 'xdvgy43',
		'password_check': 'xdvgy43'
		})

	form5 = RegistrationForm(data={
		'username': 'uqq',
		'password': 'xdv',
		'password_check': 'xdv'
		})

	form6 = RegistrationForm(data={
		'username': 'uqq',
		'password': 'xdvgy43211xdvgy43211xdvgy432111',
		'password_check': 'xdvgy43211xdvgy43211xdvgy432111'
		})
	form7 = RegistrationForm(data={
		'username': 'u',
		'password': 'xdv'*50,
		'password_check': 'xdv'*50
		})


	@parameterized.expand([[form4], [form5], [form6], [form7]])

	
	def test_password_check_form_not_valid_data_false(self, lst):

		self.assertFalse(lst.is_valid())


class TestLoginFormsOnUsernameIfTrue(TestCase):
	def setUp(self):
	
		form7 = RegistrationForm(data={
			'username': 'uqq',
			'password': 'xdvgy4321',
			'password_check': 'xdvgy4321'
			})
		new_user7 = form7.save(commit=False)
		username = form7.cleaned_data['username']
		password = form7.cleaned_data['password']
		email = form7.cleaned_data['email']
		first_name = form7.cleaned_data['first_name']
		last_name = form7.cleaned_data['last_name']
		new_user7.username = username
		new_user7.set_password(password)
		new_user7.first_name = first_name
		new_user7.last_name = last_name
		new_user7.email = email
		new_user7.save()

		form4 = RegistrationForm(data={
			'username': 'u'*30,
			'password': 'xdvgy4321',
			'password_check': 'xdvgy4321'
			})
		new_user4 = form4.save(commit=False)
		username = form4.cleaned_data['username']
		password = form4.cleaned_data['password']
		email = form4.cleaned_data['email']
		first_name = form4.cleaned_data['first_name']
		last_name = form4.cleaned_data['last_name']
		new_user4.username = username
		new_user4.set_password(password)
		new_user4.first_name = first_name
		new_user4.last_name = last_name
		new_user4.email = email
		new_user4.save()

		form5 = RegistrationForm(data={
			'username': 'u'*7,
			'password': 'xdvgy4321',
			'password_check': 'xdvgy4321'
			})
		new_user5 = form5.save(commit=False)
		username = form5.cleaned_data['username']
		password = form5.cleaned_data['password']
		email = form5.cleaned_data['email']
		first_name = form5.cleaned_data['first_name']
		last_name = form5.cleaned_data['last_name']
		new_user5.username = username
		new_user5.set_password(password)
		new_user5.first_name = first_name
		new_user5.last_name = last_name
		new_user5.email = email
		new_user5.save()

		form6 = RegistrationForm(data={
			'username': 'u'*15,
			'password': 'xdvgy4321',
			'password_check': 'xdvgy4321'
			})
		new_user6 = form6.save(commit=False)
		username = form6.cleaned_data['username']
		password = form6.cleaned_data['password']
		email = form6.cleaned_data['email']
		first_name = form6.cleaned_data['first_name']
		last_name = form6.cleaned_data['last_name']
		new_user6.username = username
		new_user6.set_password(password)
		new_user6.first_name = first_name
		new_user6.last_name = last_name
		new_user6.email = email
		new_user6.save()

	form = LoginForm(data={
		'username': 'uqq',
		'password': 'xdvgy4321'
		})

	form1 = LoginForm(data={
		'username': 'u'*30,
		'password': 'xdvgy4321'
		})

	form2 = LoginForm(data={
		'username': 'u'*7,
		'password': 'xdvgy4321'
		})

	form3 = LoginForm(data={
		'username': 'u'*15,
		'password': 'xdvgy4321'
		})

	@parameterized.expand([[form],[form1], [form2], [form3]])

	
	def test_username_login_form_valid_data_true(self, lst):

		self.assertTrue(lst.is_valid())



class TestLoginFormsOnUsernameIfFalse(TestCase):

	form = LoginForm(data={
		'username': 'uq',
		'password': 'xdvgy4321'
		})

	form1 = LoginForm(data={
		'username': 'u'*31,
		'password': 'xdvgy4321'
		})

	form2 = LoginForm(data={
		'username': 'u'*50,
		'password': 'xdvgy4321'
		})
	form3 = LoginForm(data={
		'username': 'u',
		'password': 'xdvgy4321'
		})

	@parameterized.expand([[form],[form1], [form2], [form3]])

	
	def test_username_login_form_valid_not_data_false(self, lst):

		self.assertFalse(lst.is_valid())

class TestLoginFormsOnPasswordIfTrue(TestCase):
	def setUp(self):
	
		form7 = RegistrationForm(data={
			'username': 'uqq',
			'password': 'xdvgy432',
			'password_check': 'xdvgy432'
			})
		new_user7 = form7.save(commit=False)
		username = form7.cleaned_data['username']
		password = form7.cleaned_data['password']
		email = form7.cleaned_data['email']
		first_name = form7.cleaned_data['first_name']
		last_name = form7.cleaned_data['last_name']
		new_user7.username = username
		new_user7.set_password(password)
		new_user7.first_name = first_name
		new_user7.last_name = last_name
		new_user7.email = email
		new_user7.save()

		form4 = RegistrationForm(data={
			'username': 'uqqq',
			'password': 'xdvgy4321xdvgy4321',
			'password_check': 'xdvgy4321xdvgy4321'
			})
		new_user4 = form4.save(commit=False)
		username = form4.cleaned_data['username']
		password = form4.cleaned_data['password']
		email = form4.cleaned_data['email']
		first_name = form4.cleaned_data['first_name']
		last_name = form4.cleaned_data['last_name']
		new_user4.username = username
		new_user4.set_password(password)
		new_user4.first_name = first_name
		new_user4.last_name = last_name
		new_user4.email = email
		new_user4.save()

		form5 = RegistrationForm(data={
			'username': 'uqqqq',
			'password': 'xdvgy432111',
			'password_check': 'xdvgy432111'
			})
		new_user5 = form5.save(commit=False)
		username = form5.cleaned_data['username']
		password = form5.cleaned_data['password']
		email = form5.cleaned_data['email']
		first_name = form5.cleaned_data['first_name']
		last_name = form5.cleaned_data['last_name']
		new_user5.username = username
		new_user5.set_password(password)
		new_user5.first_name = first_name
		new_user5.last_name = last_name
		new_user5.email = email
		new_user5.save()

		form6 = RegistrationForm(data={
			'username': 'uqqqqq',
			'password': 'xdvgy43211xdvgy43211xdvgy43211',
			'password_check': 'xdvgy43211xdvgy43211xdvgy43211'
			})
		new_user6 = form6.save(commit=False)
		username = form6.cleaned_data['username']
		password = form6.cleaned_data['password']
		email = form6.cleaned_data['email']
		first_name = form6.cleaned_data['first_name']
		last_name = form6.cleaned_data['last_name']
		new_user6.username = username
		new_user6.set_password(password)
		new_user6.first_name = first_name
		new_user6.last_name = last_name
		new_user6.email = email
		new_user6.save()

	form = LoginForm(data={
		'username': 'uqq',
		'password': 'xdvgy432'
		})

	form1 = LoginForm(data={
		'username': 'uqqq',
		'password': 'xdvgy4321xdvgy4321'
		})

	form2 = LoginForm(data={
		'username': 'uqqqq',
		'password': 'xdvgy432111'
		})

	form3 = LoginForm(data={
		'username': 'uqqqqq',
		'password': 'xdvgy43211xdvgy43211xdvgy43211'
		})

	@parameterized.expand([[form],[form1], [form2], [form3]])

	
	def test_password_login_form_valid_data_true(self, lst):

		self.assertTrue(lst.is_valid())


class TestLoginFormsOnPasswordIfFalse(TestCase):

	form4 = LoginForm(data={
		'username': 'uqq',
		'password': 'xdvgy43'
		})

	form5 = LoginForm(data={
		'username': 'uqq',
		'password': 'xdv'
		})

	form6 = LoginForm(data={
		'username': 'uqq',
		'password': 'xdvgy43211xdvgy43211xdvgy432111'
		})
	form7 = LoginForm(data={
		'username': 'u',
		'password': 'xdv'*50
		})


	@parameterized.expand([[form4], [form5], [form6], [form7]])

	
	def test_password_form_not_valid_data_False(self, lst):

		self.assertFalse(lst.is_valid())