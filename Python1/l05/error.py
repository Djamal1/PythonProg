week = ("Monday","Tuesday","Wednesday") # Кортеж
print(week)
week2 = "Thursday", "Friday"
# week3 = "Saturday",
# print(week3)
# full_week = []
# full_week += week
# print(full_week)
a, b = week2
print(a, b)
x, y, z = "ПН", "ВТ", "СР"
print(x, y, z)

pupils = {"Карл Маркс", "Альберт Эйнштейн",\
 "Султанмурад", "Ч. Дарвин", "Карл Маркс"}
print(pupils)
if "Карл Маркс" in pupils:
	print("Карл Маркс победил!! Коммунизм по всей планете!")
else:
	print("Забудь о коммунах!")

madteam = {"Карл Маркс", "Альберт Эйнштейн",\
 "Джон Нэш", "Дональд Трамп", "Мальчик ракета"} # Множество
print(pupils & madteam) # Пересечение
print(pupils | madteam) # Обьединение
print(pupils - madteam) # Вычитание
print(madteam - pupils)

print("-" * 50)

films = {
	"Люся": "Люся получает супермозг",
	"Безумный Маркс": "Земля превратилась в пустыню - куммунизм победил",
	"Защитники": "Наш ответ Западу! Медведь, узбек, казах, деваха-невидимка - суперскуад",
}
print(films["Защитники"])
films["Люся"] = "Люся теряет костный мозг"
print(films)
films[7] = "Жестокий фильм про семь смертных грехов"
print(films[7])
films["Человек-паук 1", "Второй человек-паук"] = ["Слив", "Шлак", "Дядя Бен!!!!"]
print(films["Человек-паук 1", "Второй человек-паук"])

for key in films: # Перебор по ключу
	print(key)
	if key =="Люся":
		print("Позор!!")

for description in films.values(): # Перебор по значению
	print(description)

for name, desc in films.items(): # Перебор по парам - ключу и значению
	print("Фильм" + str(name) + ". Описание: " + str(desc))