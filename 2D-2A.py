a = 1
b = []

while a != 0:
    a = int(input())
    b.append(a)

b.remove(0)
b.sort()

print(b)