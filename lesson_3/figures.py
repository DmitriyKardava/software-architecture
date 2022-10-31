from abc import abstractmethod


class Figure(object):
    def __init__(self):
        self.objects = []

    @abstractmethod
    def area(self):
        pass

    def add_figure(self, figure):
        self.objects.append(figure)

    @property
    def sum_area(self):
        return sum([x.area for x in self.objects])