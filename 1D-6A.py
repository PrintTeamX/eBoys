import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))


a = float(input("Введіть рахунок за їжу: "))
b = a * 0.14
c = a * 0.18
d = b + c + a
print("Чайові: " + str(b))
print("Податок: " + str(c))
print("Разом: " + str(d))