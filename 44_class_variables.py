# class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

class Student:
    num_students = 0
    class_year = 2022

    def __init__(self, name):
        self.name = name
        Student.num_students += 1


student = Student("Utkarsh")
student1 = Student("Utkarsh")
student2 = Student("Utkarsh")

print(student.class_year)
print(Student.class_year)
print(Student.num_students)
