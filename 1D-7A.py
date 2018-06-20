import datetime
a = float(input("Градус в цельсиях: "))
print ("в кельвин: ", a + 274.15)
print ("в Фарингейт: ", a * 9/5 + 32.)
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Артур Третяк"

printTimeStamp(name)
