from abc import ABC, abstractmethod


class Figure:
    """
    Абстрактный класс "Геометрическая фигура"
    """

    @abstractmethod
    def square(self):
        """
        Виртуальный метод вычисления площади фигуры
        """
        pass