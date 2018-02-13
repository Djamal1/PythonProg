class Sheros:
	def __init__(self, name, superpower, archenemy):
		self.name = name
		self.superpower = superpower
		self.archenemy = archenemy

	def superpunch(self):
		print(self.name + " Нанёс страшнейший удар" + self.superpower + ", И взрывная волна разошлась по всему миру!!!")


class Watermelon:
	def __init__(self, name, weight, diametr):
		self.name = name
		self.weight = weight
		self.diametr = diametr

	def superpunch(self):
		print(self.name + " Накатился всеми своими силами " + str(self.weight) + "Накатился так что весь мир умер!")
	

tor = Sheros("Тор-браузер", 
	" Пробивает молотом блок Роскомнадзора", "ФСБ")
aquaman = Sheros("Аква-мем", "мехотворный удар, призвал пса Дратути, вытащил рисунок суперспособности","Дружко")

def strike(hero):
	return hero.superpunch()

arboozman = Watermelon("Петрович", 320000, 1)



strike(tor)
strike(aquaman)
strike(arboozman)