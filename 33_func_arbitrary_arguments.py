# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
# * unpacking operator
# # 1. positional 2. default 3. keyword 4. ARBITRARY

def display_name(*args):
    for arg in args:
        print(arg, end=" ")
    print()


# display_name("Dr.", "shan", "naik")


def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")


# print_address(street="asdas streer", state="Maharashtra", zip="541258")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for keys, values in kwargs.items():
        print(f"{keys} : {values}")


shipping_label("Dr.", "shan", "naik", street="asdas street", state="Maharashtra", zip="541258")
