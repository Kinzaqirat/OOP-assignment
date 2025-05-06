class A:
    def show(self):
        print("A.show() called")

class B(A):
    def show(self):
        print("B.show() called")

class C(A):
    def show(self):
        print("C.show() called")

class D(B, C):  # Diamond inheritance: D -> B -> A, D -> C -> A
    pass

# Create an object of D and call show()
d = D()
d.show()

# Print the Method Resolution Order
print(D.__mro__)
