import datetime

x = int(input("Введіть рік: "))
y = int(input("Введіть місяць: "))
z = int(input("Введіть день: "))
today = datetime.date(x, y, z)
tomorrow = today + datetime.timedelta(days=1)

print("Наступний день: " + str(tomorrow))

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Team X")