import datetime

t = open("text.txt", 'a')
t.write("\n\n")

t.close()

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Team X")