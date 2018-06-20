import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Третяк Артур')
print ('Введіть числа:')
list_a = 1
x = 1
check_print = 0
l_a = []
main_restart = 1
while main_restart == 1:
    while list_a == 1:
        if x != 0:
            x = int (input ())
            l_a.append(x)
            #if 
            list_a = 1
        else:
            check = l_a.index(0)
            if check == 0:
                main_restart = 0
                check_print = 1
                print ('Перше число не може бути нулем!!!')
            l_a.remove(0)
            list_a = 0
            main_restart = 0
else:
    if check_print == 0:
        l = len(l_a)
        summ = sum(l_a)
        answear = summ / l
        print ('Середнє для набору значень:', answear)
