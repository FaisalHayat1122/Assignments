# 8. The super() Function

# Parent/Super class
class Person:
    def __init__(self, name:str):
        self.name = name

    def display(self):
        print(f"Person Name: {self.name}")

# Child class inheriting from Person
class Teacher(Person):        
    def __init__(self, name:str, subject:str):
        # Call the constructor of the parent class
        super().__init__(name)
        self.subject  = subject

    def display(self):
            return f"Teacher Name: {self.name}, Subject: {self.subject}"
        
teacher = Teacher("Faisal", "Python")
print(teacher.display())        