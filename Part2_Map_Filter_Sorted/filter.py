#Filter
#1
def pos(x):
    return x>0

def pos_filter(lst):
    ans = filter(pos, lst)
    return list(ans)
print(pos_filter([4, -3, 2]))

#2
def check_cap(s):
    return (s[0] == s[0].upper())

def upper_filter(lst):
    ans = filter(check_cap, lst)
    return list(ans)
print(upper_filter(["We", "are", "Novobi"]))

#3
dict = {"b": 4, "c": 5}
def check_exist(dict):
    if (dict.get("a") == None):
        return True
    return False

def exist_filter(lst):
    ans = filter(check_exist, lst)
    return list(ans)
print(exist_filter([{"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5}, {"a": 2, "c": 6}, {"b": 4, "c": 5}]))