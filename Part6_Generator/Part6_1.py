class fibonancciGenerator:
    def __init__(self):
      self.value = 0
      self.prev_value = 1
    def get_value(self):
        return self.value
    def get_prev_value(self):
        return self.prev_value
    def set_value(self, a):
        self.value = a
    def set_prev_value(self, a):
        self.prev_value = a
        
def next(a):
    x = a.get_value()
    a.set_value(a.get_value() + a.get_prev_value())
    print(a.get_value())
    a.set_prev_value(x)
    
    
