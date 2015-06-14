__author__ = 'sdlee'

#Variable-length arguments
def sum( arg1, *tuple ):
    sum = arg1
    for i in tuple:
        sum = sum + i
    print "Sum of arguments: %s" %(sum)
    return;

# Now you can call printinfo function
sum( 10 );
sum( 70, 60, 50 );


