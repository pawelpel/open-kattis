
def read_input():
    return raw_input()  #  raw_input (Python 2), input (Python 3)

class PhoneTree(dict):
    
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value


def check_phones():
    answer = True
    phones_tree = PhoneTree()

    def add_phone(phone):
        d = phones_tree
        for p in phone:
            d = d[p]
        d[0]

    for _ in range(int(read_input())):
        add_phone(read_input())
    
    def check_keys(dickt):
        keys = dickt.keys()
        if len(keys) > 1 and 0 in keys:
            return False
        return not any(not check_keys(v) for k, v in dickt.items())

    answer = check_keys(phones_tree)
    return 'YES' if answer else 'NO'

for _ in range(int(read_input())):
    print(check_phones())
