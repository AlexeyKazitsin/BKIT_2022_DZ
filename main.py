import numpy

from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    r = Rectangle("синего", 8, 8)
    c = Circle("зеленого", 8)
    s = Square("красного", 8)

    print(r)
    print(c)
    print(s)
    a = numpy.array([[1, 2, 3], [4, 5, 6]])
    print(a)

if __name__ == "__main__":
    main()
