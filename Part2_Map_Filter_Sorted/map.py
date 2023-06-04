#bai1
list_numbers = [1.23, 2.1, 3.44, 4.51]

map_iterator = map(lambda x: int(x), list_numbers)
my_list = list(map_iterator)
print(my_list)


#bai3
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