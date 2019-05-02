__author__ = 'robincarr'

import time
# Last item in the list named "items" is the TOP of the stack.
# First item (index 0) in the list "items" is the bottom of the stack.
# Top of the stack is the end of its list of items.

# LIST IMPLEMENTATION OF A STACK IN PYTHON

class Stack:
    def __init__(self):
        self.items = []  # Creates an empty list.

    def isEmpty(self):
        return self.items == []   # Returns True if the stack is empty, otherwise False.

    def push(self, item):
        self.items.append(item)  # Append the new item to the top of the stack's list.

    def pop(self):  # Implements the pop() method for stacks, using the pop() method for its list.
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

# These next methods are not core stack methods, but are still useful.
    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items) + "<--"  # The arrow here represents the pointer to the top of the stack.



if __name__ == "__main__":
    # Place all demo code here. Use Edit >> Indent Selection to help move all lines over 4 spaces
    # Demo code
    print "STACK DEMO 1"

    print "\n1. First we construct an empty stack."
    print "The pointer is to the top of the stack."

    s = Stack()  # Creates a new empty stack.
    print 'The empty stack is represented as:', str(s)

    print "\n2. Push 1, then 3, then 5 onto the stack."
    s.push(1)
    s.push(3)
    s.push(5)
    print 'Now the stack is:', str(s)

    print "\n3. Pop the stack twice."
    s.pop()
    s.pop()
    print 'Now the stack is:', str(s)

    print "\n~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * "

    print "\nSTACK DEMO 2: Homework"
    # Add your code here.

    # i. Create an empty stack named homework. Print it out.

    homework = Stack()
    print "The homework will appear in this stack.", homework

    print "Enter the number of exercises N for this homework."
    N = input("Enter N: ")

    # ii. Push these exercises onto the stack in reverse order. Print it.
    # "Exercise 4", "Exercise 3", "Exercise 2", "Exercise 1"

    # Old code - not as good.
    # homework.push("Exercise 4")
    # homework.push("Exercise 3")
    # homework.push("Exercise 2")
    # homework.push("Exercise 1")

    # Here is an alternative using a for loop instead.
    for k in range(N, 0, -1):
        # homework.push("Exercise" + str(k) )
        homework.push("Exercise %s" % k)  # or use this instead.



    print "The assignment is now posted. There are %d exercises to complete." % N
    print homework


    """
    iii. Using a while loop and time.sleep(1), pop the stack until all exercises are
    completed. The while loop should test if the stack isEmpty. Print out each exercise as it is completed.

    """

    while not homework.isEmpty():
        print "Working on:", homework.pop()
        time.sleep(1)
    print "Finished! Now time to relax!"

    pass # Delete this line.
