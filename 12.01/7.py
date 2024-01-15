a = int(input())
b = a - (a // 5) * 5
if b > 3 or b==0:
    print('красный')
else:
    print('зеленый')
