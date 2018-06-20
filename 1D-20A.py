import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

a = int(input('Введіть кількість буханок вчорашього хліба: '))
b = 8.50
c = 60
d = b * a * (c / 100)

print('Кількість буханок вчорашнього хліба: ' + str(a))
print('Звичайна вартість товару: ' + str(b))
print('Знижка: ' + str(c))
print('Загальна сума покупки: ' + str(d))