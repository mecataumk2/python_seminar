__author__ = 'sdlee'

def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4]; # This would assig new reference in mylist
   print "Values inside the function: ", mylist
   return

# Now you can call changeme function


mylist2 = [10,20,30];
changeme( mylist2 );
print "Values outside the function: ", mylist2
