class Employee:
    def __init__(self,name,salary,bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus
    def display(self):
        print("Employee name is",self.name)
        print("Employee salary is",self.salary)
    def withbonus(self):
        print("Bonus is ", self.salary+self.bonus)

myemployee1 = Employee("John",1000,500)
myemployee1.display()
myemployee1.withbonus()

myemployee2 = Employee("Pranjal",10000,5000)
myemployee2.display()
myemployee2.withbonus()
