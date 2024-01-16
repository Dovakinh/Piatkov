print('Введите три числа:')
a, b, c = [int(i) for i in input().split()]
if a == b == c:
    print('Все числа одинаковые.')
elif a == b and b != c or a == c and b != c or b == c and a != c:
    print('Два числа одинаковые.')
else:
    print('Нет одинаковых чисел.')