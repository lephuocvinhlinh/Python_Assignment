import itertools

# Create groups of similar items of a given list
def group_similar_items(my_list):
    group_key = lambda x: x.split()[-1]
    sorted_list = sorted(my_list, key = group_key)
    result = [list(group) for key, group in itertools.groupby(sorted_list, group_key)]
    return result

# my_list = input().split(",")
my_list = ["Thomas Brown", "Tom Smith", "Jane Brown", "John Smith"]
result = group_similar_items(my_list)
print(result)
print(end = '\n')

# Combine two lists into a new list
def combine_lists(lst1, lst2):
    return list(itertools.chain(lst1, lst2))

lst1 = [["We", "are"], "Novobi"]
lst2 = ["We", ["are", "Novobi"]]
result = combine_lists(lst1, lst2)
print(result) 
print(end = '\n')

# Generate unique combinations
my_list = ["Red", "Yellow", "Green"]
result = [" - ".join(pair) for pair in itertools.combinations(my_list, 3)]
print(result)
print(end = '\n')

# Group all iterables together and produce a single iterable
lst_1 = [1, 4, 7, 10, 13, 16]
lst_2 = [2, 5, 8, 11, 14, 17]
lst_3 = [3, 6, 9, 12, 15, 18]

print(list(itertools.chain(*[lst_1, lst_2, lst_3])))
print(end = '\n')

# Display elements in an iterable in the group of length
my_list = ["keep", "smiling", "because", "life", "is", "a", "beautiful", "thing", "and", "there", "is", "so", "much", "to", "smile", "about"]

def get_length(item):
    return len(item)

result = {}
for key, group in itertools.groupby(sorted(my_list, key = get_length), get_length):
    result[key] = list(group)

for key, group in result.items():
    print("Key: {} - Group: {}".format(key, group))
print(end = '\n')