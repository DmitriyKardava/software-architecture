from figures import Figure


class Rectangle(Figure):
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
