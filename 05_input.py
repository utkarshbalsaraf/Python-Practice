# a = float(input("Enter your name"))
# print(a)
# print(type(a))
#
# length = float(input("Enter the length\n"))
# breadth = float(input("Enter the Breadth\n"))
# print(f"Area of rectangle is {length * breadth} cm.sq")

item = input("Enter the item which you like to buy?\n")
price = float(input("Enter the price?\n"))
quantity = int(input("Enter the quantity?\n"))

print(f"You have bought {quantity} {item}/s")
print(f"Total amount paid: ${round(price * quantity, 2)}")
