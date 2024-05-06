def rim(bukva, kol):
    if bukva == 'M':
        print(1000 * kol)
    elif bukva == 'X':
        print(1000 * kol)
    elif bukva == 'I':
        print(1000 * kol)
    elif bukva == 'C':
        print(1000 * kol)


a = [i for i in input().split()]
for i in a:
    if 'M' in i or 'X' in i or 'I' in i or 'C' in i:
        kol = 1
        bukva = i[0]
        for j in range(len(i) - 1):
            if i[j] == i[j + 1]:
                kol += 1
                pass
            else:
                print(i[j], kol)
                rim(bukva, kol)
