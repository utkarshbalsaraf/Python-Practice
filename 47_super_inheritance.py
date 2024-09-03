# super() = Function used in a child class to call methods from a parent class (superclass).
#           Allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"The color is {self.color} and its {'Filled' if self.is_filled else 'not Filled'}")


class Circle(Shape):
    def __init__(self, radius, color, is_filled):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"the Area of cicle is : {3.14 * self.radius ** 2}")


class Triangle(Shape):
    def __init__(self, width, height, color, is_filled):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height


class Square(Shape):
    def __init__(self, width, color, is_filled):
        super().__init__(color, is_filled)
        self.width = width


circle1 = Circle(color="red", is_filled=True, radius=5)
square = Square(color="blue", is_filled=False, width=5)

print(circle1.radius)
print(circle1.color)
print(circle1.is_filled)
circle1.describe()
