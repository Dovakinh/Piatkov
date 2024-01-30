n = int(input('Введите N: '))
for i in range(1, n + 1):
    for j in str(i):
        if int(j) == 0 or int(j) == 1:
            pass
        elif int(i) % int(j) == 0:
            print(i, end=' ')
            