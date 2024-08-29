import time

my_time = int(input("Enter the time in seconds\n"))

for x in reversed(range(1, my_time + 1)):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP!")
