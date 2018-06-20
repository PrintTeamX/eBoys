import datetime
b = lambda year: (not year % 4 and year % 100) or not year % 400

print(b(int(input())))

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Team X")