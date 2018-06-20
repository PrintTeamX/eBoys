import math
a = int(input("Введіть 1 число: "))
b = int(input("Введіть 2 число: "))

e1 = a + b
e2 = b - a
e3 = a * b
e4 = a // b
e5 = a % b
e6 = math.log10(a)
e7 = a**b
print("Сума: ",+ e1)
print("Різниця: ",+ e2)
print("Добуток: ",+ e3)
print("Частка: ",+ e4)
print("Остача:",+ e5)
print("Значення log10a: ",+ e6)
print("Значення a^b: ",+ e7)