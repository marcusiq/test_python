class Digit(object):
    def __init__(self, number):
        self._number = number

    def __repr__(self):
        return str(self._number)

    def __add__(self, right):
        result = Digit(10*self._number + right._number)
        return result

print Digit(4) + Digit(1) + Digit(8) + Digit(9)


print Digit(123) + Digit(4)

# It is assumed that the right digit is a single number in the range from 0 to 9.
# Otherwise problems occur.

print Digit(12) + Digit(34) # Whoops! Not what we  wanted

print Digit(12) + Digit(-2) # Whoops! Also not what we wanted