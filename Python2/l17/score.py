class Users():
	def __init__(self, login, password, email, happy):
		self.login = login
		self.password = password
		self.email = email
		self.happy = happy
	def register(self, users_list):
		if self.login in users_list:
			print("Такой пользователь уже существует")
		else:
			users_list[self.login] = self.password
			users_list[self.email] = self.happy
			print("Вы успешно зарегестрировались")

	def aythorize(self, users_list):
		if self.login in users_list:
			print('Успешная авторизация')
		else:
			print('Такой пользователь не существует')
			choice = input('1) Попробовать ещё раз, 2) Создать новый аккаунт:  ')
			if choice == '1':
				aythorize(users_list)
			elif choice == '2':
				register(users_list)

def work(users_list):
		exit = 0
		choic = input('1) Войти, 2) Регистрация, 3) Выход:  ')
		if choic == '1':
			user = Users(input('Введите логин:  '), input('Введите пароль:  '))
			user.aythorize(users_list)
		elif choic == '2':
			user = Users(input('Введите логин:  '), input('Введите пароль:  '), input('Введите электронную почту:  '), input('Введите дату рождения:  '))
			user.register(users_list)
		elif choic == "3":
			f = open("users.txt" , "a")
			for i in users_list.keys():
				f.write(i+"-"+users_list[i] + ", ")
			exit = 1
			f.close()
		else:
			print("Ты поступаешь плохо (((((((")
		return exit

users_list = {}

while True:
	i = work(users_list)
	print(users_list)
	if i == 1:
		break


class Score(Users):
	def __init__(self, name, basket, products):
		self.name = name
		self.basket = basket
		self.products = products

	def add_basket(self, product_list):
		if self.basket in product_list:
			print("Вы уже добавили данный товар, больше нельзя!")
		else:
			product_list[self.products] = self.basket
			print("Вы успешно добавили товар в корзину!")
			print("Купить данный товар?  ")
			buy_product = input("1 - Да, 2 - нет:  ")
			if buy_product == '1':
				print("Вы заказали свой товар, ждите!!")
			elif buy_product == '2':
				print("Ну как хотите!")

	def buy(self, product_list):
		if self.products in product_list:
			print("Успешная покупка товара!!! К вам скоро его привезёт курьер!!!")
		else:
			print("Данный товар закончился ((((")
			buy_product = input('1) Выбрать другой товар?, 2) Ограбить магазин?:  ')
			if buy_product == '1':
				buy(product_list)
			elif buy_product == '2':
				print("Вы подскользнулись и ударились головой, и встали и узнали что вы мертвы!! ((((")

def goods(product_list):
		exit = 0
		print("Добро пожаловать в интернет магазин! Что вы хотите?:  ")
		buy_prod = input('1) Купить добовляя в корзину?, 2) Купить сразу, не добавляя в корзину?, 3) Выход:  ')
		if buy_prod == '2':
			scor = Score(input('1 - Iphone X, 2 - Гироскутер, 3 - Samsung galaxy S8, 4 - BMW Z1, 5 - Телевизор LG:  '),\
input("Купить?  "), input("Введите пароль:  "))
			scor.buy(product_list)
		if buy_prod == '1':
			scor = Score(input('1 - Iphone X, 2 - Гироскутер, 3 - Samsung galaxy S8, 4 - BMW Z1, 5 - Телевизор LG:  '), input('Добавить корзину?  '), input('Гооооо?  '))
			scor.add_basket(product_list)
		elif buy_prod == "3":
			z = open("products.txt" , "a")
			for l in product_list.keys():
				z.writte(l + ", " + product_list[l])
				exit = 1
				z.close()
		else:
			print("NOOOOOOOOOO!!!!!!!")
		return exit


product_list = {}

while True:
	l = goods(product_list)
	print(product_list)
	if l == 1:
		break