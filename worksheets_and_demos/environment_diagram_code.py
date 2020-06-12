""" Environment Diagram Code """

"""
Primitives:
    These will evaluate to themselves.
    numbers (int, float)
    strings
    booleans (True, False)
    functions (eg: print evaluates to <print function>)

Everything else needs to be evaluated ("simplified") to a primitive.

Evaluation rules:
    Primitives      ->      themselves
    Function call   ->      return value (eg: print("Lol") -> None)
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
# print(impossible)
