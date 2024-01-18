n  = int(input('Введите натуральное число:\n'))
k = [0] * 10
while n > 0:
    dig = n % 10
    k[dig] += 1
    n //= 10
    if 2 in k:
        print('Да')
        break
else:
    print('Нет')