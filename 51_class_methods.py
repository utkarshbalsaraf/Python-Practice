# Class methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself.

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data
# Class methods = Best for class-level data or require access to the class itself


class Students:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Students.count += 1
        Students.total_gpa += gpa

    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total # of students : {cls.count}"

    @classmethod
    def avg_gpas(cls):
        if cls.count == 0:
            return 0
        else:
            return f"total gpa is {cls.total_gpa/cls.count}"



student1 = Students("shan", 3.2)
student2 = Students("siddhu", 4.5)
print(Students.get_count())
print(Students.avg_gpas())
