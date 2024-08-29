# fruits = ["apple", "orange", "banana", "coconut"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats = ["chicken", "fish", "turkey"]
#
# groceries = [fruits,vegetables,meats]
# print(groceries)
# print(groceries[1][1])
#
# for collection in groceries:
#     for food in collection:
#         print(food)

# Numpad using tuple

numPad = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ("*", 0, "#"))

for row in numPad:
    for nums in row:
        print(nums, end=" ")
    print()