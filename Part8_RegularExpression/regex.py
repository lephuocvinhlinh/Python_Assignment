import re

def is_valid_email(input):
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    return bool(re.match(pattern, input))

string_input = input()
print(is_valid_email(string_input))