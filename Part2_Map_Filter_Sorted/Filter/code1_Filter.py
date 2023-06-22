nums = input().split()
nums = [int(element) for element in nums]

new_nums = list(filter(lambda x: x > 0, nums))

print(new_nums)
