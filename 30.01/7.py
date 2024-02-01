s = int(input())
for a in range(s):
    for b in range(s):
        if a * b == s:
            print(f'{a} * {b} = {s}')
        else:
            pass