#MULTIPLE INHERITANCE
class Employee:
    no_of_leaves=8 #class variable
    var=8
    def __init__(self,name , role,salary):
        self.name=name
        self.role=role
        self.salary=salary

    def printdetails(self):
        return f"The name is {self.name}. Salary is {self.salary} and the role is {self.role}"

class Player:
    var=9
    no_of_games=12
    def __init__(self,name,game):
        self.name=name
        self.game=game
    def printplayers(self):
        return f"The name is {self.name}.Game is {self.game}"

class CoolProgrammer(Employee,Player): #the attributes of this class will run based on Employee bcoz we have written
    #Employee first
    languages="C++"

    def printlanguages(self):
        print(self.languages)

Harry= Employee("Harry","instructor",3300)
Rohan= Employee("Rohan","student",330)

karan = Player("Karan","Cricket")
Veer= CoolProgrammer("Veer","coolprog",89999)
Veer.printlanguages()
print(Veer.printdetails())
print(Veer.var)
print(Veer.no_of_games )
