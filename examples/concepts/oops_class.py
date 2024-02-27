class Car:
    def __init__(self,name,price,no_of_seaters):
        self.name = name
        self.price = price
        self.no_of_seaters = no_of_seaters
    def display(self):
        print("Car name is",self.name)
        print("Car price is",self.price)
    def withno_of_seaters(self):
        print("no_of_seaters is ",self.no_of_seaters)
    def discount(self):
        print(self.price-0.2*self.price)

myCar1 = Car("Audi",10000,2)
myCar1.display()
myCar1.withno_of_seaters()
myCar1.discount()

myCar2 = Car("Mercedes",20000,4)
myCar2.display()
myCar2.withno_of_seaters()
myCar2.discount()
