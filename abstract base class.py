from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    @abstractmethod
    def area(self):
        return 0


class Square(Shape):
    side = 4

    def area(self):
        print("Area of square :", self.side*self.side)


class Rectangle(Shape):
    length = 10
    width = 15

    def area(self):
        print("Area of rectangle :", self.length*self.width)


square = Square()
rectangle = Rectangle()
square.area()
rectangle.area()
