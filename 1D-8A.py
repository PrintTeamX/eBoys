import datetime

number = str(input('Введіть 4-ох значне число: '))
number0 = int(number[0])
number1 = int(number[1])
number2 = int(number[2])
number3 = int(number[3])
print('Сума цих чисел:')
print(number0+number1+number2+number3)

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Артур Третяк"

printTimeStamp(name)
