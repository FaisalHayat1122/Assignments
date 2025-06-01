# 10. Instance Methods
class Dog:
    def __init__(self, name:str, breed:str):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"

dog = Dog("Bruno", "Labrador")
print(dog.bark())        