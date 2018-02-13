class Secret_info:
	def __init__(self, data):
		self.__data = data
		self.secret_parols = parols


	def get_secret_parols(self):
		return secret_parols

	def get_secret_parols(self, new_information):
		self.secret_parols = new_information

	self.parols = property(get_secret_parols, set_secret_parols)

my_doc = Secret_info("2*2=4")

print(my_doc._Secret_info__data)