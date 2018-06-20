import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


m = float(input('Введіть магнітуру:'))

if m <= 2:
    print ('Мікро')
elif m >= 2 and m <= 3:
    print ('Дуже слабкий')
elif m >= 3 and m <= 4:
    print ('Слабкий')
elif m >= 4 and m <= 5:
    print ('Легкий')
elif m >= 5 and m <= 6:
    print ('Помірний')
elif m >= 6 and m <= 7:
    print ('Сильний')
elif m >= 7 and m <= 8:
    print ('Дуже сильний')
elif m >= 8 and m <= 10:
    print ('Великий')
else:
    print ('Рідкісно великий')
