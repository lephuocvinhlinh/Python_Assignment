lst_1 = input().split()
lst_1 = [int(num) for num in lst_1]

lst_2 = input().split()
lst_2 = [int(num) for num in lst_2]

count = sum(list(map(lambda x, y: 1 if x == y else 0, lst_1, lst_2)))

print(count)
