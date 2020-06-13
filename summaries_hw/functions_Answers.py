""" Fun-ctions! Pun-ctions? Punctuation??? Syntax ;) Answers"""

print(f(3)) # What would this do? ____
# Would print out:
#   5
# in the terminal

""" Multi-argument functions """
def fatReptile(fat, reptile):
    if fat and reptile:
        return "weird lizard"

print(fatReptile(True, True)) # What is this?

# Would print out:
#   weird lizard
# in the terminal


x = print()
x # What do you think x is?

# x is None


# Tricky! What would
print(print("Haha"))
# do?

# Hint: remember PEMDAS! Inner parenthesis are evaluated first, so
((3 + 5) * 2)
# 3 + 5 is done first!

# It would print out this in the terminal:
# Haha
# None

x = 3 # global variable

def past(a): # local
    print(a) # Will this error?
    # No, it's defined locally as an argument, so when we look it up, we find it
    y = 5 # local
    x = 2 # local
    return # this is the same as return None

past("a") # run the function

print(a) # Will this error? ____
#   Errors, a is again defined locally, function arguments are local

print(y) # How about this? ____
#   Errors, y is again defined locally within the function, it's indented

print(x) # The fun part: what about this?

#   3, because x is defined to be 2 ONLY LOCALLY. If you wanted to change
#   the global x, you need to do this:
def past(a):
    global x
    x = 2
#   Then it would print 2, because you're saying that the function should modify
#   the global variable x, rather than create a local variable x.

past("a") # btw this is a joke, "past(a) -> pasta" if you didn't catch that
print(x) # prints 2
