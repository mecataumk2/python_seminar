__author__ = 'sdlee'

def print_keys(arg1):
    print arg1.keys()
    for x in arg1.values():
        if x != None:
            print_keys(x)
    return

# def print_keys(arg1):
#     #print arg1.keys()
#     array = arg1.keys()
#     for x in arg1.values():
#         if x != None:
#             array.append(print_keys(x))
#
#     return array

# def print_keys(arg1):
#     for i in arg1.keys():
#         print i
#         print_keys(arg1.values())



tree = {
    '01': {
        '01-01': None,
        '01-02': None,
        '01-03': None,
        '01-04': None,
        '01-05': {
            '01-05-01': None,
            '01-05-02': None,
            '01-05-03': None,
            '01-05-04': None
        }
    }
}
print_keys(tree)