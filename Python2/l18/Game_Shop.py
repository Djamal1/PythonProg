class Users:
	def __init__(self, login, password):
		self.login = login
		self.password = password

	def register(self):
		f = open("List_of_users.txt", "r")
		for log in f:
			if self.login == log.split(": ")[0]:
				print("Пользователь с таким логином уже существует")
				break
		else:
			f = open("List_of_users.txt", "a")
			f.write(self.login + ": " + self.password + "\n")
			f.close()
		f.close()

	def autorize(self):
		f = open("List_of_users.txt", "r")
		for log in f:
			if self.login == log.split(": ")[0] and self.password == log.rstrip("\n").split(": ")[1]:
				print("Вы успешно авторизовались")
				break
		else:
			print("Пользователь не найден")
			choice = input("1 - Ввести данные снова\n2 - Зарегистрироваться: ")
			if choice == "1":
				self.autorize()
			elif choice == "2":
				self.register()
			else:
				print("Ты плохой!")
		f.close()

def show_prod():
	f = open("Game_of_list.txt", "r")
	print("Список наших товаров:")
	for prod in f:
		print(prod.rstrip("\n"))
	f.close()

def make_a_shop(user):
	f = open("Game_of_list.txt", "r")
	new_f = open("Basket.txt","w")
	new_f.write(user.login + ": ")
	game = input("Для совершения покупки введите название игры: ")
	for shop_game in f:
		if game == shop_game.split(": ")[0]: 
			new_f.write(shop_game + '\n')
			print("Товар добавлен в корзину")
			break
	else:
		print("Такой игры в магазине нет!")
	f.close()
	new_f.close()

user = Users(input("Введите логин: "), input("Введите пароль: "))
#user.register()
#user.autorize()
show_prod()
make_a_shop(user)