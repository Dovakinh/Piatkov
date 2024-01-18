a = int(input('Введите счет'))
b = 0
if a == 0:
    print('1')
else:
    while a > 0:
        b += 1
        a = a // 10
    print(b)