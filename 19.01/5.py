a = int(input())
b = len(str(a))
s = 0
while b != 0:
    b -= 1
    s = a % 10
    v = (a // 10) % 10
    if v == s:
        print('Да')
        break
    a = a //10
else:
    print('Нет')