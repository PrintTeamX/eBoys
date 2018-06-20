from random import randrange
import datetime

def sattoloCycle(items):
    i = len(items)
    while i > 1:
        i = i - 1
        j = randrange(i)
        a1 = k.pop(i)
        b1 = k.pop(j)
        k.insert(j, a1)
        k.insert(i, b1)
    return

k = []
l = ['s', 'h', 'd', 'c']
s = ['J', 'Q', 'K', 'A']
for i in range(len(l)):
    for a in range(2, 11):
        b = str(a) + str(l[i])
        k.append(b)
    for c in range(len(s)):
        b = str(s[c]) + str(l[i])
        k.append(b)
print(k)
print('\n')
sattoloCycle(list(k))
print(k)

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Team X")