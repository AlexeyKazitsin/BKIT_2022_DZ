from lab_python_oop.figure import Figure
from lab_python_oop.color import Color


class Rectangle(Figure):
    """
    Класс "Прямоугольник"
    """
    FIGURE_TYPE = "Прямоугольник"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color_param, width_param, height_param):
        """
        Класс должен содержать конструктор по параметрам «ширина», «высота» и «цвет». В конструкторе создается объект
        класса «Цвет фигуры» для хранения цвета.
        """
        self.width = width_param
        self.height = height_param
        self.fc = Color()
        self.fc.color_property = color_param

    def square(self):
        """
        Вычисление площади фигуры
        """
        return self.width * self.height

    def __repr__(self):
        return '{} {} цвета, шириной {} и высотой {}, площадью {:.3f}.'.format(
            Rectangle.get_figure_type(),
            self.fc.color_property,
            self.width,
            self.height,
            self.square()
        )