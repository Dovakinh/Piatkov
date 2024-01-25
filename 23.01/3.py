for i in range(1, int(input()) + 1):
    a = int((str(i ** 2))[-int(len(str(i))):])
    if i == a:
        print(f"{i} * {i} =", i ** 2)
