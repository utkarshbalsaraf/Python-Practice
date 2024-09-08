# Decorator = A function that extends the behavior of another function
#             w/o modifying the base function
#             Pass the base function as an argument to the decorator


def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("You added sprinkles")
        func(*args, **kwargs)

    return wrapper


def scoop_icecream(func):
    def wrapper(*args, **kwargs):
        print("you scooped the icecream")
        func(*args, **kwargs)

    return wrapper


@scoop_icecream
@add_sprinkles
def get_ice_cream(flavour):
    print(f"here is your {flavour} ice cream")


get_ice_cream("Strawberry")
