a = 1
p = 0
m = 0
while a != 0:
    a = int(input('Введите число: '))
    if a > 0:
        p += 1
    elif a < 0:
        m += 1
print(f'Кол-во положительных чисел: {p}')
print(f'Кол-во отрицательных чисел: {m}')