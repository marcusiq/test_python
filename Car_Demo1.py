from Vehicle import *
from Car import *

# A demo file to test drive our new Car class

my_18_wheeler = Vehicle(18)

print "My Big Rig has %d wheels." % my_18_wheeler._numberOfTires

my_car = Car() # You get a new car!

print "My new car has %d wheels." % my_car._numberOfTires


# A polymorphic function
# Can accept a Vehicle, a Car, anything with a getDescription() method.
def print_description(foo):
    print foo.getDescription()



print_description(my_18_wheeler)
print_description(my_car)