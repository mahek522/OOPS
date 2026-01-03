#Implementing abstraction
from abc import ABC, abstractmethod
from math import pi
class Shape(ABC):
    
    def __init__(self):
        self.area = 0
    @abstractmethod
    def take_input(self):
        pass
    @abstractmethod
    def find_area(self):
        pass
    @abstractmethod
    def disp_area(self):
        pass
class  Circle(Shape):
    def __init__(self):
        super().__init__()
        self.radius = 0
    def take_input(self):
        self.radius = float(input("Enter radius of circle: "))
    def find_area(self):
        self.area = pi * self.radius * self.radius
    def disp_area(self):
        print("Area of circle is:", self.area)
class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        self.length = 0
        self.breadth = 0
    def take_input(self):
        self.length = float(input("Enter length of rectangle: "))
        self.breadth = float(input("Enter breadth of rectangle: "))
    def find_area(self):
        self.area = self.length * self.breadth
    def disp_area(self):
        print("Area of rectangle is:", self.area)
class Triangle(Shape):
    def __init__(self):
        super().__init__()
        self.base = 0
        self.height = 0
    def take_input(self):
        self.base = float(input("Enter base of triangle: "))
        self.height = float(input("Enter height of triangle: "))
    def find_area(self):
        self.area = 0.5 * self.base * self.height
    def disp_area(self):
        print("Area of triangle is:", self.area)
def geometric_shape(ref):
    ref.take_input()
    ref.find_area()
    ref.disp_area()
def main():
    c = Circle()
    r = Rectangle()
    t = Triangle()
    print("For Circle:")
    geometric_shape(c)
    print("For Rectangle:")
    geometric_shape(r)
    print("For Triangle:")
    geometric_shape(t)
if __name__ == "__main__":
    main()
    