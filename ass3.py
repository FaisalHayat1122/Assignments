# 3. Public Variables and Methods
class Car:
    def __init__(self, brand:str):
        self.brand = brand #instance variable

    def start(self):
        print(f"{self.brand} is starting.....")    
        
my_car = Car("Tesla")        
my_car.start()
# Public variables are by default in Python.