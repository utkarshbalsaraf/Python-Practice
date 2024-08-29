principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount\n"))
    if principle <= 0:
        print("Principle cant be less than 0")

while rate <= 0:
    rate = float(input("Enter the Interest percentage\n"))
    if rate <= 0:
        print("Principle cant be less than 0")

while time <= 0:
    time = int(input("Enter the Time in Years\n"))
    if time <= 0:
        print("Principle cant be less than 0")

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} years is ${total:.2f}")
