num1 = int(input("Enter the first Number\n"))
num2 = int(input("Enter the Second Number\n"))
operator = input("Enter the Operation +,-,*,/\n")

if operator == "+":
    print(f"Addition : {num1+num2}")
if operator == "-":
    print(f"Subtraction : {num1-num2}")
if operator == "*":
    print(f"Multiplication : {num1*num2}")
if operator == "/":
    print(f"Division : {num1/num2}")
else:
    print("Enter valid operation")
