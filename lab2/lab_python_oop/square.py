from lab_python_oop.rectangle import Rectangle
from lab_python_oop.figure_color import FigureColor

class Square(Rectangle):
    figure_name = "Квадрат"
    def __init__(self, side, color):
        super().__init__(side, side, color)


    def get_figure_name(self):
        return self.figure_name

    def __repr__(self):
        return "{} цвета {}, co стороной {}, площадью {}".format(
            self.figure_name,
            self.color,
            self.width,
            self.square()
        )