a = int(input('Введите начало отрезка: '))
b = int(input('ведите конец отрезка: '))
h = int(input('Введите шаг: '))
if h > 0:
    a, b = min(a, b), max(a, b) + 1
else:
    b, a = min(a, b) - 1, max(a, b)
for x in range(a, b, h):
    y = (x ** 3) + 2 * (x ** 2) - 4 * x + 1
    print(f'В точке {x} функция равна {y}')
