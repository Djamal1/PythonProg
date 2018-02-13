def ride(car):
	car["distance"] += car["speed"]
	car["fuel"] -= car["spend"]

def faster(car):
	car["speed"] += 10
	car["spend"] += 8

def fuel(car):
	car["distance"] += car["fuel"]
	car["distance"] -= car["speed"]

def fuel1(car):
	car["fuel"] += 20
	car["speed"] -= 10

def nitro(car):
	car["distance"] += car["nitro"]
	car["fuel"] -= car["spend"] * 3


def car_info(car):
	print("\n Текущее состояние:", 
		"Топливо: " + str(car["fuel"]),
		"Скорость: " + str(car["speed"]),
		"Нитро: " + str(car["nitro"]),
		"Проехали: " + str(car["distance"]) + "/" + str(track)
		)


def race_step(car):
	choose = input("Твой ход, " + car["name"] + " Выбери вариант:\n 1 - Прибавляет скорость, 2 - Даёт нитро, 3 - Прибавляет топливо: ")


	if choose == "1":
		ride(car)
	elif choose == "2":
		faster(car)
	elif choose == "3":
		fuel1(car)
	else:
		nitro(car)

	car_info(car)

	input()

	cars = input("1 - Mercedes, 2 - BMW, 3 - Ferrari: ")
	
	cars = dict()

	if cars == "1":
		car1["Mercedes"] = "Mercedes"
	elif cars == "2":
		car2["BMW"] = "BMW"
	elif cars == "3":
		car3["Ferrari"] = "Ferrari"

car1 = {
	"name": "Mercedes",
	"speed": 12,
	"fuel": 100,
	"spend": 3,
	"nitro": 5,
	"distance": 0
}

car2 = {
	"name": "BMW",
	"speed": 9,
	"fuel": 100,
	"spend": 2,
	"nitro": 4,
	"distance": 0
}

car3 = {
	"name": "Ferrari",
	"speed": 15,
	"fuel": 100,
	"spend": 4,
	"nitro": 7,
	"distance": 0
}

track = 100

while True:
	race_step(car1)
	race_step(car2)
	race_step(car3)