""" Environment Diagram Code
By Calvin Wong
"""

"""
Primitives:
    These will evaluate to themselves.
    numbers (int, float)
    strings
    booleans (True, False)

Pointers:
    With these, you draw an arrow to it.
    Functions (eg: func name [parent = global])
    Lists (introduced later)

Everything else needs to be evaluated ("simplified") to a primitive.

Evaluation rules:
    Primitives      ->      themselves
    Function call   ->      return value (eg: print("Lol") -> None)

    Side note: Scope

        Arguments and variables declared in functions will only exist in the function.
        These args and vars are in the "local scope" of the function.

        Those declared in the main program are called "global" variables.

        If there are conflicting variables
        (ie: there's a local and global variable with the same name)
        then the local variable is used first.

Open new frames for each function call
    ie: funcName()     <-     parenthesis means it's called!
    Don't forget all functions have a return value!
    Remember local variables are looked for first, then you go to the parent frames
        if you can't find the variable, if it reaches the global frame and can't find
        the variable, it errors
"""


nickname = "l33t h@ck3r"
nickname += " fails: "

fails = 0

for i in range(3):
    fails += 1

def howManyFails(fails):
    what = "does wat?"
    return print(fails)

fails = howManyFails(100)

impossible = nickname + str(fails)
# print(impossible) # lol super funny message right
