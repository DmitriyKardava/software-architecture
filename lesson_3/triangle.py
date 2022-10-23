from figures import Figure


class Triangle(Figure):
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
