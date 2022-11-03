from lab_python_oop.rectangle import Rectangle
from lab_python_oop.color import FigureColor


class Square(Rectangle):
    FIGURE_TYPE = "Квадрат"

    def __init__(self, side, color):
        self.side = self.width = self.height = side
        # self.side = side
        self.color = FigureColor()
        self.color.colorproperty = color
    
    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __repr__(self):
        return "{} {} цвета со стороной {} и площадью {}.".format(
            self.get_figure_type(),
            self.color.colorproperty,
            self.side,
            self.square()
        )
