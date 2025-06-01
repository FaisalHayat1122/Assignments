# 16. Function Decorators
def log_function_call(func):
    def wrapper():
        print(f"Function is being called")
        func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello, Faisal!")
say_hello()       