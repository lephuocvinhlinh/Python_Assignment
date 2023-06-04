def palindrome(my_str):
    my_string_re = my_str[::-1]
    if (my_str==my_string_re):
        print('True')
    else:
        print('False')

my_str = "naan"
palindrome(my_str)

def sum(*tong):
   sum = 0
   for i in tong:
       sum += i
   return sum

print(sum(1, 2, 3))
