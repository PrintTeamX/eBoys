a = int(input("Введіть першу сторону: "))
b = int(input("Введіть другу сторону: "))
c = int(input("Введіть третю сторону: "))

def func():
    if a == b == c:
        print("Трикутник рівносторонній")
    elif a == b != c or a != b == c or a != c == b or a == c != b:
        print("Трикутник рівнобедренний")
    elif a != b != c:
        print("Трикутник довільний")
    else:
        print("Невідомо")
func()

