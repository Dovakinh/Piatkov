from random import randint
a = [randint(120, 200) for i in range(30)]
print(f'Ученики:\n{" ".join(str(i) for i in a)}')
b = 0
for i in range(30):
    if a[i] >= 170:
        b += 1
    else:
        pass
if b >= 5:
    print("Команду можно создать")
else:
    print("Команду нельзя создать")

