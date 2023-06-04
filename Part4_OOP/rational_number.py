import math

# Create class RationalNumber with attributes numerator and denominator, default = 1
class RationalNumber:
    def __init__(self, numerator, denominator=1):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise NotIntegerError("Numerator or Denominator is not an integer")
        elif denominator == 0:
            raise ZeroDenominatorError("Denominator cannot be zero")
        gcd_value = math.gcd(numerator, denominator)
        self.numerator = numerator // gcd_value
        self.denominator = denominator // gcd_value

    def simplify(self):
        gcd_value = math.gcd(self.numerator, self.denominator)
        return RationalNumber(self.numerator // gcd_value, self.denominator // gcd_value)

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        else:
            return str(self.numerator) + "/" + str(self.denominator)

    def __add__(self, other):
        numerator = self.numerator * other.denominator + self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return RationalNumber(numerator, denominator).simplify()

    def __sub__(self, other):
        numerator = self.numerator * other.denominator - self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return RationalNumber(numerator, denominator).simplify()

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return RationalNumber(numerator, denominator).simplify()

    def __truediv__(self, other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return RationalNumber(numerator, denominator).simplify()

    def __lt__(self, other):
        return self.numerator * other.denominator < self.denominator * other.numerator

    def __gt__(self, other):
        return self.numerator * other.denominator > self.denominator * other.numerator

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

# Exception hierarchy which defines a different exception for each of these error conditions
class NotIntegerError(Exception):
    pass

class ZeroDenominatorError(Exception):
    pass

#Test case for question 7
print(RationalNumber(15, 20).simplify())
print(end = '\n')

#Test case for question 8
print(RationalNumber(4, 6)) 
print(RationalNumber(5, 1))
print(end = '\n')

#Test case for question 9
r1 = RationalNumber(1, 2)
r2 = RationalNumber(1, 3)
print(r1 + r2) 
print(r1 - r2) 
print(r1 * r2) 
print(r1 / r2) 
print(end = '\n')

#Test case for question 10
r1 = RationalNumber(3, 7)
r2 = RationalNumber(4, 9)
print(r1 > r2) 

r1 = RationalNumber(3, 7)
r2 = RationalNumber(4, 11)
print(r1 < r2) 

r1 = RationalNumber(2, 4)
r2 = RationalNumber(4, 8)
print(r1 == r2) 