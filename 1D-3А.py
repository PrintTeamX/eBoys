import datetime

print("Число в кПа: ")
a = float(input())
print ("фт/дм2: ", a*0.145038)

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Артур Третяк"
printTimeStamp(name)

