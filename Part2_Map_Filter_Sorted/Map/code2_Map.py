import math
lst = input().split()
lst = [int(num) for num in lst]

result = map(lambda x: int(math.pow(x, 2)), lst)
print(list(result))
