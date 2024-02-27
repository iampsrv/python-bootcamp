from abc import ABC, abstractmethod

class Product(ABC):

    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    @abstractmethod
    def get_total_cost(self):
        pass

class ProductDetails(Product):

    def get_total_cost(self):
        return self._price * self._quantity

    # Optionally, you can provide getters for private attributes
    def get_price(self):
        return self._price

    def get_quantity(self):
        return self._quantity

    # Optionally, you can provide setters for private attributes
    def set_price(self, price):
        self._price = price

    def set_quantity(self, quantity):
        self._quantity = quantity

# Usage
product1 = ProductDetails("chair", 100, 5)

# Accessing the total cost through the method
print(product1.get_total_cost())  # Output: 500

# Attempting to directly modify private attributes (not recommended)
product1.set_price(0)

# Accessing the total cost again through the method
# The total cost remains the same because the private attribute was not actually modified
print(product1.get_total_cost())  # Output: 500
