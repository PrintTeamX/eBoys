import datetime

summ = 0
while True:
    try:
        x = input()
        if x == '':
            break
        summ += int(x)
        print("Сума: " + str(summ))
    except:
        print("Введите коректні дані: ")
        print("Сума: " + str(summ))
print("Сума: " + str(summ))

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Team X")