f = open("KEK.txt", "r")
my_list = f.read().split(", ")
print(my_list)
l = 1 
for i in my_list:
	print(l, i)
	l += 1