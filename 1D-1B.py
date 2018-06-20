a = float(input("Введіть тиск: "))
b = float(input("Об'єм: "))
c = float(input("Температура: "))
f = 8.314
b3 = b/1000
g = c + 273.15
n = (a*b3)/(f*g)
print("Молярна маса газу:" + str(n))
