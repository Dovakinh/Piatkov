from random import randint
n = int(input())
a = [randint(2, 100) for i in range(n)]
b = []
for i in range(len(a)):
    if a[i] % 2 == 0 or a[i] % 3 == 0 or a[i] % 5 == 0 or a[i] % 7 == 0:
        pass
    else:
        b.append(a[i])
s = sum(i for i in b)
print(f'Массив:\n{" ".join(str(i) for i in a)}')
print(f'Простые числа:\n{" ".join(str(i) for i in b)}')
print(f'Среднее арифметическое: {s/len(b)}')
