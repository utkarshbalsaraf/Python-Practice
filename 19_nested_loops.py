# for x in range(1, 11):
#     for y in range(1, 10):
#         print(y, end="-")
#     print()


rows = int(input("Enter the number of rows\n"))
columns = int(input("Enter the number of columns\n"))
symbols = input("Enter the Symbol\n")

for x in range(rows):
    for y in range(columns):
        print(symbols, end="")
    print()
