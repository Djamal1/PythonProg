# guests = input("Введите список пришедших гостей: ")
# print(guests)
# list_of_guests = guests.split(", ")
# print(list_of_guests[0])

# final_guests = " Любит ".join(list_of_guests)
# print(final_guests)

# numbers = input("Введите числа: ")
# numbers_list = numbers.split(" ")

# print(numbers_list)

# n = 0
# for i in numbers_list:
# 	numbers_list[n] = int(i)
# 	n += 1

# print(numbers_list)

# print(len(numbers_list)) # длина списка
# print(min(numbers_list)) # самый маленький элемент списка
# print(max(numbers_list)) # самый большой элемент списка

# numbers2 = [20, 15, 21, 99]

# guess = int(input("Отгадай число: "))

# # print(guess in numbers2)

# if guess in numbers2:
# 	print("Ты чёртов экстрасенс!")
# else:
# 	print("Ты облажался, парень!")

# numbers3 = {5: "пять", 10: "десять", 15: "девять", 20: "нуль"}
# if guess in numbers3:
# 	print("Урра, словарь!!!")


# numbers4 = (10, 14, 22, 33)
# for i in numbers4:
# 	print(i)


# numbers5 = {10, 14, 22, 33}
# for i in numbers5:
# 	print(i)


# numbers6 = {5: "пять", 10: "десять", 15: "девять", 20: "нуль"}
# for i in numbers6: #перебор по ключам
# for i in numbers6.values(): # перебор по значениям
# for i in numbers6.items(): # перебор по парам
# 	print(i)

numbers = 10
if numbers in range(0, 50):
	print("Попал")


# for i in range(0, 10, 2):
#	print(i)