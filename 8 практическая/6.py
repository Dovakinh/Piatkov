def perev(a):
    s = 0
    for i in range(len(str(a)), -1, -1):
        s += (a % 10) * (10 ** (i - 1))
        a //= 10
    print(int(s))
perev(1234)