def squared(a, b, k):
    d = 0
    for i in range(a, b + 1):
        if (i ** 2) % k == 0:
            pass
        else:
            if d == 9:
                print()
                d = 0
            else:
                print(f'{i ** 2}', end=' ')
            d += 1
squared(11, 99, 10)