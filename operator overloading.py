class Square:
    def __init__(self, side):
        self.side = side

    def __add__(square_one, square_two):
        return (4 * square_one.side) + (4 * square_two.side)


square_one = Square(4)
square_two = Square(5)
print("Sum of sides of both squares = ", square_one + square_two)
