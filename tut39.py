#SUPER() AND OVERRIDING
class A:
    classvar1="I am a class variable in class A"

    def __init__(self):
        self.var1="I am a variable in class A's constructor"
        self.classvar1="I am an instance varibale of class A"
class B(A):

    #classvar1="I am a class variable in class B"

    def __init__(self):
        #super().__init__()
        self.var1="I am a variable in class B's constructor"
        self.classvar1="I am an instance varibale of class B"
        super().__init__()


a=A()
b=B()
print(b.classvar1)
