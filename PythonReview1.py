# Python Review Part 1 - Strings and string-slicing.
# See the file HW1_QuickPythonReview.pdf for additional commentary, sample output and hints.


print "\n\nLet's check our version of Python and your Platform"
import sys;
print('Python %s on %s' % (sys.version, sys.platform))

print "\nWhat is the prefix used to find the python library?"
print sys.prefix

print("\nLet's get more info on our version.")
print sys.subversion

print("\nIs there a subversion?")
print sys.subversion

print("\nWhat are the built-in modules?")
print sys.builtin_module_names

print("\nWhat is the executable?")
print sys.executable

print "\nWhat are the loaded modules. This is a dynamic object!"
print sys.modules


# ~ ~ ~  ~ ~ ~  ~ ~ ~  ~ ~ ~  ~ ~ ~  ~ ~ ~  ~ ~ ~  ~ ~ ~  ~ ~ ~  ~ ~ ~  ~ ~ ~  ~ ~ ~



print "Python Review Part 1 - Strings and string-slicing."
print "See the file HW1_QuickPythonReview.pdf for additional commentary, sample output and hints."


import string
print "\nUncomment the next line to see help showing the functions available from the string module."
# help(string)


print "EXERCISES Part 1 of Review - Strings and String Slicing"
s = 'catfish hatchery'
# Tip: Use repr() when you print, so we can see the enclosing quotes.
# # This will help verify there are no extraneous spaces.


print "\n1. Using string-slicing, print out just the  word 'cat' from the larger phrase '%s'" %s
print "Answer:\t\t",

# 1. Add code to extract 'cat' and print it here. Use repr() so we can see your answer in quotes.
answer = s[:3]
print "The first word in '%s' is:" % s, repr(answer)



print "\n2. Using string-slicing, print out just the  word 'fish'."
print "Answer:\t\t",
answer = s[3:7]
print "The second word in '%s' is:" % s, repr(answer)


print "\n3. Using string-slicing in the form s[m:], print out just the  word 'hatchery'."
m = s.find('hatch')
print 'The desired index is:', m
print "Answer:\t\t",
answer = s[m:]
print "The last word in '%s' is:" % s, repr(answer)


print "\n4. Count the number of h's in s, defined above. Use the count() method. "
print "Answer:\t\t",
print "The number of h's in %s is:" % s,  s.count('h')


print "\n5. Count the number of vowels in 'catfish hatchery', using a for loop. Do not use the count() method."
print "Answer:\t\t",
s = 'catfish hatchery'
counter = 0
target = 'aeiouAEIOU'
for ch in s:
    if ch in target:
        counter += 1
print 'The number of vowels in %s is: ' % s, counter


print "\n6. Use the upper() method to convert these initials to all upper case."
# Print out "I live in the USA." using the result and a %s format flag.
country = "usa"
country = country.upper()
print "I live in the %s." % country

print '\n7. Convert the country below to the more proper form: "United States of America" using title().'
country = "united states of america"

# Add two lines here, first using title() and then using replace() to make 'O' small again.
country = country.title() # Capitalizes each new word.
country = country.replace('O', 'o')  # But we  don't want the 'o' in "of" capitalized.
print "I live in the %s." % country


print "\n8. Find out which of these test words startswith() 'dog', endswith() 'fish' or contains() 'cat'."
word1 = "dogcatcher"
word2 = "dogfish"
word3 = "dogberry"
words = [word1, word2, word3]
print "Test words:", words
# Add your code for exercise 8 here.
# A. Find the words that start with 'dog' here. Use a for loop.
print "\nThese words start with 'dog':\t\t",
for word in words:
    if word.startswith('dog'):
        print word,

# B. Find the words that end with 'fish' here. Use a for loop.

print "\nThese words end with with 'fish':\t",
for word in words:
    if word.endswith('fish'):
        print word,

# C. Find the words that contain 'cat' here. Use the "in" operator.
print "\nThese words contain 'cat':\t\t\t",
for word in words:
    if 'cat' in word:
        print word,

# LIVE QUESTION for peer review.
# 1A. Live! Print out the sum of the number of c's,  a's and t's in s = 'catfish hatchery'
# Use count() three times.

print "\n\nThe total number of c's, a's and t's in 'catfish hatchery' is: ", s.count('c') + s.count('a')  + s.count('t')