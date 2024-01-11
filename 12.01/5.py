a, b, c, d, v = [int(i) for i in input().split()]
if a > b and a > c and a > d and a > v:
    print(a)
elif b > c and b > a and b > d and b > v:
    print(b)
elif c > b and c > a and c > d and c > v:
    print(c)
elif d > b and d > c and d > a and d > v:
    print(d)
elif v > b and v > c and v > d and v > a:
    print(v)