def sover(a):
    c = 0
    for i in range(1, a):
        if a % i == 0:
            c += i
        else:
            pass
    return c == a
print(sover(28))