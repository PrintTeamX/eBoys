result = ''
q = int(input('Введіть ціле десяткове число: '))
while q != 0:
    r = q % 2
    result += str(r)
    q //= 2
print('Двійкове представлення числа: ' + result)
import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Третяк Артур')