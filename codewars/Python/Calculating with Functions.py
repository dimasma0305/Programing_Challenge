'''
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
'''

def zero(func):
    return 0 if func is None else func()
def one(func):
    return 1

def plus(func):
    return 

print(plus(one)(1))