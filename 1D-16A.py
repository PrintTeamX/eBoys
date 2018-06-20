import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

a = int(input("ввеліть площу у метрах: "))

if a >= 0:
    b = a / 10000
    c = a / 100
    print(str(b) + " гектарів\n" + str(c) + " ар")
else:
    print("error")
