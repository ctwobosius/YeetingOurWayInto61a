""" Recursively doing Recursion...hm...Version: homework
By Calvin Wong
"""

import random   # this basically imports code that someone else
                # (in this case the Python creators) wrote, so you can use it in yours

""" Recursion is simply calling the function in your definition!
You need at least 2 things:
Base case: This stops the function from continuing to call itself forever.
Recursive case(s): This does the stuff in between the base case and your first case.
"""


def countdown(n):
    """ Recursively count down from n all the way to 0.
    If n is negative, you can print whatever, or you could print something funny lol
    >>> countdown(3)
    3
    2
    1
    0
        # Everything below is just me monkeying around with print statements
    Blastoff!
    ...
    I said blastoff, ya monkeys, why aren't we moving?! Push the button!!!
    """
    # base case
    if ____:
        print(____) # or print 0

    # recursive case
    else:
        ____
        return countdown(____)

print("Counting down:")
countdown(3)

def random_sum(n):
    """ Returns n random one digit, nonzero numbers added together. Kind of like what you do on math tests.
    >>> random_sum(3)
    15 # pretend the random numbers chosen were 5 + 3 + 7
    """
    if ____:
        return ____
    else:
        # random is the library we imported at the top, which allows us to access randint
        return random.randint(____, ____) ____
        # randint documentation: https://www.pythoncentral.io/how-to-generate-a-random-number-in-python/

print()
print("Random sum: ")
print(random_sum(3)) # Think about what the minimum and maximum this could print out. When you run it, is your number in this range?
