print "Python review Part 4 - Calculations and Math Functions"


# import the math module as follows.
import math

# Get help on the math module by uncommenting this statement.
# help(math)

message1 = """\n1. Find the absolute value of  the floating point number -2.34 using a method from the math module.
You must not use the __builtin__ method abs(), but a similar math module method starting with f.
"""
print message1
x = -2.34
# Add your code for exercise 1 here. Be sure to print out the results.
print "The  absolute value of %f is: %f" % (x, math.fabs(x))


message2 = """\n2. A right triangle has legs a = 5.0, b = 12.0
Find the hypotenuse c using the sqrt() method from the math module.
"""
print message2
a = 5.0
b = 12.0
# Add your code for exercise 2 here. Be sure to print out the results.

c = math.sqrt(a**2 + b**2)
print "The hypotenuse C of the right triangle is:" , c


message3 = """\n\n3. Find the angle B opposite the longer side b using the relation:
sin(B) = b/c
"""
print message3

# Add your code for exercise 3 here. Use the asin() function, which by definition returns radians.

sinB = b/c
B = math.asin( sinB )
print "The angle B is %.3f radians." % B


message4 = """\n\n4. Express the angle B in degrees using math.degrees()
"""
print message4

# Add your code for exercise 4 here.
print "The angle B is %.3f degrees." % math.degrees(B)


message5 = """\n\n5. Express 1000 (base 10) in base 2 using the built-in bin() command. (bin, short for binary).
"""
print message5
# Add your code for exercise 5 here.
print "The binary representation for 1000 (base 10) is: ", bin(1000)



message6 = """\n\n6a. Convert the binary number n2 = '10100100010000100000' back to base 10 using the built-in int() command
with an optional second argument to specify the base.
"""
print message6
n2 = "10100100010000100000"
# Add your code for exercise 6a here.

n10 = int(n2, 2)
print "In base 10, the number is:", n10

print "b. Check you work by converting back to base 2 using bin()."
# Add your code for exercise 6b here.

print "Check: Converting the answer back to base 2 gives: ", bin(n10)


# * * * EXERCISE 7 * * *

message7a = """\n\n7a. Using math.log() with two arguments, find the log of 10,000,000 in base 1000. (one thousand)
"""
print message7a
# Add your code for exercise 7a here. Be sure to print out the answer using a complete sentence.
math.log(10000000, 1000)
print "\nThe log of ten million in base 1000 is:", math.log(10*1000*1000, 1000)


message7b = """\n\n7b. Using math.pow() find  1000 to the seven thirds power. Beware of the integer division!
"""
print message7b
# Add your code for exercise 7b here. Be sure to print out the answer using a complete sentence.

print "Check: One thousand to the seven thirds power is:", math.pow(1000, 7.0/3)  # Must use a decimal here!



print "\n\nLIVE CHALLENGE - Palindromes in Base 2"
live_message = """4LIVE! These numbers in base 10 are palindromic numbers because they are the same forwards and backwards.
22, 121, 12321, 14441 and many, many more.
Similarly, these number in base2 are palindromes: 11, 101, 1111, 110011
Using bin() and a for loop, find the first number greater than 1000 (base 10), which is a palindrome in base2.
Print it out and  use break, so it only shows the first palindrome matching the condition.
"""

print live_message

for n in range(1000, 2000):
    binary_string = bin(n)[2:]
    if binary_string == binary_string[::-1]:
        print "The first number greater than one thousand, which is a palindrome in base 2 is:"
        print "Base 10:%5d --> Base 2: %s" %(n, binary_string)
        break


print "\nAdded challenge.\nFind the number Nb of palindromes (base 2) in the range [1, 1024]. Note 1024 = 2**10"

Nb = 0
for n in range(1, 2**10+1):
    binary_string = bin(n)[2:] # Strip off the binary prefix.
    if binary_string == binary_string[::-1]:
        Nb +=1 # We found another palindrome (in base 2)
        print "Base 10:%5d --> Base2: %s" %(n, binary_string)

print "The number Nb of palindromes (base 2) in the range [1, 1024] is:", Nb