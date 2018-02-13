class Guns:
	def __init__(self, name, shot_range, calibre, holder):
		self.name = name
		self.shot_range = shot_range
		self.__calibre = calibre
		self.holder = holder

	def check_calibre(self):
		print(self.__calibre)

def shot(weapon):
	print("БА-БАХ!")
	weapon.holder -= 1
	print("В обойме осталось " + str(weapon.holder) + " патронов")

def modify_weapon(weapon):
	weapon.__calibre = "9x30"
	print("Калибр оружия изменен на " + weapon.__calibre)
	print("Настоящий калибр " + weapon._Guns__calibre)

glock = Guns("Глок", 50, "9x19", 17)
shot(glock)
modify_weapon(glock)
glock.check_calibre()