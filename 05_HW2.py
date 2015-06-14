__author__ = 'sdlee'

def extract(arg1):
    print arg1.keys()
    for x in arg1.values():
        if x != None:
            extract(x)
    return

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
extract(tree)

# keylist = tree.keys()
# print keylist