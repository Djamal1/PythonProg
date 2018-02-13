week = ("Английский словарь: ")
print(week)

x = "A: "
print(x)

print("academic - академический")
print("accept - допускать")
print("acceptable - допустимый")
print("access - доступ")
print("accident - авария")
print("accommodation - помещение")
print("accompany - сопровождать")
print("according - соответствие")
print("accordingly - соответственно")
print("account - счет")
print("accountant - бухгалтер")
print("accurate - верный, правильный")
print("achieve - достигать")

print("-" * 70)

y = "B: "
print(y)

print("baby - дитя")
print("back - назад; спина")
print("background - фон")
print("backwards - назад")
print("bad - плохой")
print("badly - плохо")
print("bag - сумка")
print("baggage - багаж")
print("bake - выпекать")
print("balance - баланс")
print("balcony - балкон")
print("ball - мяч")

print("-" * 70)

z = "C: "
print(z)

print("cabinet - кабинет министров; шкаф")
print("cable - канат; трос")
print("cafe - кафе")
print("cage - клетка")
print("cake - кекс, пирожное, торт")
print("calculate - вычислять")
print("calculation - вычисление")
print("call - звонок; звать, звонить, называться")
print("calm - спокойный")
print("camera - фотоаппарат")
print("camp - лагерь")
print("campaign - кампания")

print("-" * 70)

a = "D: "
print(a)

print("dad - папа")
print("daily - ежедневный")
print("damage - вред , вредить")
print("dance - танец, танцевать")
print("danger - опасность")
print("dangerous - опасный")
print("dare - сметь")
print("dark - темный")
print("darkness - темнота")
print("data - данные")
print("database - база данных")
print("date - дата, датировать")

print("-" * 70)

s = "E: "
print(s)

print("each - каждый")
print("ear - ухо")
print("early - рано")
print("earn - зарабатывать")
print("earth - земля")
print("easily - легко")
print("east - восток")
print("eastern - восточный")
print("easy - легкий")
print("eat - кушать")
print("economic - экономический")
print("economics - экономика")

print("_" * 70)


m = "Мои любимые мульты: "
print(m)

print("1. Гравити Фолз")

films = {
	"Гравити Фолз": "↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓",
}

print(films["Гравити Фолз"])
films["Гравити Фолз"] = "Главные герои: Диппер, Мейбл, Зус, дядя Стен и т.д."
print(films)
films["Гравити Фолз"] = ["Приключение", "наука", "интрига"]
print(films["Гравити Фолз"])

print("Возрастное ограничение: 12+")

for name, desc in films.items():
	print("" + str(name) + ". → → → Описание мультика: Мульт очень интересный! \
Где Диппер с Мейбл изучают Гравити Фолз. " + str(desc))

print("-" * 70)

print("2. Время приключений")

films = {
	"Время приключений": "↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓",
}

print(films["Время приключений"])
films["Время приключений"] = "Главные герои: Финн, Джейк, Бимо и многие другие."
print(films)
films["Время приключений"] = ["Приключение", "драки", "интрига"]
print(films["Время приключений"])

print("Возрастное ограничение: 12+")

for name, desc in films.items():
	print("" + str(name) + ". → → → Описание мультика: Финн и Джейк путешествуют по всему миру и убивают монстров, спасают принцесс \
и помогают тем кому нужна помощь. " + str(desc))

print("_" * 80)