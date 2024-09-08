import os

file_path = "test.txt"
if os.path.exists(file_path):
    print(f"the location '{file_path}' exists")
    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("this is a folder")
else:
    print("The location doesn't exist")
