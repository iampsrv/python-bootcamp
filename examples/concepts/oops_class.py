class Car:
    def __init__(self,name,price,no_of_seaters,color):
        self.name = name
        self.price = price
        self.no_of_seaters = no_of_seaters
        self.color=color
    def display(self):
        print("Car name is",self.name)
        print("Car price is",self.price)
    def withno_of_seaters(self):
        print("no_of_seaters is ",self.no_of_seaters)
    def discount(self):
        print(self.price-0.2*self.price)
    def colorofcar(self):
        print("Color of car is ", self.color)

myCar1 = Car("Audi",10000,2,"red")
myCar1.display()
myCar1.withno_of_seaters()
myCar1.discount()
myCar1.colorofcar()

myCar2 = Car("Mercedes",20000,4,"black")
myCar2.display()
myCar2.withno_of_seaters()
myCar2.discount()
myCar2.colorofcar()