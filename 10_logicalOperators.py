# logical operators = evaluate multiple conditions (or, and, not)
#                       or = at least one condition must be True
#                       and = both conditions must be True
#                       not = inverts the condition (not False, not True)

temp = 50
isRaining = False

if temp > 35 or temp <= 0 or isRaining:
    print("Dont go outside")
else:
    print("You can go Outside")

if temp > 35 or temp <= 0 or isRaining:
    print("Dont go outside")
else:
    print("You can go Outside")


if temp > 35 and temp <= 0 and isRaining:
    print("Dont go outside")
else:
    print("You can go Outside")


# ternary operator
num = 89
a=6
b=8
result = "EVEN" if num % 2 == 0 else "ODD"
maxnum = a if a > b else b
print(result)
print(f"max: {maxnum}")

minnum = b if a > b else a
print(f"min: {minnum}")
