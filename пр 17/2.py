a = input('Введите строку: \n')
b = input('Что меняем: \n')
c = input('Чем заменить: \n')
d = [i for i in a.split(b)]
print('Результат: \n' + c.join(d))