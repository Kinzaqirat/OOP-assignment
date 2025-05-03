class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Using the static method without creating an object
result = MathUtils.add(10, 20)
print("Sum:", result)
