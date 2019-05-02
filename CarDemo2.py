import Vehicle
import Car

# Notice the imports are different than in CarDemo1

# A demo file to test drive our new Car class

my_18_wheeler = Vehicle.Vehicle(18)  # Different than in CarDemo1

print "My Big Rig has %d wheels." % my_18_wheeler._numberOfTires

my_car = Car.Car()  # Different than in CarDemo1

print "My new car has %d wheels." % my_car._numberOfTires


# A polymorphic function
# Can accept a Vehicle, a Car, anything with a getDescription() method.
def print_description(foo):
    print foo.getDescription()


print_description(my_18_wheeler)
print_description(my_car)
