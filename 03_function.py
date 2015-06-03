def print_me( s ):
    "This prints a passed string into this function."
    print s
    return

def add(arg1, arg2):
    sum = arg1 + arg2
    return sum

print "print_me"

print_me("call print_me")
print add(10, 20)