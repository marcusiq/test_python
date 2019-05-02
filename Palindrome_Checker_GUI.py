from Tkinter import *
from Stack import Stack
import copy


# Flashes a widget, typically as a warning or to get attention.
def flash(my_widget, n): # Typically n = 2k will be even to give k complete cycles.
    if n == 0:
        root.after(2000, clear_result)  # Wait 2 seconds, then clear the error message.
        my_widget.config(bg="white")
    else:
        current_color = my_widget.cget("background")
        next_color = "red" if current_color == "yellow" else "yellow"
        my_widget.config(background=next_color)
        root.after(250, flash, my_widget , n-1)


# Method to check if two stacks are the same.
# This version does not consume  the stacks, but instead makes duplicates first.
def stack_equals(stack1, stack2):
    stack1_copy = copy.deepcopy(stack1)
    stack2_copy = copy.deepcopy(stack2)

    while True:
        try:
            ch1 = stack1_copy.peek()
            ch2 = stack2_copy.peek()
            if stack1_copy.pop() != stack2_copy.pop():
                print "%s!= %s" % (ch1, ch2)
                return False
            else:
                print "%s = %s" % (ch1, ch2)

        except IndexError:
            return True

def clear_result():
    test_results_widget.delete(0,END)
    test_results_widget.config(state=DISABLED)

# Method to add a valid palindrome after the "Test Results" button is pressed.
# It is only added if it is new, up to case.
def add_palindrome(valid_palindrome):
    # 1. First make a deepcopy of the stack of example palindromes.
    duplicate1 = copy.deepcopy(stack_of_example_palindromes)

    # 2. Push the entire stack to a new stack, converting to upper case as you do.
    duplicate2 = Stack() # An Empty stack.
    while not duplicate1.isEmpty():
        next_palindrome = duplicate1.pop()
        duplicate2.push( next_palindrome.upper() )  # Convert to all upper to make the method case insensitive.

    # 3. Check if the valid_palindrome (in upper case) is in the stack's list of items.
    if valid_palindrome.upper() in duplicate2.items:
        print "Example stack aleady contains this palindrome."
    else:
        print "New palindrome added to the example stack of palindromes!"
        print "Added the palindrome: %r" % valid_palindrome

        stack_of_example_palindromes.push(valid_palindrome)


def check_palindrome():
    # 1. Get the user's test phrase.
    phrase = test_phrase_widget.get().upper()

    # 2. Build a stack of letters using just the alphabetical characters, all in upper case.
    letter_stack = Stack() # Create an empty stack.
    for character in phrase:
        if character.isalpha():
            letter_stack.push(character)
    print 'Forward:', letter_stack

    # 3. Create a second stack in the reverse order. Must use copy.deepcopy() and not just copy.copy()
    duplicate = copy.deepcopy(letter_stack)  # A temp copy, which will be exhausted by popping to create the reverse stack.
    reverse_stack = Stack() # Create a new empty stack.
    while not duplicate.isEmpty():
        next_letter = duplicate.pop()
        reverse_stack.push(next_letter)
    print 'Reverse:', reverse_stack

    # 4. Check if the forward and reverse stacks of letters are equal.
    is_palindrome = stack_equals(letter_stack, reverse_stack)
    test_results_widget.config(state=NORMAL)
    test_results_widget.delete(0,END)
    if is_palindrome:
        test_results_widget.insert(0,"Yes! It's a palindrome!")
        # A line was  added here to add it to the stack of examples, if it is a new palindrome.
        add_palindrome( test_phrase_widget.get() )
    else:
        test_results_widget.insert(0,"Not a palindrome!")
    flash(test_results_widget, 8)




def print_to_tk_window():
    # Pop up a new window
    new_window = Tk()
    new_window.title("List of palindromes")
    Label(new_window, text="The stack of examples includes these fun palindromes.".upper()).grid()
    #  Make a copy of the stack first. Must use copy.deepcopy() and not just copy.copy()

    duplicate = copy.deepcopy(stack_of_example_palindromes)  # A temp copy, which will be exhausted by popping during printing.
    while not duplicate.isEmpty():
        next_palindrome = duplicate.pop()
        Label(new_window, text=next_palindrome).grid()

# Complete this stub to print all the example palindromes to the console window,
# without depleting the stack.
def print_to_console():
    # 3. Make a copy of the stack first. Must use copy.deepcopy() and not just copy.copy()
    print "\nThe stack of examples includes these fun palindromes."
    duplicate = copy.deepcopy(stack_of_example_palindromes)  # A temp copy, which will be exhausted by popping during printing.
    while not duplicate.isEmpty():
        next_palindrome = duplicate.pop()
        print next_palindrome
    print_to_tk_window()  # Also print them in a new Tk window



def show_random_palindrome():
    try:
        example = stack_of_example_palindromes.pop()
    except Exception as e:
        print e
        example = "Madam, I'm Adam!"
    test_phrase_widget.delete(0,END)
    test_phrase_widget.insert(0,example)


root = Tk()
root.title("Palindrome Checker")


stack_of_example_palindromes  = Stack()
stack_of_example_palindromes.push("Stack Cats")
stack_of_example_palindromes.push("TacoCat")
# Push at least ten more example palindromes onto the stack of examples here.
# Here is one good source. http://www.palindromelist.net

stack_of_example_palindromes.push("A dog! A panic in a pagoda!")
stack_of_example_palindromes.push("Borrow or rob?")
stack_of_example_palindromes.push("Cigar? Toss it in a can. It is so tragic.")
stack_of_example_palindromes.push("Dammit, I'm mad!")
stack_of_example_palindromes.push("Devil never even lived.")

