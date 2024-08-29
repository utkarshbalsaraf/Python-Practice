foods = []
prices = []
total = 0

while True:
    food = input(f"Enter the food to buy (q to Quit)\n")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: \n$"))
        foods.append(food)
        prices.append(price)
for food in foods:
    print(food, end=", ")

for price in prices:
    total += price
print(f"\nYour total is {total:.2}")
