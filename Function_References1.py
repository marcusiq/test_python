def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


# Now define a dictionary of function references
mops = {"add": add, "sub": sub, "mul": mul, "div": div}


def do_math(operation, x, y):
    if not operation in mops:
        ans = 0
    else:
        ans = mops[operation](x, y)
    print "%s %i %i \t-> %i" % (operation, x, y, ans)


do_math("add", 1, 2)

