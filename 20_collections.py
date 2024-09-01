# collection = single "variable" used to store multiple values
#               List = [ ] ordered and changeable. Duplicates OK
#               Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
#               Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# LIST
# fruits = ["apple", "banana", "papaya", "orange"]

# print(fruits)
# print(fruits[3])
# print(fruits[::-1])
# print("apple" in fruits)

# for x in fruits:
#     print(x)

# fruits[0] = "pineapple"
# fruits.append("strawberry")
# fruits.remove("banana")
# fruits.insert(0,"apple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("apple"))
# print(fruits.count("banana"))
# print(fruits)

# SETS
fruits = {"apple", "banana", "papaya", "orange"}
print(fruits)
