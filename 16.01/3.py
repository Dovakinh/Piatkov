print('Введите номер месяца:')
a = int(input())
if 1 <= a < 3 or a == 12:
    print("Зима")
elif a >= 3 and a < 6:
    print('Весна')
elif a >= 6 and a < 9:
    print('Лето')
elif a >= 9 and a < 12:
    print('Осень')
else:
    print('Неверный номер месяца.')
