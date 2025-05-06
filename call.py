class Multiper:
    def __init__(self,factor):
        self.factor=factor
    def __call__(self, value):
        return value *self.factor


triple=Multiper(3)
print(callable(triple))
result=(10)
print(result)            