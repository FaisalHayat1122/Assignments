# 20. Creating a Custom Exception
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older"):
        self.message = message
        super().__init__(self.message)


def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. Must be 18 or older.")
    else:
        return f"Age {age} is valid."
    
try:
    age = int(input("Enter your age: "))
    result = check_age(age)
    print(result)

except InvalidAgeError as e:
    print(f"Error: {e.message}")




        