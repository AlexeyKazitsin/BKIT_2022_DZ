from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):
    """
    Класс "Квадрат"
    """
    FIGURE_TYPE = "Квадрат"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color_param, side_param):
        """
        Класс должен содержать конструктор по параметрам "цвет" и "сторона"
        """
        self.side = side_param
        super().__init__(color_param, self.side, self.side)

    def __repr__(self):
        return '{} {} цвета со стороной {}, площадью {:.3f}.'.format(
            self.get_figure_type(),
            self.fc.color_property,
            self.side,
            self.square()
        )