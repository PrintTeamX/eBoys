import datetime

def calc(*args):
    summ = 0
    mass= 0
    calcu = 0
    for i in args:
        for ii in i:
            calcu += ii[1]
            mass += ii[2]
    summ += calcu * 2
    if mass <= 5:
        summ += 10
    elif mass <= 10:
        summ += 12
    elif mass <= 20:
        summ += 15
    else:
        summ += 25
    return summ

print(calc([["s", 10, 5], ["w", 10, 5], ["t", 10, 5]]))

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Team X")
