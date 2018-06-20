import datetime
t = open('test1.txt', 'r')
for i in range(10):
    print(t.readline())

t.close()
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Team X")