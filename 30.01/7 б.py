s = int(input())
fchis = []
schis = []
for a in range(s):
    for b in range(s):
        if a * b == s:
            if (a in schis) and (b in fchis):
                pass
            else:
                print(f'{a} * {b} = {s}')
                fchis.append(a)
                schis.append(b)
        else:
            pass
