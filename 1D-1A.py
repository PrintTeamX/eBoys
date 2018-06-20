import datetime
print("Введіть число контейнера")
print("Ведіть число контейнерів до 1л.: ")
a = int(input())
print("Ведіть число контейнерів більше 1л.: ")
b = int(input())
e1 = a * 0.1
e2 = b * 0.25
e3 = e1 + e2
print("Гроші за контейнери до 1л.: $",+ e1)
print("Гроші за контейнери більше 1л.: $",+ e2)
print("Разом: $",+ e3)

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Артур Третяк"

printTimeStamp(name)
