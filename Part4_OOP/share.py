from abc import ABC, abstractmethod
import math
import array as arr 

class Shape:
  @abstractmethod
  def calculate_perimeter(self):
      pass
  @abstractmethod
  def calculate_area(self):
      pass

class Rectangle(Shape):
    
    def __init__(self, a, b):
      self.height = a
      self.width = b

    def calculate_perimeter(self):
      return (self.height + self.width) * 2
    def calculate_area(self):
      return (self.height * self.width)

class Square():
    def __init__(self, a):
      self.side = a
    def calculate_perimeter(self):
      return (self.side * 4)
    def calculate_area(self):
      return (self.side * self.side)

class Triangle():
    def __init__(self, tuple):
      self.sides = arr.array('i', tuple)

    def calculate_perimeter(self):
      return (self.sides[0] + self.sides[1] + self.sides[2])
    def calculate_area(self):
      return math.sqrt(self.calculate_perimeter() * (self.calculate_perimeter() - self.sides[0]) * (self.calculate_perimeter() - self.sides[1])  * (self.calculate_perimeter() - self.sides[2]))