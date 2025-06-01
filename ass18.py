# 8. Property Decorators: @property, @setter, and @deleter
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        """Get the price of the product."""
        return self._price
    

    @price.setter
    def price(self, value):
        """Set the price of the product."""
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value   


    @price.deleter
    def price(self):
        """Delete the price of the product."""
        print("Deleting price...")
        del self._price

p = Product(100)
print(p.price)  # Output: 100

p.price = 150
print(p.price)  # Output: 150

del p.price