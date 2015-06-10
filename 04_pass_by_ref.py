__author__ = 'sdlee'

# Function definition is here
def changeme( arg1 ):
    "This changes a passed list into this function"
    result=arg1.upper()
    print "Values inside the function: ", result
    return

mylist = "hi. sdlee."
changeme( mylist )
print "Values outside the function: ", mylist