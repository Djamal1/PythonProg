class Cats:
	def __init__(self, name, paws, eyes, tail, ear):
		self.name = name
		self.paws = paws
		self.eyes = eyes
		self.tail = tail
		self.ear = ear

	@property
	def my_paws(self):
		return "У меня " + str(self.paws) + " лапки... ((("

	@my_paws.setter
	def my_paws(self, value):
		self.paws = value + ". Я бы дал тебе по лицу! Но у меня ЛАПКИ!!!"


maine_coon = Cats("Мейкун", 2, 2, 1, 2)

print(maine_coon.my_paws)
maine_coon.my_paws = "2 лапки!!!!!"
print(maine_coon.my_paws)


print()


class Cats:
	def __init__(self, name, paws, eyes, tail, ear):
		self.name = name
		self.paws = paws
		self.eyes = eyes
		self.tail = tail
		self.ear = ear

	@property
	def my_eyes(self):
		return "У меня " + str(self.eyes) + " глаза! И это главное!"

	@my_eyes.setter
	def my_eyes(self, value):
		self.eyes = value + ". Жаль что не четыре глаза((("


maine_coon = Cats("Мейкун", 2, 2, 1, 2)

print(maine_coon.my_eyes)
maine_coon.my_eyes = "2 глаза!!!!!"
print(maine_coon.my_eyes)


print()


class Cats:
	def __init__(self, name, paws, eyes, tail, ear):
		self.name = name
		self.paws = paws
		self.eyes = eyes
		self.tail = tail
		self.ear = ear

	@property
	def my_tail(self):
		return "У меня " + str(self.tail) + " хвост. Этого достаточно что-бы убить армию солдат!"

	@my_tail.setter
	def my_tail(self, value):
		self.tail = value + ". Повезло мне с хвостом!"


maine_coon = Cats("Мейкун", 2, 2, 1, 2)

print(maine_coon.my_tail)
maine_coon.my_tail = "1 хвост"
print(maine_coon.my_tail)


print()


class Cats:
	def __init__(self, name, paws, eyes, tail, ear):
		self.name = name
		self.paws = paws
		self.eyes = eyes
		self.tail = tail
		self.ear = ear

	@property
	def my_ear(self):
		return "У меня " + str(self.ear) + " уха. Они нужны что-бы слышать"

	@my_ear.setter
	def my_ear(self, value):
		self.ear = value + ". Уши для того что-бы слышать! (И всё, кек)"


maine_coon = Cats("Мейкун", 2, 2, 1, 2)

print(maine_coon.my_ear)
maine_coon.my_ear = "2 уха"
print(maine_coon.my_ear)