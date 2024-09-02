# List comprehension = A concise way to create lists in Python
# Compact and easier to read than traditional loops
# [expression for value in iterable if condition]

# doubles= []
# for x in range(1,11):
#     doubles.append(x*2)
#
# print(doubles)

# doubles = [x * 2 for x in range(1, 11)]
# print(doubles)
# triple = [x * 3 for x in range(1, 11)]
# print(triple)
# squares = [x * x for x in range(1, 11)]
# print(squares)

# fruits = ["apple", "orange", "banana", "coconut"]
# print(fruits)
# fruits = [fruit.upper() for fruit in fruits]
# print(fruits)

numbers = [1, -2, 3, 4, -5, -6]
positive_nums = [num for num in numbers if num >= 0]
print(positive_nums)
negative_nums = [num for num in numbers if num <= 0]
print(negative_nums)
