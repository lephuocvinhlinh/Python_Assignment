class iterator_enum:
    def __init__(self, Enumerate):
        self.Enumerate = Enumerate
    def __iter__(self):
        self.ele = list(self.Enumerate)
        self.start = 0
        self.end = 0
        if(self.ele):
            self.start = self.ele[0][0]
            self.end = self.ele[-1][0]
        self.index = self.start
    
    def __next__(self):
        if(self.index > self.end):
            raise Exception("StopIteration")
        else:
            res = self.ele[self.index - self.start]
            self.index += 1
            return res

my_enum = enumerate(["a", "b", "c"], start=2)
test = iterator_enum(my_enum)
enum_iter = iter(test)
print(enum_iter.next())
print(enum_iter.next())
print(enum_iter.next())
print(enum_iter.next())


class iterator_zip:
    def __iter__(self, Zip):
        self.ele = Zip
        self.index = 0
        self.end = len(Zip)
    
    def __next__(self):
        if(self.index > self.end):
            raise Exception("StopIteration")
        else:
            res = self.ele[self.index]
            self.index += 1
            return res
        
