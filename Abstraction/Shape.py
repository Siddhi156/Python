from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self, radius):
       print("Area of Circle: = 7.85")

c = Circle()
c.area(5)