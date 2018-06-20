import datetime

def rec(x):
    if x == 1:
        return 1
    else:
        return (1 / x) + rec(x - 1)

print(rec(5))

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Team X")