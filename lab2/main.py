from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

import cowsay

def main():
    rect_width = float(input("Введите ширину прямоугольника: "))
    rect_height = float(input("Введите высоту прямоугольника: "))
    rect_color = input("Введите цвет прямоугольника: ")

    circle_radius = float(input("Введите радиус круга: "))
    circle_color = input("Введите цвет круга: ")

    square_side = float(input("Введите сторону квадрата: "))
    square_color = input("Введите цвет квадрата: ")

    rect = Rectangle(rect_width, rect_height, rect_color)
    circle = Circle(circle_radius, circle_color)
    square = Square(square_side, square_color)

    print(rect)
    print(circle)
    print(square)

    cowsay.cow("Все фигуры успешно созданы через консольный ввод!")

if __name__ == "__main__":
    main()