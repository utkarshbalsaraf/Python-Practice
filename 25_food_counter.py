menu = {
    "Bananas": 0.58,  # per lb
    "Oranges": 1.25,  # per lb
    "Bread": 2.50,  # per loaf
    "Tomatoes": 1.85,  # per lb
    "Chicken": 3.99,  # per lb
    "Milk": 3.29,  # per gallon
    "Eggs": 2.99,  # per dozen
    "Cheese": 4.50,  # per lb
    "Apples": 1.50,  # per lb
    "Rice": 1.20,  # per lb
    "Pasta": 1.10,  # per lb
    "Beef": 5.99,  # per lb
    "Potatoes": 0.99,  # per lb
    "Carrots": 1.10,  # per lb
    "Lettuce": 1.75,  # per head
    "Yogurt": 0.99,  # per cup
    "Butter": 3.49,  # per lb
    "Fish": 6.99,  # per lb
    "Cereal": 3.99  # per box
}

cart = []
total = 0

for key, value in menu.items():
    print(f"{key:15}:${value:.2f}")

print("---------------------------------------------")

while True:
    food = input("Enter the food in cart\n").capitalize()
    if food == "Q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("\n------------------ Order --------------------")

for food in cart:
    total += menu.get(food)
    print(f"{food}", end=", ")

print("\n\n--------------Total Amount-------------------")

print(f"Your total payable amount is : ${total}")
