#List
#1
def Concatenate1(lst1, lst2):
    ans = []
    for i in range(0, len(lst1)):
        ans.append(lst1[i] + lst2[i])
    return ans
#print(Concatenate1(["W", "a", "Novo"], ["e", "re", "bi"]))
#2
def Concatenate2(lst1, lst2):
    ans = []
    for i in range(0, len(lst1)):
        for j in range(0, len(lst2)):
            ans.append(lst1[i] + ' ' + lst2[j])
    return ans
#print(Concatenate2( ["Hello", "World"], ["Dear", "Sir"]))

#3
def Combi(lst1, lst2):
    ans = []
    lst2.reverse()
    for i in range(0, len(lst1)):
        temp = []
        temp.append(lst1[i])
        temp.append(lst2[i])
        temp = tuple(temp)
        ans.append(temp)
    return ans
#print(Combi([10, 20, 30], [100, 200, 300]))

#4
def checkEmpty(s):
    return s != ""

def removeEmpty(lst):
    lst = filter(checkEmpty, lst)
    return list(lst)
#print(removeEmpty(["10", "20", "30", "", "40"]))

#5
def removeOccur20(lst):
    ans = [i for i in lst if (i!="20")]
    return ans
#print(removeOccur20(["10", "20", "30", "40", "20", "50"]))

#6
def sort_dict(lst):
    lst = sorted(lst, key=lambda lst: lst['color'])
    return lst
#print(sort_dict([ {"make": "Nokia", "model": 216, "color": "Black"}, {"make": "Mi Max", "model": 2, "color": "Gold"}, {"make": "Samsung", "model": 7, "color": "Blue"} ]))