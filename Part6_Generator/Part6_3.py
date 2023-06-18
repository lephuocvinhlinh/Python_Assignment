class exponentialBy:
    def __init__(self, a):
        self.value = a
        self.index = 1
    def get_value(self):
        return pow(self.index, self.value)
    def get_index(self):
        return self.index
    def set_index (self, a):
        self.index = a

def next(a):
    print(a.get_value())
    a.set_index(a.get_index() + 1)
    
exponential = exponentialBy(3)
next(exponential)
next(exponential)
next(exponential)