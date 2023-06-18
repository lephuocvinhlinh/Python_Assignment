class multipleBy:
    def __init__(self, a):
        self.value = a
        self.index = 1
    def get_value(self):
        return self.value * self.index
    def get_index(self):
        return self.index
    def set_index (self, a):
        self.index = a

def next(a):
    print(a.get_value())
    a.set_index(a.get_index() + 1)
    
multiply = multipleBy(5)
next(multiply)
next(multiply)
next(multiply)