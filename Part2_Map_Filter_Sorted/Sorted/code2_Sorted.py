nums = input().split()
nums = [int(element) for element in nums]
nums = sorted(nums, reverse=True)
print(nums)
