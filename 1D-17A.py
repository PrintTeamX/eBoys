import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

a = int(input("Введіть суму: "))
a1 = (a * 0.14) + a
a2 = (a1 * 0.14) + a1
a3 = (a2 * 0.14) + a2
print("Рік 1: " + str(a1))
print("Рік 2: "+ str(a2))
print("Рік 3: " +str(a3))