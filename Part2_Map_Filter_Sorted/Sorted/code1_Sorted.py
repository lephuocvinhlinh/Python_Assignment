nums = input().split()
nums = [int(element) for element in nums]

nums.sort(reverse=True)
print(nums)