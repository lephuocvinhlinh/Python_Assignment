#Function to convert data type
my_list = [10.8932, 12.434, 13.65656]
temp = map(int, my_list)
new_list = list(temp)
print(new_list)

#Function to square the elements of a list Check multiple keys exists in a dictionary
my_list = [2, 4, 6]
temp = map(lambda x: x**2, my_list)
new_list = list(temp)
print(new_list)

#Function to count the same pair in two given lists
lst_1 = [1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9]
lst_2 = [1, 2, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8]

count = 1
temp = map(tuple, zip(lst_1, lst_2))
result = set(temp)
for elem in result:
    if lst_1.count(elem[0]) > 1 and lst_2.count(elem[1]) > 1:
        count += 1

print(count)