from lab_python_oop.geometric_figure import GeometricFigure
from lab_python_oop.figure_color import FigureColor

class Circle(GeometricFigure):
    figure_name = "Круг"
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def square(self):
        return 3.14 * self.radius * self.radius

    def get_figure_name(self):
        return self.figure_name

    def __repr__(self):
        return "{} цвета {}, c радиусом {}, площадью {}".format(
            self.figure_name,
            self.color,
            self.radius,
            self.square()
        )