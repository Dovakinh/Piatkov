for i in range(1, 10001):
    chislo = 0
    n = 0
    for h in range(1, i):
        if i % h == 0:
            chislo += h
    for j in range(1, chislo):
        if chislo % j == 0:
            n += j
    if i == n and i != chislo and i == min(i, chislo):
        print(f'{i} = {chislo}')