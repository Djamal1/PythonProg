import random

def create_player():
	player = {"HP": 100, "Урон": 10, "Щит": 20}
	player["Имя"] = input("Введи ник, бойца: ")
	choose = input("1 - Увеличить HP, 2 - Увеличить Урон, 3 - Поставить Щит: ")
	if choose == "1":
		player["HP"] += 50
	if choose == "2":
		player["Щит"] += 40
	else:
		player["Урон"] += 5
	return player

def show_health(player):
	print("Количество жизней игрока: ", player["Имя"], player["HP"])
def show_shit(player):
	print("Количество жизней у щита: ", player["Имя"], player["Щит"])

def attack(attacker, victim):
	damage = random.randint(attacker["Урон"]-3, attacker["Урон"]+5)
	print(attacker["Имя"], ", Нанёс ", damage, "едениц урона")
	victim["HP"] -= damage

def attack(attacker, shit):
	damage = random.randint(attacker["Урон"]-3, attacker["Урон"]+5)
	print(attacker["Имя"], ", Нанёс ", damage, "едениц урона")
	shit["Щит"] -= damage



player1 = create_player()
player2 = create_player()

while True:
	attack(player1, player2)
	attack(player2, player1)

	show_health(player1)
	show_health(player2)

	show_shit(player1)
	show_shit(player2)

	input()

	if player1["Щит"] <= 0:
		print(player1["Имя"], "Щит сломан!")

	if player2["Щит"] <= 0:
		print(player2["Имя"], "Щит сломан!")


	if player1["HP"] <= 0:
		print(player2["Имя"], "Выйграл!!")
		break

	if player2["HP"] <= 0:
		print(player1["Имя"], "Выйграл!!")
		break