x, y, p = [int(i) for i in input('Введите 3 целых числа\n').split()]
g = 0
while x <= y:
    x += y
    g += 1
print(g)