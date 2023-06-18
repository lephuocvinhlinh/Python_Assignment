#1
def palindrome(my_str):
    my_string_re = my_str[::-1]
    if (my_str==my_string_re):
        print('True')
    else:
        print('False')

my_str = "naan"
palindrome(my_str)
#2
def division_n(lst, n):
    ans = []
    for i in range(0, n):
        temp = [] 
        for j in lst:
            if (j % n == i):
                temp.append(j)
        ans.append(temp)
    return ans
print(division_n([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  3))
#3
def split_lst(s):
    s = s.split(' ')
    return s
print(split_lst("Onboarding Python Training Session 2023"))
#4
def sum(*lst):
    ans = 0
    for i in lst:
        ans += i
    return ans
print(sum(10, 20, 30))
#5
def initialize_employee(name, gender, salary=0):
    out_dict = {}
    out_dict["name"] = name
    out_dict["gender"] = gender
    out_dict["salary"] = salary
    return out_dict
print(initialize_employee("Jayson", "Male", 10000))
print(initialize_employee("Sarah", "Female"))