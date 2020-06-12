""" Fun-ctions! Pun-ctions? Punctuation??? Syntax ;)"""

print() # is a function!
""" You can tell because there's no space between the variable name
and the parenthesis. """

# So for example, the below are all functions as well!
int()
str()
float()

""" Functions behave like they do in math, for example """
def f(x):
    return x + 2

"""
        This is saying assign the variable f to a function which takes in x
        and returns x + 2.
            Function/variable name:    f
            Argument(s):      x
            Return value:     x + 2
        Indenting indicates the indented code "belongs" to the function that
        it's indented under.
        Don't forget to indent and include the ":"!
"""

print(f(3)) # What would this do? ____

""" Multi-argument functions """
def fatReptile(fat, reptile):
    if fat and reptile:
        return "weird lizard"

print(fatReptile(True, True)) # What is this? ____

""" Boolean facts """
False == 0 == "" == None # False-y values
False == () == [] == {} # False-y values you'll learn later on
# Everything else is True-thy!

""" Boolean short circuiting """
# "and" returns 1st False-y values
# "or" returns 1st True-thy value

""" None/no return """
def garbage(): # No arguments is possible!
    "This does nothing"
    342 + 3
    "asdf"
"""
        If you have no return, then the function returns None, a False-y value
"""

def garbage_equivalent():
    return None

x = print()
x # What do you think x is? ____

""" Print function looks something like this (*NOT the actual code*) """
def print(msg):
    display_in_terminal(msg)
    return None

# Tricky! What would
print(print("Haha"))
# do? ____

# Hint: remember PEMDAS! Inner parenthesis are evaluated first, so
((3 + 5) * 2)
# 3 + 5 is done first!

""" Scope """

"""
    Arguments and variables declared in functions will only exist in the function.
    These args and vars are in the "local scope" of the function.

    Those declared in the main program are called "global" variables.

    If there are conflicting variables
    (ie: there's a local and global variable with the same name)
    then the local variable is used first.
"""
x = 3 # global variable

def past(a): # local
    print(a) # Will this error? ____
    y = 5 # local
    x = 2 # local
    return # this is the same as return None

print(a) # Will this error? ____
print(y) # How about this? ____
print(x) # The fun part: what about this? ____
