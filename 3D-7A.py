import datetime
import random

def password():
    passw = ''
    for i in range(random.randint(8,17)):
        passw += chr(random.randint(33, 127))
    print(passw.encode("ascii"))

for i in range(10):
    password()

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Team X")