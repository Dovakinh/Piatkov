a = int(input())
b = len(str(a))
s = 0
while b != 0:
    b -= 1
    s += a % 10
    a = a // 10
print(s)