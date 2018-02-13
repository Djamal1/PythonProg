# a = ""
a = "Переправа, переправа, берег левый, берег правый."
print(a)
print(a[0])
print(a[-3])
print(a[0:9])
print(a[28:33])
print(a[35:])
print(a[-12:-1])
print(a[::2])
print(a[:9:3])
print(a[::-1])

print(len(a))
b = "   "
print(len(b))

print(a.upper())
print(a.lower())
print(a.title())
print(a.count("берег"))
print(a.find("берег"))
print(a.rfind("берег"))
print(a.count("Переправа"))

print(a.lower().count("переправа"))
print(a.replace("берег", "Крекер"))