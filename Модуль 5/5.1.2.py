class Point:

    def __init__(self, x=0, y=0):
        if self.check_coord(x) and self.check_coord(y):
            self.x = x
            self.y = y

    def check_coord(self, a):
        return type(a) in (int, float)

    def set(self, x, y):
        if self.check_coord(x) and self.check_coord(y):
            self.x = x
            self.y = y
        else:
            print('Используйте только числа')

    def get(self):
        return self.x, self.y


class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        p = 0
        tmp = tuple([c, a, b, c])
        for i in range(1, len(tmp)):
            x1 = tmp[i-1].x
            y1 = tmp[i-1].y
            x2 = tmp[i].x
            y2 = tmp[i].y
            p += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)
        return p


a = Point(1, 1)
b = Point(2, 2)
c = Point(2, 1)
b.set(3, 6)

abc = Triangle(a, b, c)

print(abc.perimeter())
