file = open("New_file.txt", "w")
file.write("Новая запись!")
file.close()
file = open("New_file.txt", "r")
print("LOLOLOL", file.read())
file.close()
file = open("New_file.txt", "a")
name_list = ["Обама", "Путин", "Кто-то"]
i = 1
for name in name_list:
	file.write("\n" + str(i) + ": " + name)
	i += 1
file.close()
file = open("New_file.txt", "r+")
print("Состав группы: ")
for name in file:
	print(name)
file.close()