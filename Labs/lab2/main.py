from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from faker import Faker

def main():
    rect = Rectangle(2, 2, "Синего")
    circle = Circle(2, "Зеленого")
    square = Square(2, "Красного")
    print(rect, circle, square, sep="\n")
    print(Faker().word())

if __name__ == "__main__":
    main()
