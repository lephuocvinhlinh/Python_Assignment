class fibonancciGenerator:
    def __init__(self):
      self.value = 0
      self.prev_value = 1
      self.type = 0
    def get_type(self):
        return self.type
    def get_value(self):
        return self.value
    def get_prev_value(self):
        return self.prev_value
    def set_value(self, a):
        self.value = a
    def set_prev_value(self, a):
        self.prev_value = a
        
class multipleBy:
    def __init__(self, a):
        self.value = a
        self.index = 1
        self.type = 1
    def get_type(self):
        return self.type
    def get_value(self):
        return self.value * self.index
    def get_index(self):
        return self.index
    def set_index (self, a):
        self.index = a

class exponentialBy:
    def __init__(self, a):
        self.value = a
        self.index = 1
        self.type = 2
    def get_type(self):
        return self.type
    def get_value(self):
        return pow(self.index, self.value)
    def get_index(self):
        return self.index
    def set_index (self, a):
        self.index = a

def next(a):
    if (a.get_type == 0):
        x = a.get_value()
        a.set_value(a.get_value() + a.get_prev_value())
        print(a.get_value())
        a.set_prev_value(x)
    elif (a.get_type() == 1):
        print(a.get_value())
        a.set_index(a.get_index() + 1)
    
