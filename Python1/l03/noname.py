weight = int(input("Введи свой вес, dude: "))

if (weight == 20):
	print("Тебя сдувает порывом ветра")
elif (weight < 20):
	print("Лифт не реагирует на тебя")
elif (weight > 20 and weight < 30):
	print("Можешь кататься на кошках")
elif (weight > 30 and weight < 40):
	print("Тебя выдержит собака")
elif (40 < weight < 50):
	print("Ты король ящериц!")
elif (weight == 66 or weight > 300):
	print("Ты пораждение ада")
elif (weight >= 70 and weight != 80):
	print("Ты турникмен!")
else:
	print("Ты шварц!!")