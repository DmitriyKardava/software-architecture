from abc import abstractmethod
from figures import Figure


class Polygon(Figure):
    @abstractmethod
    def area(self):
        pass


class Triangle(Polygon):
    def __init__(self, a, b, c):
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError
        self.a = a
        self.b = b
        self.c = c
        super().__init__()

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    @property
    def area(self):
        p = self.perimeter / 2
        return p*(p-self.a)*(p-self.b)*(p-self.c) ** 0.5


class Rectangle(Polygon):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        super().__init__()

    @property
    def perimeter(self):
        return (self.a * 2) + (self.b * 2)

    @property
    def area(self):
        return self.a * self.b


class Square(Rectangle):
    def __init__(self, a, b):
        if a != b:
            raise ValueError
        self.a = a
        self.b = b
        super().__init__(self.a, self.b)
