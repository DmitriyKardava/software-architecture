from figures import Figure


class Circle(Figure):
    pi = 3.1415926

    def __init__(self, r):
        self.r = r
        super().__init__()

    @property
    def length(self):
        return Circle.pi * self.r * 2

    @property
    def area(self):
        return Circle.pi * self.r ** 2
