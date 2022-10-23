class Figure(object):
    def __init__(self):
        self.objects = []

    def add_figure(self, figure):
        self.objects.append(figure)

    @property
    def perimeter(self):
        s = 0
        for x in self.objects:
            s += x.perimeter
        return s

    @property
    def area(self):
        s = 0
        for x in self.objects:
            s += x.area
        return s
