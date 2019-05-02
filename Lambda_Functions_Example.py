
def add_numbers(x, y):
    return x + y


print "The result is a function object:", type(add_numbers)

foo = add_numbers # just another name for the same function object
print "Just a new name, still the same function object:", type(foo)

print "Are foo and add_numbers the same function object?", foo == add_numbers

# Repeat using a lambda function, aka a nameless function. LOL - Except we named it bar!!
# PEP 8 guidelines  suggest we do not assign a lambda expression but use a def instead.
# So this is for illustration purposes only.
bar = lambda x, y: x+y

print foo(500, 20)
print bar(500, 20)

