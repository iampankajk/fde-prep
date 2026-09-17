from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def describe(self):
        print(f"{self.__class__.__name__} has area {self.area():.2f}")


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth


    def area(self):
        return self.length * self.breadth


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

shapes = [
    Rectangle(10, 5),   
    Square(4),          
    Circle(3),          
    Rectangle(3, 4),    
    Square(7)           
]


for shape in sorted(shapes, key=lambda shape: shape.area()):
    print(shape.describe())