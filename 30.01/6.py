n, m = [int(i) for i in input('Введите n И m: \n').split()]
for i in range(n):
    for j in range(n):
        a = i ** 2 + 2 * i * j + j ** 2
        if a == m:
            print(f'({i} + {j})**2 = {m}')
        else:
            pass