from abc import abstractmethod
from figures import Figure


class Polygon(Figure):
    def __init__(self, sides):
        self.sides = sides
        super().__init__()

    @abstractmethod
    def area(self):
        pass

    @property
    def perimeter(self):
        return sum(self.sides)


class Triangle(Polygon):
    def __init__(self, sides):
        if len(sides) != 3:
            raise ValueError
        if not (sides[0] + sides[1] > sides[2]
                and sides[0] + sides[2] > sides[1]
                and sides[1] + sides[2] > sides[0]):
            raise ValueError
        super().__init__(sides)

    @property
    def area(self):
        p = self.perimeter / 2
        return (p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2])) ** 0.5


class Rectangle(Polygon):
    def __init__(self, sides):
        if len(sides) != 2:
            raise ValueError
        super().__init__(sides)

    @property
    def area(self):
        return self.sides[0] * self.sides[1]

    @property
    def perimeter(self):
        return super().perimeter * 2
        

class Square(Rectangle):
    def __init__(self, sides):
        if sides[0] != sides[1]:
            raise ValueError
        super().__init__(sides)
