a = 10
b = 5
c = 0.5
for i in range(11):
    for j in range(21):
        for k in range(201):
            k_g = i * a + j * b + k * c
            k_r = i + j + k
            if (k_r <= 100) and k_g == 100:
                print(f'Быков {i}, коров {j}, телят {k}')
