class Enumarate:
    index = 0
    def __init__(self, a, b):
        self.list1 = a
        self.start = b
        self.index = 0
        self.type = 0
    def get_type(self):
        return self.type
    def get_list(self):
      return self.list1
    def get_start(self):
      return self.start
    def get_index(self):
      return self.index
    def set_index(self, c):
        self.index = c

class Zip:
    index = 0
    def __init__(self, a, b, c):
        self.list1 = a
        self.list2 = b
        self.list3 = c
        self.index = 0
        self.type = 1
    def get_type(self):
        return self.type
    def get_list1(self):
      return self.list1
    def get_list2(self):
      return self.list2
    def get_list3(self):
      return self.list3
    def get_index(self):
      return self.index
    def set_index(self, c):
        self.index = c

def iter(a):
    a.set_index(0)
    return a

def next(a):
    if (a.get_type() == 1):
        a.set_index(a.get_index() + 1)
        if (a.get_index() > len(a.get_list1()) or a.get_index() > len(a.get_list2()) or a.get_index() > len(a.get_list3())):
            raise TypeError("Raise StopIteration exception")
        return (a.get_list1()[a.get_index() - 1],  a.get_list2()[a.get_index() - 1],  a.get_list3()[a.get_index() - 1])
    else:
        a.set_index(a.get_index() + 1)
        if (a.get_index() > len(a.get_list())):
            raise TypeError("Raise StopIteration exception")
        return (a.get_start() + a.get_index() - 1, a.get_list()[a.get_index() - 1])
    
