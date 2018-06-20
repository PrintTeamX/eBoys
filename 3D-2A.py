import datetime
import random

x = 0
nums = []
def num():
    global nums

    global x

    num1 = '+38(0'
    num1 += str(random.randint(0, 9))
    num1 += str(random.randint(0, 9))
    num1 += ')'
    num1 += str(random.randint(0, 9))
    num1 += str(random.randint(0, 9))
    num1 += str(random.randint(0, 9))
    num1 += '-'
    num1 += str(random.randint(0, 9))
    num1 += str(random.randint(0, 9))
    num1 += '-'
    num1 += str(random.randint(0, 9))
    num1 += str(random.randint(0, 9))
    nums.append(num1)
    x += 1
    if x < 3:
        num()

num()
print(nums)
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Team X")