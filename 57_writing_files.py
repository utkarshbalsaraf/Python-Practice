import csv
import json

txt_data = "I like pizza"
file_path = "output.txt"

employee = ["utkarsh","shantanu","Siddhesh"]
with open(file_path, "w") as file:
    for emp in employee:
        file.write("\n" + emp)
    print(f"txt file {file_path} is created")

# employees = {"name": "utkarsh", "age": 30, "job": "cook"}
# with open(file_path, "w") as file:
#     json.dump(employees, file,indent=4)
#     print(f"json file {file_path} is created")

# employees = [["Name", "Age", "Job"],
#              ["Spongebob", 30, "Cook"],
#              ["Patrick", 37, "Unemployed"],
#              ["Sandy", 27, "Scientist"]]
# with open(file_path, "w", newline="") as file:
#     writer = csv.writer(file)
#     for row in employees:
#         writer.writerow(row)
#     print(f"csv file {file_path} is created")
