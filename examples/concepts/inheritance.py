# Parent class: Family Member
class FamilyMember:
    def talk(self):
        print("I can talk!")

    def laugh(self):
        print("I can laugh!")

    def walk(self):
        print("I can walk!")


# Child class: Dad
class Dad(FamilyMember):
    def fix_things(self):
        print("I can fix things using a toolbox.")
    def laugh(self):
        print("I can laugh loudly!")  # Override the laugh method from the parent class

# Child class: Mom
class Mom(FamilyMember):
    def cook(self):
        print("I can cook delicious meals without using a recipe book.")
    def dance(self):
        print("I can dance.")
    def talk(self):
        print("I can talk without stop")

# Child class: Kid
class Kid(Mom,FamilyMember): # Multiple Inheritance
    def play(self):
        print("I love to play games!")
    def walk(self):
        print("I can walk slowly")  # Override the laugh method from the parent class
    def cook(self):
        print("I can cook")
    def talk(self):
        print("I can talk but not long")

dad = Dad()
mom = Mom()
kid = Kid()

# dad.talk()
# dad.fix_things()
# dad.laugh()

# mom.cook()
# mom.dance()
# mom.talk()
# mom.laugh()

kid.cook()
kid.dance()
kid.talk()
kid.laugh()