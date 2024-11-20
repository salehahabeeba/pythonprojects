#SINGLE INHERITANCE
class Employee:
    no_of_leaves=8 #class variable
    def __init__(self,name , role,salary):
        self.name=name
        self.role=role
        self.salary=salary
#init make the code less we dont have to write the same code for every person again and again like in the line 17 18 19
#we can just pass the arguments in the line 14
    def printdetails(self):
        return f"The name is {self.name}. Salary is {self.salary} and the role is {self.role}"
#TO INHERIT TAKE THE SUPER CLASS NAME IN THE BRACKETS OF THE CURRENT CLASS NAME
class Programmer(Employee):
    def __init__(self,name , role,salary,languages):
        self.name=name
        self.role=role
        self.salary=salary
        self.languages= languages
    def printprog(self):
        return f"The name is {self.name}. Salary is {self.salary} and the role is {self.role} and the languages are{self.languages}"

Harry= Employee("Harry","instructor",3300)
Rohan= Employee("Rohan","student",330)

karan = Programmer("Karan","Programmer",55000,["Python"])
Veer= Programmer("Veer","Programmer",66000,["Python","CPP"])
print(Harry.salary)