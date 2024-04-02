from random import randint
n= 25
a = [randint(30, 140) for i in range(n)]
b = []
for i in range(len(a)):
    if a[i] >= 100:
        b.append(a[i])
        del a[i]
    else:
        pass
print(*a)
print(*b)