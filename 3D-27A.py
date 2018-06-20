import datetime
import random
t = open("aa.txt", 'r')
text = t.readlines()

password = text[random.randint(0, len(text) - 1)].title() + text[random.randint(0, len(text) - 1)]
print(password)
t.close()

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Team X")