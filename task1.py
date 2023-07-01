class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return (self.w + self.h) * 2


rectangle1 = Rectangle(4, 5)
rectangle2 = Rectangle(3, 5)
print(f'Площадь: {rectangle1.area()}')
print(f'Площадь: {rectangle2.area()}')
print(f'Периметр: {rectangle1.perimeter()}')
print(f'Периметр: {rectangle2.perimeter()}')
