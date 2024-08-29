# name = input("Enter your name\n")
# while name == "":
#     print("You didn't enter the name")
#     name = input("Please enter your name\n")
# print(f"Hello {name}")

food = input("Enter the food you like (q for Quit)\n")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q for Quit)\n")
print("Bye")
