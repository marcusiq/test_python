from Stack import *
import copy

# Custom method to check for equality of stacks.
def equals_with_details(stack1, stack2):
    while True:
        try:
            ch1 = stack1.peek()
            ch2 = stack2.peek()
            if stack1.pop() != stack2.pop():
                print "%s!= %s" % (ch1, ch2)
                return False
            else:
                print "%s = %s" % (ch1, ch2)

        except IndexError:
            return True


def equals(stack1, stack2):
    list1 = stack1.items
    list2 = stack2.items
    return list1==list2


# 1. Enter the test phrase to check if it is a palindrome.
phrase = "Madam, I'm Adam"
phrase = "Snow Dragons!"  # Overwrites the previous value. Just use commenting to select one or other.

# Added code here.
done = False
while not done:
    print "\nEnter a phrase to test if it is a palindrome. Type Q to quit."
    phrase = raw_input()
    if phrase=="Q" or phrase=="q":
        print "Ok, bye!"
        break
    phrase = phrase.upper()
    print "The test phrase is: ", phrase

    # 2. Build a stack of letters using just the alphabetical characters, all in upper case.
    letter_stack = Stack() # Create an empty stack.
    for character in phrase:
        if character.isalpha(): # Ignore any characters that are not letters like spaces, and punctuation marks.
            letter_stack.push(character)
    print "The first stack is:\t\t", str(letter_stack)

    # 3. Create a second stack in the reverse order. Must use copy.deepcopy() and not just copy.copy()
    duplicate = copy.deepcopy(letter_stack)  # A temporary copy, which will be exhausted by popping to create the reverse stack.
    reverse_stack = Stack() # Create a new empty stack.
    while not duplicate.isEmpty():
        next_letter = duplicate.pop()
        reverse_stack.push(next_letter)
    print "The reversed stack is:\t", str(reverse_stack)


    # Now we need to check if the original stack of letters and the reverse stack are equal.
    # If they are, we have a palindrome.
    print "\nComparing letters forwards versus backwards."
    equals_with_details(letter_stack, reverse_stack)
    is_palindrome = equals(letter_stack, reverse_stack)
    if is_palindrome:
        print "Yes, %s is a palindrome." % phrase
    else:
        print "No, %s is NOT a palindrome." % phrase



