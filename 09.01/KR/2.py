from math import sqrt
x, y = [float(i) for i in input().split()]
x1, y1 = [float(i) for i in input().split()]
print(sqrt(x - x1)**2 + (y - y1)**2)
