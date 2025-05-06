class Product:
    def __init__(self, price):
        self._price = price  # Private attribute (conventionally)

    # Getter
    @property
    def price(self):
        return self._price

    # Setter
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    # Deleter
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Example usage
p = Product(100)

# Accessing the price
print(p.price)  # Output: 100

# Updating the price
p.price = 150
print(p.price)  # Output: 150

# Deleting the price
del p.price
