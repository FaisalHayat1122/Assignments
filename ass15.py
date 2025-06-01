# 15. Method Resolution Order (MRO) and Diamond Inheritance

class A:
    def show(self):
        print("Hello from A")

class B(A):
    def show(self):
        print("Hello from B")

class C(A):
    def show(self):
        print("Hello from C")

class D(B, C):
    pass

# Create an instance of D
d = D()

# Check the method resolution order
print(D.mro())

# Call the show method
d.show()