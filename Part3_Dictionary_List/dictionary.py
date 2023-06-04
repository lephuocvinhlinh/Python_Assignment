
class Dictionary:
    def __init__(self):
        self.my_dict = {}
    def get_dict(self):
        return self.my_dict
    def map_list_to_dict(self, keys, values):
        if(len(keys) == len(values)):
            for ind, key in enumerate(keys):
                self.my_dict[key] = values[ind]
            return self.my_dict
        else:
            raise "Error"
    def check_exist(self, keys):
        for key in keys:
            if(key not in self.my_dict.keys()):
                return False
        return True
    def remove_key(self, key):
        if(key in self.my_dict.keys()):
            self.my_dict.pop(key)
            return self.my_dict
        else:
            print("Key not exist")
    def concatenate(self, *dicts):
        result = {}
        for d in dicts:
            result.update(d.get_dict())
        return result
    def count_num_of_items(self):
        count = 0;
        for value in self.my_dict.values:
            if(type(value) == type(list())):
                count += len(value)
        return count
    def group_elements(self, input):
        result = {}
        for ip in input:
            key = str(len(ip))
            if key not in result.keys():
                result[key] = []
            result[key].append(ip)
        return result
            