b = int(input('Введите кол-во мальчиков: '))
g = int(input('Введите кол-во девочек: '))
answer = ''
if (b > 2 * g) or (g > 2 * b):
    print('Нет решения.')
elif b >= g:
    k = b - g
    for i in range(k):
        answer += 'BGB'
    for i in range(g - k):
        answer += 'BG'
else:
    k = g - b
    for i in range(k):
        answer += 'GBG'
    for i in range(b - k):
        answer += 'GB'
print(answer)