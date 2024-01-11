a = int(input())
b = int(input())
v = int(input())
if a == b and b == v:
    print('Одинаковый')
elif a >= b and a >= v:
    if a == b:
        print('Антон и Борис')
    elif a == v:
        print('Антон и Виктор')
    else:
        print('Антон')
elif b >= a and b >= v:
    if a == b:
        print('Борис и Антон')
    elif b == v:
        print('Борис и Виктор')
    else:
        print('Борис')
elif v >= b and v >= a:
    if v == b:
        print('Виктор и Борис')
    elif v == a:
        print('Виктор и Антон')
    else:
        print('Виктор')