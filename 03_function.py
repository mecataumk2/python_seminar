
print __file__

global_variable = 1

def print_me( arg1, arg2 ):
    "This prints a passed string into this function"
    print "Print arg1: " +  arg1
    print "Print arg2: " +  arg2
    concat = arg1 + '+' + arg2
    return concat

def func1():
    print 'nothing'
    func2()


def func2():
    print 'nothing 2'

print func1

func1()

ret_value = print_me("this is argument", "this is second argument")
print "return value: " + ret_value





