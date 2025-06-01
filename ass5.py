# 5. Static Variables and Static Methods
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

static_method = MathUtils()
print(static_method.add(5, 10))
# Static method does not take self or cls as first parameter.
