from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor


class Rectangle(Figure):
    FIGURE_TYPE = "Прямоугольник"

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = FigureColor()
        self.color.colorproperty = color
    
    def square(self):
        return self.width * self.height
    
    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __repr__(self):
        return "{} {} цвета, шириной {}, высотой {} и площадью {}.".format(
            self.get_figure_type(),
            self.color.colorproperty,
            self.width,
            self.height,
            self.square()
        )
