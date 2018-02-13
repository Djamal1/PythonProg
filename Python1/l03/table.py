import random

print("Реши пример!!!")
number1 = random.randint(0, 100)
number2 = random.randint(0, 1000) # случайное число
answer = int(input("Увеличь " + str(number1) \
	+ " на " + str(number2) + " = "))

if (answer == number1 + number2):
	print("Молодец. Ты всё правильно решил! :)")
else:
	print("Неправильно!! :(")