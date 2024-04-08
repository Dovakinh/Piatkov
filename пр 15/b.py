from random import randint
a = [randint(0, 100) for i in range(5)]
print('Массив', end = ' ')
print(*a)
b = []
for i in range(len(a)):
    if a[i] % 2 == 0 or a[i] % 3 == 0 or a[i] % 5 == 0 or a[i] % 7 == 0:
        pass
    else:
        b.append(a[i])
print('Массив', end = ' ')
print(*b)
