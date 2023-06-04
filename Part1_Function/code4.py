def sum(lst):
    total = 0
    for num in lst:
        total += int(num)
    return total

# Example usage
lst = input().split()
print(sum(lst))
