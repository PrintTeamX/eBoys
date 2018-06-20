a = "b"
b = []
while a != '':
    a = str(input())
    for i in a:
        if i not in b:
            b.append(a)
print(b)