#MULTILEVEL INHERITANCE
class Dad:
    Basketball=1

class Son(Dad):
    Dance=1
    def isdance(self):
        return f"I can dance {self.Dance} no of times"

class Grandson(Son):
    Dance=6
#the below is an overriding function because it is same as in son class , simply we can inherit from the son class

    # def isdance(self):
    #     return f"I can dance {self.Dance} no of times"

larry=Dad()
darry=Son()
harry=Grandson()
print(harry.isdance())
print(harry.Basketball)

