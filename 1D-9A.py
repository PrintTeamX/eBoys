import datetime
print("Введіть роки вашого життя: ")
a = float(input())
def breaku():
    if a < 0:
        print("Неправильно введене число")
        return;
    else:
        a1 = 2
        a2 = a - 2
        b1 = a1 / 10.5
        b2 = a1 / 4
        b3 = a2 / 7
        b4 = b2 + b3
        b5 = b1 + b3
        print("Ваші собачі роки: ",+ b5)

breaku()
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Артур Третяк"

printTimeStamp(name)

