data = {}

for i in range(3):
    key = input("Enter employee's name: ")
    value = input("Enter employee's salary: ")

    data[key] = value

key_check = input().split()


keys_exist = all(key in data for key in key_check)
print(keys_exist)
