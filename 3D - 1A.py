n = int(input ("Введіть пройденний шлях(метри): "))
def newfunc(a,n):
    print("До сплати: " + str(((n//140)*a) + 25))
newfunc(2, n)

import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Артур Третяк"

printTimeStamp(name)
