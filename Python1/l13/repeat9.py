class Car:
	def __init__(self, color, firm):
		self.color = color
		self.firm = firm

	def signal (self):
		print("Бим, бим, бим")

volga = Car("Красный", "Газ")
volga.signal()
# Car.signal(volga):
print(volga)

class Cargo_car(Car):
	def __init__(self, color, firm, carring):
		super().__init__(color, firm)
		self.carring = carring

	def signal(self):
		print("ТА-ДАААААААМ!!!")

belaz = Cargo_car("Жёлтый", "Белаз", 450000)
belaz.signal()