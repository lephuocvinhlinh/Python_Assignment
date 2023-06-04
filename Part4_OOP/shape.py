from abc import ABC, abstractmethod

#Create abstract class Shape with methods calculate_perimeter() and calculate_area()

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass
    
    @abstractmethod
    def calculate_area(self):
        pass

#Creata a child class Rectangle, inherited from class Shape
class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_perimeter(self):
        return 2 * (self.height + self.width)

    def calculate_area(self):
        return self.height * self.width

##Creata a child class Square, inherited from class Shape
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return 4 * self.side

    def calculate_area(self):
        return self.side ** 2

#Creata a child class Triangle, inherited from class Shape
class Triangle(Shape):
    def __init__(self, sides):
        self.sides = sides

    def calculate_perimeter(self):
        return sum(self.sides)

    def calculate_area(self):
        #a, b, c = self.sides
        #p = (a + b + c) / 2
        #return (p * (p - a) * (p - b) * (p - c)) ** 0.5
        p = self.calculate_perimeter() / 2
        return (p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2])) ** 0.5

#Test case for class child Rectangle
r = Rectangle(3,6)
print(r.calculate_perimeter()) 
print(r.calculate_area()) 
print(end = '\n')

#Test case for class child Square
s = Square(5)
print(s.calculate_perimeter())
print(s.calculate_area())
print(end = '\n')

#Test case for class child Triangle
t = Triangle((3, 4, 5))
print(t.calculate_perimeter()) 
print(t.calculate_area()) 