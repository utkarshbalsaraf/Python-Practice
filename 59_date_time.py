import csv
import datetime

date = datetime.date(2025, 1, 23)
print(date)

today = datetime.date.today()
print(today)

time = datetime.time(12, 30, 15)
print(time)

now = datetime.datetime.now()
now = now.strftime("%H:%M:%S %m-%d-%Y")
print(now)

target_datetime = datetime.datetime(2025, 1, 2, 12, 30, 3)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("target date has not passed")
