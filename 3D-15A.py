import datetime

arr = [1]
def Catalan(n):
    global arr
    while(len(arr) != n+1):
        arr.append(int(int(arr[len(arr)-1] ) * (4*len(arr)-2)/(len(arr)+1) ) )
    print(arr[n])

Catalan(10)

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Team X")