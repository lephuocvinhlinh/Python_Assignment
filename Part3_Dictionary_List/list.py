def concat_index_wise(lst1, lst2):
    result = []
    if(len(lst1) == len(lst2)):
        for ind, ele1 in enumerate(lst1):
            if(type(ele1) == type(str()) and type(lst2[ind]) == type(str())):
                result.append(ele1 + lst2[ind])
        return result

def concat_two_list(lst1, lst2):
    return lst1 + lst2

