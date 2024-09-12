import csv
import json

file_path = "output.csv"

# try:
#     with open(file_path, "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("file not found")

# try:
#     with open(file_path, "r") as file:
#         content = json.load(file)
#         print(content["name"])
#         print(content["age"])
# except FileNotFoundError:
#     print("file not found")

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[0])
except FileNotFoundError:
    print("file not found")