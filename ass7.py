# 7. Access Modifiers: Public, Private, and Protected

class Employee:
    def __init__(self, name:str, salary:int, ssn:str):
        self.name = name # public attribute
        self._salary = salary # protected attribute
        self.__ssn = ssn # private attribute

emp = Employee("Meer", 50000, "123-45-6789")

print(emp.name) # Accessing public attribute
print(emp._salary) # Protected attribute (not recommended) but accessible
print(emp.__ssn) # Private attribute (not accessible directly)        