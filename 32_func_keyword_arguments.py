def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")


hello("Hello", "Mr.", "John", "Doe")
hello("Mr.", "Hello", "Doe", "John")
hello(title="Mr.", greeting="Hello", last="Doe", first="John")  # giving keywords to arguments
