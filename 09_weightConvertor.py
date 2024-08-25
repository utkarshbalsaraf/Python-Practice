weight = float(input("Enter your weight\n"))
unit = input("Kilograms or Pounds? (k or l): \n")

if unit == "k":
    print(f"Weight in Pounds is {round(weight*2.205, 2)} Lbs")
elif unit == "l":
    print(f"Weight in kilograms is {round(weight/2.205, 2)} kg")
else:
    print("give valid operation")
