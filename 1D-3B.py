import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

s1 = []
s = []
while True:
    a = int(input('Введіть значення в Цельсіях (введіть 1 щоб перестати вводити значення): '))
    s1.append(a)
    b = a % 10
    if b == 0 and a >= 0 and a <= 100:
        c = a * 9/5 + 32
        s.append(c)
    elif a == 1:
        break
    else:
        print('Помилка')
for i in range(len(s)):
    print('{0} °C       ==>       {1} ºF'.format(s1[i], s[i]))
