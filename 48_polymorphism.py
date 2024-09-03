# Polymorphism = Greek word that means to "have many forms or faces"
# Poly = Many
# Morphe = Form
from abc import abstractmethod


class Shape:
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Square(Shape):
    def __init__(self, width):
        self.width = width

    def area(self):
        return self.width ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5


shapes = [Circle(5), Square(4), Triangle(6, 3)]

for shape in shapes:
    print(shape.area())