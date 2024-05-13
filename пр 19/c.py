def rim(bukva):
    if bukva == 'M':
        return (1000)
    elif bukva == 'X':
        return (10)
    elif bukva == 'I':
        return (1)
    elif bukva == 'C':
        return (100)


b = [i for i in input().split()]
for a in b:
    if 'M' in a or 'X' in a or 'I' in a or 'C' in a:
        kol = 0
        bukva = a[0]
        s = 0
        for i in a:
            s += rim(i)
        b.insert(b.index(a), s)
        del b[b.index(a)]
print(*b)
