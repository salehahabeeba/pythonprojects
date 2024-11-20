# SELF AND INIT CONSTRUCTOR
class Employee:
    no_of_leaves=8 #class variable
    def __init__(self,name , role,salary):
        self.name=name
        self.role=role
        self.salary=salary
#we can also pass default attribute which is common to all the objects same as class variable
        self.address="Hyderabad"

#init make the code less we dont have to write the same code for every person again and again like in the line 17 18 19
#we can just pass the arguments in the line 14
    def printdetails(self):
        return f"The name is {self.name}. Salary is {self.salary} and the role is {self.role}"

Harry= Employee("Harry","instructor",3300)
Rohan= Employee("Rohan","student",330)

# Harry.name= "Harry"
# Harry.role= "instructor"
# Harry.salary=3300
#
# Rohan.name= "Rohan"
# Rohan.role= "Student"
# Rohan.salary=330
# print(Rohan.printdetails())
print(Rohan.address)