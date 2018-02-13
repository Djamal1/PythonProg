buys = ["Хлеб", "Молоко", "телевизор Bosh"]
print(buys[0])
print(buys[-1])
print(buys[::])
buys.append("Маска")
print(buys)
buys.insert(2, "Маска")
another_buys = ["Холодильник", "чай"]

buys.extend(another_buys)
print(buys)

del buys[1]
print(buys)

buys.remove("чай")
print(buys)
print(buys.pop(2))

print(buys)

buys2 = buys
del buys[2]
print(buys)
print(buys2)