def equation(a, b):
    x1, x2 = map(int, a.split(';'))
    y1, y2 = map(int, a.split(';'))
    x = ((y1 - y2) / (x1 - x2))
    y = y2 - x * x2
    print(f'{x};{y}')
equation('12;4', '10;1')
