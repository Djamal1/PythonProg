import random

player1 = {"Счёт": 1000}
player2 = {"Счёт": 1000}

player1["Имя"] = input("Введите имя первого игрока: ")
player2["Имя"] = input("Введите имя второго игрока: ")

while True:
	player1["Ставка"] = int(input("Введите ставку: "))
	player2["Ставка"] = int(input("Введите ставку: "))

	player1["Бросок"] = random.randint(1, 12)
	player2["Бросок"] = random.randint(1, 12)
	print(player1)
	print(player2)

	if player1["Бросок"] > player2["Бросок"]:
		print(player1["Имя"], "Выйграл ставку!!!")
		player1["Счёт"] += player2["Ставка"]
		player2["Счёт"] -= player2["Ставка"]

	if player2["Бросок"] > player1["Бросок"]:
		print(player2["Имя"], "Выйграл ставку!!!")
		player2["Счёт"] += player1["Ставка"]
		player1["Счёт"] -= player1["Ставка"]

	else:
		print("Ничья")
	print(player1["Имя"], player1["Счёт"])
	print(player1["Имя"], player1["Счёт"])

	elif player1["Счёт"] <= 0:
		print(player2["Имя"], "Проиграл!")
		break

	elif player2["Счёт"] <= 0:
		print(player2["Имя"], "Проиграл!")
		break
