print "Part 3. Conditionals. Using if statements."


print "\n1. Use isalpha() to test which characters in this string are alphabetical."
print 'aliens = "Area-51"'
aliens = "Area-51"

# 1. Add a for loop and if/else statements here to test which letters are alphabetical.
# Replace pass with your code.

for ch in aliens:
    if ch.isalpha():
        print "Yes, '%s' is an alphabetical character." % ch
    else:
        print "No, '%s' is not an alphabetical character."  % ch


print "\n\n2. Here is a dictionary showing the ages of some students."
age = {"Alan": 19, "Brenda": 20, "Charlene": 21, "David": 19, "Ed": 24}
print "Dictionary with Name and Age:", age
print "Print out which students can attend an open-bar dance. They must be 21."

# 2. Add your code for exercise 2 here.
print "List of those students 21 and over."

for name in age:
    if age[name] >= 21:
        print "\t%s is %2d and can attend the dance." % (name, age[name])


print "\n\n3. Here is a dictionary showing the grades for some students."
grade = {"Alan": 91.5, "Brenda": 88, "Charlene" : 77, "David": 100, "Ed": 66, "Frank": 50}
print "Dictionary of grades:", grade
print "Print out their letter grades A, B, C, D or F."
# 3. Add your code for exercise 3 here.
# Use the for loop header provided below, and replace the pass command with if/elif/else blocks.

for name in grade:
    if grade[name] >= 90:
        print "%-10s has earned an A." % name
    elif grade[name] >= 80:
        print "%-10s has earned a  B." % name
    elif grade[name] >= 70:
        print "%-10s has earned a  C." % name
    elif grade[name] >= 60:
        print "%-10s has earned a  D." % name
    else:
        print "%-10s has earned an F." % name


# Here is a method, to assign letter grades based on the numerical break points.
# Why keep typing this over and over?
def letter_grade(the_grade):
    if the_grade >= 90:
        return "A"
    elif the_grade >= 80:
        return "B"
    elif the_grade >= 70:
        return "C"
    elif the_grade >= 60:
        return "D"
    else:
        return "F"

print "\n\n4. Print the grades again, but show the student names in alphabetical order."
names = grade.keys()
 # 4a. Add code to sort the list of names from A - Z here.
names.sort()

# 4b. Add more code for exercise 4 here.
# Use the for loop header provided below, and replace the pass command with if/elif/else blocks.
for name in names:
    if grade[name] >= 90:
        print "%-10s has earned an A." % name
    elif grade[name] >= 80:
        print "%-10s has earned a  B." % name
    elif grade[name] >= 70:
        print "%-10s has earned a  C." % name
    elif grade[name] >= 60:
        print "%-10s has earned a  D." % name
    else:
        print "%-10s has earned an F." % name


# Alternatively, we can use the method letter_grade() defined directly above this problem.
print "\nHere are the grades again, but using our user-defined method."
for name in names:
    letter = letter_grade(grade[name])
    print "%-10s has earned an %s." % (name, letter)




print "\n\n5. Print out the students by rank, that is from highest to lowest numerical grade."
grade = {"Alan": 91.5, "Brenda": 88, "Charlene" : 77, "David": 100, "Ed": 66, "Frank": 50}

# 5a. Create a list of the values here.
numerical_grades = grade.values()
print "The students' unsorted numerical grades are:\t", numerical_grades

# 5b. Sort that list of values here.
numerical_grades.sort(reverse=True)
print "The students' sorted numerical grades are:\t\t", numerical_grades

rank=0
print "%-8s%-10s%-2s" % ("Rank", "Name", "Grade")

# 5c. Complete the nested for loop using an if statement to find the student
# with each number_grade, (assumed to be unique), increase the rank by 1, and print out
# that students info to match the sample output in the PDF instruction file.

for number_grade in numerical_grades:
    for name in grade:
        if grade[name]==number_grade:
            rank +=1
            print "%-8s%-10s%-2s" % (rank, name, grade[name])

print "\nThe above method breaks down, if two grades are the same."
print "Change Ed's grade from 66 to 50, the same as Frank's."
grade["Ed"] = 50
numerical_grades = grade.values()
numerical_grades.sort(reverse=True)

print "Then, each student with the same grade appears multiple times."
rank=0
for number_grade in numerical_grades:
    for name in grade:
        if grade[name]==number_grade:
            rank +=1
            print "%-8s%-10s%-2s" % (rank, name, grade[name])



# * * * * LIVE QUESTION * * * *

aliens = "Area-51"; print '\nIs "%s" in title case?  %s'  % (aliens, aliens.istitle() ) # It's true!
aliens = "Area-51"; print '\nAre all the characters in "%s" alphanumeric?  %s'  % (aliens, aliens.isalnum() )   # It's false because of the dash.

