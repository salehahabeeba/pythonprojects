#ABSTRACT BASE CLASS AND @abstractmethod
# from abc import ABCMeta , abstractmethod
                #OR
from abc import ABC , abstractmethod

# class Shape(metaclass=ABCMeta):
            #OR
class Shape(ABC):

    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type="rectangle"
    sides=4
    def __init__(self):
        self.length=6
        self.breadth=5
    def printarea(self):
        return self.length * self.breadth


rect1=Rectangle()
print(rect1.printarea())