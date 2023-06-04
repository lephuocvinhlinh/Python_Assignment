from collections import defaultdict

#bai1
print("Bai 1: ")
keys = ['key_1', 'key_2', 'key_3']
values = ['values1','values2', 'values3']
my_dictionary = dict(zip(keys, values))
print(my_dictionary)

#bai2
print("Bai 2: ")
dictionary = {"key_1": "value_1", "key_2": "value_2", "key_3": "value_3"}
lst_1 = ["key_1", "key_4"]
lst_2 = ["key_2", "key_3"]

set1 = set(lst_1)
set2 = set(lst_2)
print(set1.issubset(dictionary))
print(set2.issubset(dictionary))

#bai3
print("Bai 3: ")
dictionary = {"key_1": "value_1", "key_2": "value_2", "key_3": "value_3"}
key = "key_1"
dictionary.pop(key)
print(dictionary)

#bai4
print("Bai 4: ")
dict_1 = {1: 10, 2: 20}
dict_2 = {3: 30, 4: 40}
dict_3 = {5: 50, 6: 60}
dict_4 = {}
for i in (dict_1, dict_2, dict_3): dict_4.update(i)
print(dict_4)

#bai5
print("Bai 5: ")
my_dict = {"key_1": ["value_1", "value_2"], "key_2": ["value_3", "value_4", "value_5"]}
count = 0
for i in my_dict:
    if (isinstance(my_dict[i], list)):
        count += len(my_dict[i])
print(count)

#bai6
print("Bai 6: ")
dict1 = ["the", "purpose", "of", "our", "lives", "is", "to", "be", "happy"]
d = defaultdict(list)
for key in dict1:
    d[len(key)].append(key)
print(dict(d))