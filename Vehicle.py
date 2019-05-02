# A simple class for vehicles.
# Vehicles have one attribute, the number of tires.
# This is the parent class of the Car subclass, defined in its own file.

class Vehicle(object):
    def __init__(self, numberOfTires):
        self._numberOfTires = numberOfTires

    def getNumberOfTires(self):
        return self._numberOfTires

    def setNumberOfTires(self, numberOfTires):
        self._numberOfTires = numberOfTires

    def getDescription(self):
        return "A vehicle with %d tires" % self._numberOfTires

