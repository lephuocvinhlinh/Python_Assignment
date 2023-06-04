
#Define a function.
def isPalindrome(string):
# input : type string 
# output : type bool   
    if (string == string[::-1]) :
        return True
    else:
        return False
#Enter input string.
string = input ("Enter string: ")

print(isPalindrome(string))