class Exception:
    def __init__(self, a):
      self.er = (a == 0)
    def get_er(self):
      return (self.er != 0)

def uscln(a, b):
    if (b == 0):
        return a
    return uscln(b, a % b)

class RationalNumber(Exception):
  denominator = 1
  def __init__(self, a, b):
    
      if (Exception(b).get_er()):
        raise TypeError(" Raise ZeroDenominatorError")
      if (not type(a) is int) or (not type(b) is int):
        raise TypeError("Raise NotIntegerError")
      else:
        self.numerator = a
        self.denominator = b
  def get_numerator(self):
      return self.numerator
  def get_denominator(self):
      return self.denominator
  def simplify(self):
    temp = uscln(self.numerator, self.denominator)
    return RationalNumber(int(self.numerator / temp), int(self.denominator / temp))
  def __str__(self):
    if (self.denominator == 1):
      return "{}".format(self.numerator)
    else:
      return "{0}/{1}".format(self.numerator ,self.denominator)
  def __add__(self, a):
      return RationalNumber(self.numerator * a.get_denominator() + self.denominator * a.get_numerator(), self.denominator * a.get_denominator()).simplify()
  def __sub__(self, a):
      return RationalNumber(self.numerator * a.get_denominator() - self.denominator * a.get_numerator(), self.denominator * a.get_denominator()).simplify()
  def __mul__(self, a):
      return RationalNumber(self.numerator * a.get_numerator(), self.denominator * a.get_denominator()).simplify()
  def __truediv__(self, a):
      return RationalNumber(self.numerator *  a.get_denominator(), self.denominator * a.get_numerator()).simplify()
  def __lt__(self, a):
      return (((self - a).get_numerator() < 0) and ((self - a).get_denominator() < 0)) ;
  def __gt__(self, a):
      return (((self - a).get_numerator() > 0) and ((self - a).get_denominator() > 0)) ;
  def __eq__(self, a):
      return ((self - a).get_numerator() == 0) ;