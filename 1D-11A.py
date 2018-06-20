import datetime
print("B сантиметрах: ")
a = float(input())

print ("футах: ", a * 12)
print ("дюймах: ", a * 2.54, "\n")

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Артур Третяк"

printTimeStamp(name)
