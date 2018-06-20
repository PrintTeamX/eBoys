import itertools
import random
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(a)
b = []
for i in range(8):
    c = random.randint(1, 100)
    b.append(c)
print(list(itertools.permutations(a)))

print(a + b)