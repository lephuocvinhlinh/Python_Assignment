data = [{"a": 1, "b": 2, "c": 3}, 
        {"b": 4, "c": 5}, 
        {"a": 2, "c": 6}, 
        {"b": 4, "c": 5}]

letter = input()
data = list(data)
result = filter(lambda x: letter not in x, data)
output = list(result)

print(output)
