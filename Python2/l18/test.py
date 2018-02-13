# my_test = "Один, два, три."
# print(my_test.split(", "))

f = open("List_of_users.txt", "r")
for i in f:
	print(i.split(" : ")[1])
	print("Мяу" == i.split(" : ")[1])