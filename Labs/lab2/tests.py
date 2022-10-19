import unittest
from lab_python_oop.color import FigureColor
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


class TestLabPythonOOP(unittest.TestCase):
    def test_color(self):
        color = FigureColor()
        color.colorproperty = "red"
        self.assertDictEqual(color.__dict__, {"_color": "red"})

        color.colorproperty = "green"
        self.assertDictEqual(color.__dict__, {"_color": "green"})

        self.assertFalse(hasattr(FigureColor, "_color"))

    def test_rectangle(self):
        self.assertEqual(Rectangle.get_figure_type(), "Прямоугольник")

        rect = Rectangle(3, 5, "black")
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.color.colorproperty, "black")
        self.assertEqual(rect.square(), 15)

    def test_circle(self):
        self.assertEqual(Circle.get_figure_type(), "Круг")

        circle = Circle(5, "white")
        self.assertEqual(circle.color.colorproperty, "white")
        self.assertEqual(circle.radius, 5)
        self.assertTrue(abs(78.539816 - circle.square()) < 0.000001)

    def test_square(self):
        self.assertEqual(Square.get_figure_type(), "Квадрат")

        square = Square(8, "yellow")
        self.assertEqual(square.side, 8)
        self.assertEqual(square.color.colorproperty, "yellow")
        self.assertEqual(square.square(), 64)


if __name__ == "__main__":
    unittest.main()
