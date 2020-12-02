from django import forms
from django.utils import timezone
from django.contrib.auth.models import User




class LoginForm(forms.Form):

	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	
	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)
		self.fields['username'].label = 'Логин'
		self.fields['password'].label = 'Пароль'


	def clean(self):
		username = self.cleaned_data['username']
		password = self.cleaned_data['password']
		if len(username) < 3:
			raise forms.ValidationError('Логин слишком короткий')
		if len(username) >30:
			raise forms.ValidationError('Логин слишком длинный')
		if not User.objects.filter(username=username).exists():
			raise forms.ValidationError('Пользователь с таким логином не зарегистрирован')
		user = User.objects.get(username=username)
		if len(password) > 30:
			raise forms.ValidationError('Пароль слишком длинный')
		if len(password) < 8:
			raise forms.ValidationError('Пароль слишком короткий')
		if user and not user.check_password(password):
			raise forms.ValidationError('Неверный пароль')



class RegistrationForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	password_check = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = [
			'username',
			'password',
			'password_check',
			'first_name',
			'last_name',
			'email'
		]


	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)
		self.fields['username'].label = 'Логин'
		self.fields['password'].label = 'Пароль'
		self.fields['password'].help_text = 'Придумайте пароль'
		self.fields['first_name'].label = 'Имя'
		self.fields['last_name'].label = 'Фамилия'
		self.fields['email'].label = 'Ваша почта'
		self.fields['email'].help_text = 'Пожалуйста указывайте реальный Адрес'
		self.fields['password_check'].label	 = 'Повторите пароль'


	def clean(self):
		username = self.cleaned_data['username']
		password = self.cleaned_data['password']
		password_check = self.cleaned_data['password_check']
		if User.objects.filter(username=username).exists():
			raise forms.ValidationError('Пользователь с таким логином уже зарегистрирован')
		if len(username) < 3:
			raise forms.ValidationError('Логин слишком короткий')
		if len(username) >30:
			raise forms.ValidationError('Логин слишком длинный')
		if password != password_check:
			raise forms.ValidationError('Пароли не совпадают')
		if len(password) > 30:
			raise forms.ValidationError('Пароль слишком длинный')
		if len(password) < 8:
			raise forms.ValidationError('Пароль слишком короткий')




class OrderForm(forms.Form):
	
	name = forms.CharField(max_length=30)
	last_name =  forms.CharField(required=False, max_length=100)
	phone = forms.CharField(max_length=8)
	buying_type = forms.ChoiceField(widget=forms.Select(), choices=([("self", "Самовывоз"), ("delivery", "Доставка")]))
	date = forms.DateField(widget=forms.SelectDateWidget(), initial=timezone.now())
	address = forms.CharField(required=False, max_length=100)
	comments = forms.CharField(widget=forms.Textarea, required=False, max_length=100)


	def __init__(self, *args, **kwargs):
		super(OrderForm, self).__init__(*args, **kwargs)
		self.fields['name'].label = 'Имя'
		self.fields['last_name'].label = 'Фамилия'
		self.fields['phone'].label = 'Контактный телефон'
		self.fields['phone'].help_text = 'Пожалуйста, указывайте реальный номер телефона, по которому с вами можно связаться'
		self.fields['buying_type'].label = 'Способ получения'
		self.fields['address'].label = 'Адресс доставки'
		self.fields['address'].help_text = '*обязательно указывайте город'
		self.fields['comments'].label = 'Комментарии к заказу'
		self.fields['date'].label = 'Дата доставки'
		self.fields['date'].help_text = 'Доставка производится на следующий день после оформления заказа. Менеджер с вами свяжется'


