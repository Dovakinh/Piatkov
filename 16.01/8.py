a = int(input('Введите площадь квартиры '))
b = float(input('Введите цену квартиры (в миллионах)'))
if a >= 100 and b <= 10 or a >= 80  and b <= 7:
    print('Квартира подходит')
else:
    print('Квартира не подходит')
