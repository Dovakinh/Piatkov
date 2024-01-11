a, b, c = [int(i) for i in input().split()]
if a > b and a > c:
    print(a)
elif b > c and b > a:
    print(b)
elif c > b and c > b:
    print(c)