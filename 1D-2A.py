a = float(input('Введіть ваш зріст: '))
b = float(input('Введіть вашу вагу: '))

print ("""
Виберіть формулу обчислення індексу маси тіла:

[1] - дюйми та фунти
[2] - метри та кілограми
""")

choose = int(input('Оберіть формулу обчислення: '))
if choose == 1:
    a = a**2
    imt = b/a
    imt = 703*imt
    print ('Ваш imt: ', imt)
else:
    a = a**2
    imt = b/a
    print ('Ваш imt: ', imt)
import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Третяк Артур')