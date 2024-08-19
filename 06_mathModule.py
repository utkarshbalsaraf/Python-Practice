import math

x=5.4
# print(math.pi)
# print(math.e)
#
# print(math.sqrt(16))
# print(math.ceil(x))
# print(math.floor(x))

radius = float(input("Enter the radius of circle"))

circumference= 2*math.pi * radius
print(f"Circumference of circle is : {round(circumference,2)}")

area = math.pi * radius ** 2
print(f"Area of circle is : {round(area,2)} cm.sq")