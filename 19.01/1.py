a, b = [int(i) for i in input('Введите 2 целых числа\n').split()]
while a <= b:
    print(f'{a} * {a} =', a * a)
    a += 1