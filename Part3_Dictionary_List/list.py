def concat_index_wise(lst1, lst2):
    result = []
    if(len(lst1) == len(lst2)):
        for ind, ele1 in enumerate(lst1):
            if(type(ele1) == type(str()) and type(lst2[ind]) == type(str())):
                result.append(ele1 + lst2[ind])
        return result

def concat_two_list(lst1, lst2):
    return lst1 + lst2

def simultaneously(lst1, lst2):
    if(len(lst1) == len(lst2)):
        result = zip(tuple(lst1), tuple(lst2))
    return list(result)

def remove_empty(lst):
    for ele in lst:
        if(ele == ""):
            lst.remove(ele)
    return lst

def remove_20(lst):
    res = [i for i in lst if i != "20"]
    return res

def sort_list_of_dict(list):
    result = sorted(list, key=lambda d: d['model'], reverse=True) 
    return result


