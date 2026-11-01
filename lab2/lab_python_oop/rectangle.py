from lab_python_oop.geometric_figure import GeometricFigure
from lab_python_oop.figure_color import FigureColor

class Rectangle(GeometricFigure):
    figure_name = "Прямоугольник"
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def square(self):
        return self.width * self.height

    def get_figure_name(self):
        return self.figure_name

    def __repr__(self):
        return "{} цвета {}, co сторонами {} и {}, площадью {}".format(
            self.figure_name,
            self.color,
            self.width,
            self.height,
            self.square()
        )