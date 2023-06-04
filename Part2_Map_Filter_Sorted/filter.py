#Function to get the list of positive numbers
my_list = [4, -3, 2]
temp = filter(lambda x: x > 0, my_list)
new_list = list(temp)
print(new_list)

#Function to get the list of words having the first letter is capotal
my_list = ["We", "are", "Novobi"]
temp = filter(lambda x: x[0].isupper(), my_list)
new_list = list(temp)
print(new_list)

#Function to get the list of dictionaries missing the key a
my_list = [{"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5}, {"a": 2, "c": 6}, {"b": 4, "c": 5}]
temp = filter(lambda x: "a" not in x, my_list)
new_list = list(temp)
print(new_list)