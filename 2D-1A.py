from copy import copy
a = [1, 2 ,3, 3, 3, 3, 2, 5, 6, 7, 8, 1, 10]
b = []
for i in a:
    if i not in b:
        b.append(i)

print(b)

c = copy(b)

del c[0]
del c[1]
del c[1]
print(c)