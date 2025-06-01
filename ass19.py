# 19. callable() and __call__()

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor


m = Multiplier(3)
# Check if m is callable
print(callable(m))
# Call m as a function
print(m(4))        