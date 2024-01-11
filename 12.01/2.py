from random import randint
a= randint(1,6)
b = randint(1,6)
c = randint(1,6)
print('Выпало очков:', a, b, c)
print('Число :', str(a) + str(b) + str(c))
print('Его квадрат:', int(str(a) + str(b) + str(c)) ** 2)