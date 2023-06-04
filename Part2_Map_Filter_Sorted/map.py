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
#3
def check(x, y):
    if(x == y):
        return 1
    else:
        return 0
lst_1 = [1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9]
lst_2 = [1, 2, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8]
map_iterator = map(lambda x, y: check(x, y), lst_1, lst_2)
my_list = list(map_iterator)
sum = 0
for i in my_list:
    sum += i
print(sum)