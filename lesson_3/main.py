from figures import Figure
from curve import Circle
from polygon import Triangle, Rectangle, Square


if __name__ == '__main__':
    figures = Figure()
    figures.add_figure(Circle(2))
    figures.add_figure(Rectangle(1, 1))
    # figures.add_figure(Square(2, 1))
    figures.add_figure(Square(2, 2))
    #figures.add_figure(Triangle(1, 2, 3))
    figures.add_figure(Triangle(4, 5, 6))
    print(f"Всего фигур: {len(figures.objects)}")
    print(f"Общая площадь: {figures.sum_area}")
