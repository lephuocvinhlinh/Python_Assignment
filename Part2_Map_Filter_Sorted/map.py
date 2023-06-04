#Map
#1
def function_round(lst):
    return int(lst)

def round_lst(lst):
    lst = map(function_round, lst)
    lst = list(lst)
    return lst
print(round_lst([10.8932, 12.434, 13.65656]))
# 2
def square(x):
    return x**2

def square_lst(lst):
    lst = map(square, lst)
    lst = list(lst)
    return lst
print(square_lst([2, 4, 6]))