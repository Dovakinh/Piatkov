from random import randint
n= 25
a = [randint(30, 140) for i in range(n)]
b = []
c = []
for i in range(25):
    if a[i] >= 100: 
        b.append(a[i])
    else:
        c.append(a[i])
bs = sum(i for i in b)
cs = sum(i for i in c)
print(f'Средняя масса полных людей {bs/len(b)}')
print(f'Средняя масса остальных людей {cs/len(c)}')
