import datetime
print("Обирайте яку кількість товарів ви хочете купити:")
print("Скільки 'Штучки'?")
a = int(input())
print("Скільки 'Штукенції'?")
b = int(input())
x1 = a * 0.075
x2 = b * 0.112
x3 = x1 + x2 
print("Загальна маса замовлення: ", x3,"Kr")

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Артур Третяк"

printTimeStamp(name)
