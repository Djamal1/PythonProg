class Guns:
	def __init__(self, name, shot_range, calibre, holder, hammer):
		self.name = name
		self.shot_range = shot_range
		self.calibre = calibre
		self.holder = holder
		self.hidden_hammer = hammer


	# Первый способ описания геттера и сеттера.

	# def show_hammer(self):
	# 	# return "Это информация засекречена!! Даже не думай!"
	# 	return self.hidden_hammer

	# def change_hammer(self, value):
	# 	# print("Нельзя менять!!!! Руки прочь!!")
	# 	self.hidden_hammer = value

	# hammer = property(show_hammer, change_hammer) # геттер и сеттер


	# Второй способ описания геттера и сеттера.

	@property
	def my_calibre(self):
		return "Мой калибр " + self.calibre

	@my_calibre.setter
	def my_calibre(self, value):
		self.calibre = value + " Навальный!"


railgun = Guns("Рельсотрон", 200000, "100x200", 1, "USA")
# print(railgun.hammer)
# railgun.hammer = "MotherRussia"

print(railgun.my_calibre)
railgun.my_calibre = "200x400"
print(railgun.my_calibre)