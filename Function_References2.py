# Same as function references #1, but now with lambda functions.
mops = {
    "add": lambda x, y: x + y,
    "sub": lambda x, y: x - y,
    "mul": lambda x, y: x * y,
    "div": lambda x, y: x / y,
    "rem": lambda x, y: x % y  # let's add remainder operator
}


# the next method is unchanged
def do_math(operation, x, y):
    # This if/else construct is rather messy. Let's replace it with something better.
    # if not operation in mops: ans = 0
    # else: ans = mops[operation](x, y)
    # Here's a two-line version.
    # foo = mops.get(operation, lambda x, y: 0)  # assigns anonymous zero-function if operation is not in the dictionary
    # ans = foo(x, y)
    ans = mops.get(operation, lambda x0, y0: 0)(x, y) # the change to x0 & y0 avoids shadowing x & y, but not necessary
    # Here's a one-line version
    print "%s %i %i \t-> %i" % (operation, x, y, ans)
    # print "%s %d %d \t-> %d" % (operation, x, y, ans) # alternative


do_math("add", 1, 2)
do_math("sub", 50, 2)
do_math("mul", 9, 5)
do_math("div", 9, 5)
do_math("rem", 9, 5)  # We added remainder operator
do_math("nop", 9, 5)  # Ack! Nope!! not an operation in our dictionary.

# Typical output
# add 1 2 	-> 3
# sub 50 2 	-> 48
# mul 5 5 	-> 45
# div 9 5 	-> 1
# rem 9 5 	-> 4
# nop 9 5 	-> 0
