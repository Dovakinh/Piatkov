n = int(input('n '))
c = 0
for i in range(100, 1000):
    if n == ((i // 100) % 10) + ((i % 100) // 10) + (i % 10):
        c += 1
print(c)