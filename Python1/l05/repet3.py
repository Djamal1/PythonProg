a = "У лукоморья дуб зелёный"
print(a)
print(a[2])
b = ["Арамен", "человек шашлык", "тор"]
print(b[0])
# b.append(input("Добавь нового персанажа: "))
print(b)
b.insert(2, "Халк")
print(b)
del b[1]
print(b)
b.remove("Арамен")
print(b)
jl = ["Флеш","Аквамен"]
b.extend(jl)
print(b)