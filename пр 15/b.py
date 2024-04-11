from random import randint
a = [randint(0, 100) for i in range(5)]
print('Массив', end = ' ')
print(*a)
b = []
for i in range(len(a)):
    if a[i] == 2 or a[i] == 3 or a[i] == 5 or a[i] == 7:
        b.append(a[i])
    elif a[i] <= 1 or a[i] % 2 == 0 or a[i] % 3 == 0 or a[i] % 5 == 0 or a[i] % 7 == 0:
        pass
    else:
        b.append(a[i])
if len(b) == 0:
    print('Простых чисел нет')
else:
    print('Массив', end = ' ')
    print(*b)
