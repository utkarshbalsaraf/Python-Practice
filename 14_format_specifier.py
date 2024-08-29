# format specifiers = {value: flags} format a value based on what
# flags are inserted

price1 = 45123.1453
price2 = -945.234
price3 = 45712.12

print(f"Price 1 is ${price1:.2f}")
print(f"Price 2 is ${price2:.1f}")
print(f"Price 3 is ${price3:.4f}\n")

print(f"Price 1 is ${price1:10}")
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:10}\n")

print(f"Price 1 is ${price1:010}")
print(f"Price 2 is ${price2:010}")
print(f"Price 3 is ${price3:010}\n")

print(f"Price 1 is ${price1:<10}")
print(f"Price 2 is ${price2:<10}")
print(f"Price 3 is ${price3:<10}\n")

print(f"Price 1 is ${price1:>10}")
print(f"Price 2 is ${price2:>10}")
print(f"Price 3 is ${price3:>10}\n")

print(f"Price 1 is ${price1:^10}")
print(f"Price 2 is ${price2:^10}")
print(f"Price 3 is ${price3:^10}\n")

print(f"Price 1 is ${price1:+}")
print(f"Price 2 is ${price2:+}")
print(f"Price 3 is ${price3:+}\n")

print(f"Price 1 is ${price1:,}")
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}\n")

print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:10}\n")
