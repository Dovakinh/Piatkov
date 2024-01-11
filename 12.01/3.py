from random import randint
a = randint(100,999)
print('Получено число', a)
print('сотни:', (a//100)%10)
print('десятки:', (a%100)//10)
print('единицы:', a%10)