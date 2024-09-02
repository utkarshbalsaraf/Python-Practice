# def happy_birthday(name, age):
#     print(f"Happy Birthday {name}")
#     print(f"You are {age} years old now\n")
#
#
# happy_birthday("Utkarsh", 25)
# happy_birthday("Simran", 22)
# happy_birthday("Shantanu", 26)

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    a * b


def divide(a, b):
    return a / b


# print(divide(534543, 545))
# print(add(3424, 5453))
# print(multiply(32, 24))
# print(subtract(2343243, 2343423))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last


print(create_name("utkarsh", "balsaraf"))
