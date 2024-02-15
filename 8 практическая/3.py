def sum_chisla(c):
    sum = 0
    for i in range(len(str(c))):
        sum += c % 10
        c //= 10
    return c


a = sum_chisla(int(input()))
b = sum_chisla(int(input()))
if a > b:
    print(a)
elif a < b:
    print(b)
else:
    print(f"{a} и {b} равны")
