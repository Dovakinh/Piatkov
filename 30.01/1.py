a = 15
b = 17
c = 21
d = 0
for i in range(16):
    for j in range(21):
        for k in range(201):
            k_g = i * a + j * b + k * c
            if k_g == 185:
                d += 1
print(d)