ff = open("KEK.txt", "w")
my_list = ["Киркоров,", " Басков, ", " Майкл, ", " Менсен"]
for n in my_list:
	ff.write(n)
ff.close()
ff = open("KEK.txt", "a")
ff.write(", Дима Билан.")