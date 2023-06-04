import math
lst = input().split()
lst = [float(num) for num in lst]

result = map(math.floor, lst)
print(list(result))

