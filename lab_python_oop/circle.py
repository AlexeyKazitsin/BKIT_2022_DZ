import math

from lab_python_oop.figure import Figure
from lab_python_oop.color import Color


class Circle(Figure):
    """
    Класс "Круг"
    """

    FIGURE_TYPE = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color_param, r_param):
        self.fc = Color()
        self.fc.color_property = color_param
        self.r = r_param

    def square(self):
        return 2 * math.pi * self.r ** 2

    def __repr__(self):
        return '{} {} цвета, радиуса {}, площадью {:.3f}.'.format(
            self.get_figure_type(),
            self.fc.color_property,
            self.r,
            self.square()
        )
