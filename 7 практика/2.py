a = int(input())
dlin = 10 ** (len(str(a)) - 1)
for i in range(len(str(a))):
    print(int(a // dlin))
    a %= dlin
    dlin /= 10