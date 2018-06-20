import datetime
print("Введіть ваше імя: ")
a = input()
print("Привіт,", a, "!")

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Артур Третяк"

printTimeStamp(name)
