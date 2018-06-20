import datetime

def rec(x, y):
    if y == 0:
        return 1
    else:
        return x * rec(x, y - 1)


print(rec(2, 10))

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Team X")