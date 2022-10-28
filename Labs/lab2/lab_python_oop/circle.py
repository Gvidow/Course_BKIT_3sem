import math
from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor


class Circle(Figure):
    FIGURE_TYPE = "Круг"

    def __init__(self, radius, color):
        self.radius = radius
        self.color = FigureColor()
        self.color.colorproperty = color

    def square(self):
        return self.radius ** 2 * math.pi
    
    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __repr__(self):
        return "{} {} цвета, радиусом {} и площадью {}.".format(
            self.get_figure_type(),
            self.color.colorproperty,
            self.radius,
            self.square()
        )
