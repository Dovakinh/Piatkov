a = int(input('Введите ваш возраст:'))
if a == 1 or a == 21 or a == 31 or a == 41:
    print(f'Вам {a} год')
elif a == 51 or a == 61 or a == 71 or a == 81 or a == 91 or a == 101 or a == 121:
    print(f'Вам {a} год')
elif (a > 1 and a <= 4) or (a > 21 and a <= 24) or (a > 31 and a <= 34):
    print(f'Вам {a} годa')
elif (a > 41 and a <= 44) or (a > 51 and a <= 54) or (a > 61 and a <= 64) or (a > 71 and a <= 74):
    print(f'Вам {a} годa')
elif (a > 81 and a <= 84) or (a > 91 and a <= 94):
    print(f'Вам {a} годa')
else:
    print(f'Вам {a} лет')