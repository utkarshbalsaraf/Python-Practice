# object = A "bundle" of related attributes (variables) and methods (functions)
#           Ex. phone, cup, book
#           You need a "class" to create many objects
# class = (blueprint) used to design the structure and layout of an object

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.model}")


car1 = Car("Mustang",2024,"red",False)
car2 = Car("Corvette",2014,"blue",True)
car1.drive()
car2.drive()
car1.stop()
car2.stop()

print(f"{car1.model} {car1.year} {car1.color} {car1.for_sale}")
print(f"{car2.model} {car2.year} {car2.color} {car2.for_sale}")