__author__ = 'robincarr'

import math

print 'A triangle has sides a, b and c and opposite angles A, B and C.'
print 'For our SAS triangle calculation, angle A is known and the adjacent sides b and c are also known.'
print 'GOAL: Solve the triangle, i.e., find the third side a, and the angles B and C in degrees.\n'


# Collect the three known data points from the user.

print 'Enter the included angle A in degrees:'
A_in_degrees = float( input() )
A_in_radians = math.radians(A_in_degrees)


print 'Enter side b:'
b = input() * 1.0

print 'Enter side c:'
c = float( input() )  # Another way to guarantee the side is treated as a float.



# First, find the missing side a, using the law of cosines.
# See this link for a refresher on SAS triangles.
# https://www.mathsisfun.com/algebra/trig-solving-sas-triangles.html

a_squared = b**2 + pow(c,2) - 2*b*c * math.cos(A_in_radians)
a = math.sqrt(a_squared)
print "Using the Law of Cosines, the side 'a' opposite angle 'A' is: %0.3f units." % a

"""
Alert for Obtuse Triangles: An obtuse triangle is one containing an angle > 90 degrees.
This creates a problem, because the arc sine of an angle greater than 90 degrees will return an angle less than 90 degrees.
Indeed sin(90 + theta) = sin(90-theta), and you'll get the angle (90-theta) instead.
Thus, if any angle is over 90 degrees, or the equivalent in radians, it will be given incorrectly using the asin() function.
"""

# Now find the sine of the smaller angle, which is opposite the smaller of the two given sides. Critically important!
# The code below assumes b < c and so B is the smaller angle.
# But that might not be the case. If it is not, we will first swap sides b and c, then swap angles B and C
# using Python "tuple assignment" statements.
swapped_sides = False
if b > c:
    b, c = c, b  # Swap the two sides so b holds the smaller value.
    swapped_sides = True  # A flag to remember we swapped the sides, and will have to swap them back.
    print "\t1. Swapping 'b' and 'c' because b > c."

# Now find the sine of the smaller angle, which will be < 90 degrees, and hence we can safely use asin().
sine_of_B = b * math.sin(A_in_radians)/a
B_in_radians = math.asin(sine_of_B)
B_in_degrees = math.degrees(B_in_radians)

# For the third angle, use the fact that angles in a triangle add up to 180 degrees.
C_in_degrees = 180 - A_in_degrees - B_in_degrees

# Did we swap the sides? If so, we must now swap them back, and also swap the angles B and C.
if swapped_sides:
    print "\t2. Swapping 'b' and 'c' back again."
    b, c = c, b  # Swap them again!
    B_in_degrees, C_in_degrees = C_in_degrees, B_in_degrees


print 'The angle B is: %0.3f degrees.' % B_in_degrees
print 'The angle C is: %0.3f degrees.' % C_in_degrees
