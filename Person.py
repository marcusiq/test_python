class Person:
    """
    This is the docstring for the Person class!!

    The Person class (loosely) represents a Person.
    """

    def __init__(self, age, weight):
        self.age = age
        self.weight = weight

    def gain_weight(self, amount):
        """Add 'amount' to the weight of a Person object."""
        self.weight += amount

    def lose_weight(self, amount):
        """Subtract 'amount' from the weight of a Person object."""
        self.weight -+ amount

    def have_birthday(self):
        """Increase the age of a Person object by one year."""
        self.age +=1

joe = Person(12, 88)
bob = Person(30, 155)

print "Joe's age yesterday was %d years." % joe.age
joe.have_birthday()
print "It's Joe's birthday today and he is now %d years old." % joe.age

print "\nBob's weight is %d" % bob.weight
print "Bob and Joe coincidentally have the same birthday."
Person.have_birthday(bob)  # Uncommon alternative
print "Bob's age is now %d years old." % bob.age

print "\nThat was a lot of birthday cake! Joe gained 5 pounds. Bob gained 10 pounds!!"
Person.gain_weight(joe, 5) # Uncommon alternative
bob.gain_weight(10)

print "Joe's new weight is %d." % joe.weight
print "Bob's new weight is %d." % bob.weight

