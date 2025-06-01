# 1. Using self
class Student:
    def __init__(self, name:str, marks:int):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student Name: {self.name}, Marks: {self.marks}")
student_details = Student("John Doe", 85)
student_details.display()

