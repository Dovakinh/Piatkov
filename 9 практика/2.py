def tr(a, b, c):
    return a + b > c and a + c > b and b + c > a

def pr(a, b, c):
    if (a ** 2 + b ** 2 == c ** 2) or (b ** 2 + c ** 2 == a ** 2) or (a ** 2 + c ** 2 == b ** 2):
        return True
    else:
        return False

a, b, c = [float(i) for i in input('Введите а, b, с: \n').split()]
if pr(a, b, c):
    print("есть")
else:
    print('нет')