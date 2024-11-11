class Car:
    number_of_wheels = 4
    _color = "Black"
    __year_of_manufacture = 2017


class Bmw(Car):
    def __init__(self):
        print("protected attribute color:", self._color)


car = Car()
print("public attribute number_of_wheels ", car.number_of_wheels)
bmw = Bmw()
print("private attribute year_of_manufacture", car._Car__year_of_manufacture)