class Product:

    def __init__(self,name,price,quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
    
    def get_total_cost(self):
        return self.__price * self.__quantity

# product1 = Product("chair",100,5)
# print(product1.__name)
# print(product1.__price)
# print(product1.__quantity)


# print(product1.get_total_cost())
# product1.__price=0
# print(product1.get_total_cost())


product2 = Product("table",500,10)
print(product2.__name)
print(product2.__price)
product2.__price=0
print(product2.__price)
print(product2.__quantity)

