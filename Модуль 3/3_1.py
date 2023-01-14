def area(a, b, c):
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** (1/2)
    return s


a, b, c = int(input('Сторона 1: ')), int(input('Сторона 2: ')), int(input('Сторона 3: '))
print('Площадь треугольника:', area(a, b, c))
