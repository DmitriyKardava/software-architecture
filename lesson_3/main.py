from figures import Figure
from circle import Circle
from rectangle import Rectangle
from square import Square
from triangle import Triangle

if __name__ == '__main__':
    figures = Figure()
    figures.add_figure(Circle(2))
    figures.add_figure(Rectangle(1, 1))
    figures.add_figure(Square(2))
    # figures.add_figure(Triangle(1, 2, 3))
    figures.add_figure(Triangle(4, 5, 6))
    print(f"Всего фигур: {len(figures.objects)}")
    print(f"Общий периметр: {figures.perimeter}")
    print(f"Общая площадь: {figures.area}")
