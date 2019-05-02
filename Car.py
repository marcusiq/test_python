# import the superclass
from Vehicle import *
# Blueprint for the subclass named Car
# All cars have 4 wheels (our assumption)
# Car is a subclass of Vehicle, aka a child class.

class Car(Vehicle):
    def __init__(self):
        super(Car, self).__init__(4) # Calls the constructor from the superclass Vehicle
        self._plateNumber = None  # you can't drive without a license plate

    def setLicensePlate(self, plateNumber):
        self._plateNumber = plateNumber

    def getLicensePlate(self):
        return self._plateNumber

    # An overridden method.
    def getDescription(self):
        return "A car is a vehicle with %d tires" % self._numberOfTires