stack_of_example_palindromes.push("Did Hannah see bees? Hannah did.")
stack_of_example_palindromes.push("Do geese see God?")
stack_of_example_palindromes.push("Doc, note, I Dissent. A fast never prevents a fatness. I diet on cod.")
stack_of_example_palindromes.push("Dr. Awkward")
stack_of_example_palindromes.push("Drab as a fool, aloof as a bard.")

stack_of_example_palindromes.push("Elba Kramer saw I was remarkable.")
stack_of_example_palindromes.push("Eva, can I stab bats in a cave?")
stack_of_example_palindromes.push("Evil did I dwell, lewd I did live.")
stack_of_example_palindromes.push("Evil rats on no star live.")
stack_of_example_palindromes.push("Gnu dung.")

stack_of_example_palindromes.push("God! A red nugget! A fat egg under a dog!")
stack_of_example_palindromes.push("He did, eh?")
stack_of_example_palindromes.push("Hey, Roy! Am I mayor? Yeh!")
stack_of_example_palindromes.push("I did, did I?")
stack_of_example_palindromes.push("I'm a lasagna hog, go hang a salami.")

stack_of_example_palindromes.push("I'm a fool; aloof am I.")
stack_of_example_palindromes.push("In word salad, alas, drown I.")
stack_of_example_palindromes.push("Lager, sir, is regal.")
stack_of_example_palindromes.push("Lepers repel.")
stack_of_example_palindromes.push("Live not on evil.")

stack_of_example_palindromes.push("Ma is as selfless as I am.")
stack_of_example_palindromes.push("Madame, not one man is selfless; I name not one, madam.")
stack_of_example_palindromes.push("Mega gem!")
stack_of_example_palindromes.push("Mr. Owl ate my metal worm.")
stack_of_example_palindromes.push("Murder for a jar of red rum.")

stack_of_example_palindromes.push('Nella risks all: "I will ask Sir Allen!"')
stack_of_example_palindromes.push("No lemons, no melon.")
stack_of_example_palindromes.push("No, it is opposition.")
stack_of_example_palindromes.push("No, sir, away! A papaya war is on!")
stack_of_example_palindromes.push("On a clover, if alive, erupts a vast, pure evil; a fire volcano.")

stack_of_example_palindromes.push("Oprah deified Harpo.")
stack_of_example_palindromes.push("Poor Dan is in a droop.")
stack_of_example_palindromes.push("Pull up, Eva, we're here! Wave! Pull up!")
stack_of_example_palindromes.push("Put Eliot's toilet up.")
stack_of_example_palindromes.push("Red rum, sir, is murder.")

stack_of_example_palindromes.push("Rise to vote sir.")
stack_of_example_palindromes.push('"Rum ... rum ..." I murmur.')
stack_of_example_palindromes.push("Senile felines.")
stack_of_example_palindromes.push("Sir, I'm Iris.")
stack_of_example_palindromes.push("Step on no pets.")

stack_of_example_palindromes.push("Stressed? No tips? Spit on desserts.")
stack_of_example_palindromes.push("Stung nuts.")
stack_of_example_palindromes.push("Todd erases a red dot.")
stack_of_example_palindromes.push("Tuna roll or a nut?")
stack_of_example_palindromes.push("Was it a bar or a bat I saw?")




palindrome_image1 = PhotoImage(file="images_for_palindromes/TacoCat.gif")
palindrome_image2 = PhotoImage(file="images_for_palindromes/StackCats.gif")

outside_frame = Frame(root, bg="blue", padx=4, pady = 4)
outside_frame.grid(row=0, column=0, columnspan=4)
# The outside frame merely acts as a blue frame about the GUI.

top_frame = Frame(outside_frame, bg="lightyellow", padx=4, pady = 4)
# top_frame.grid(row=0, column=0, columnspan=4, sticky=NSEW)
top_frame.pack()

# Next, we add frame2 for the control buttons.
bottom_frame = Frame(outside_frame, padx=4, pady = 4, bg="yellow")
# bottom_frame.grid(row=1, column=0, columnspan=4, sticky=NSEW)
bottom_frame.pack(fill=X, anchor=CENTER)

image_label1 = Label(top_frame, bg="black", image = palindrome_image1)
image_label1.grid(row=0, column=0, columnspan=2, sticky=NSEW)
image_label2 = Label(top_frame, bg="black", image = palindrome_image2)
image_label2.grid(row=0, column=2, columnspan=2, sticky=NSEW)

Label(top_frame, text="Test Phrase", bg="lightyellow", fg ="blue").grid(row=1, column=0)
test_phrase_widget = Entry(top_frame, justify=CENTER, width=40)
test_phrase_widget.grid(row=1, column=1, columnspan=3)

Label(top_frame, text="Test Results", bg="lightyellow", fg ="blue").grid(row=2, column=0)
test_results_widget = Entry(top_frame, justify=CENTER, width=40, state=DISABLED)
test_results_widget.grid(row=2, column=1, columnspan=3)

# Add some control buttons
show_button = Button(top_frame, text="Show Random", command = show_random_palindrome)
show_button.grid(row=3, column=0, columnspan=2, sticky=SW)

check_button = Button(top_frame, text="Check", command = check_palindrome)
check_button.grid(row=3, column=2, sticky=W)

# The Print button was added here.
print_button = Button(top_frame, text="Print to Console", command = print_to_console)
print_button.grid(row=3, column=3, sticky=E)



root.mainloop()