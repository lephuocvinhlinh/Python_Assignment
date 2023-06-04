#Function to check whether a passed string is a palindrome or not
def is_palindrome(string):
    string = string.lower()
    if string == string[::-1]:
        return True
    else:
        return False

#Test case 
string = "banana"
print(is_palindrome(string))

#Function returns a list of lists where each list stores elements with the same remainder after dividing by n
def remainder_list(lst, n):
    result = [[] for i in range(n)]
    check = False
    for num in lst:
        remainder = num % n
        if(remainder == 0):
            check = True
        result[remainder].append(num)
    if(check):
        first = result.pop(0)
        result.append(first)
    return result

#Test case
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3
print(remainder_list(lst, n))

#Function to split a string into a list of words
string = "Onboarding Python Training Session 2023"
result = string.split()
print(result)

#Function with variable length of arguments and calculate the total
def sum(*args):
    result = 0
    for num in args:
        result += num
    return result

#Test case 1
result1 = sum(10, 20, 30)
print(result1)

#Test case 2
result2 = sum(10, 20)
print(result2)

#Function that accept the employee's name and return basic information
def initialize_employee(name, gender, salary = 0):
    employee = {
        "name" : name,
        "gender" : gender,
        "salary" : salary
    }
    return employee

# Test case 1
employee1 = initialize_employee("Jayson", "Male", 10000)
print(employee1)

# Test case 2
employee2 = initialize_employee("Sarah", "Female")
print(employee2)