""" Abstraction (Abstract Art? Maybe...???) """

from no_looky import *

"""
Abstraction is basically hiding details! This helps you write cleaner code
and avoid copy pasting the same code over and over.

no_looky contains:

rational(num, den):
    # Returns a "rational" object, we pretend it's a black box
    >>> r = rational(5, 2) # used below

numer(r):
    # Returns the numerator of R, a rational object
    >>> r = rational(5, 2)
    >>> numer(r)
    5

denom(r):
    # Returns the denominator of R, a rational object
    >>> r = rational(5, 2)
    >>> denom(r)
    2

rational_to_float(r):
    # Returns the float of R, a rational object
    >>> r = rational(5, 2)
    >>> rational_to_float(r)
    2.5

"""

x = rational(3, 2)
rational_to_float(x)
numer(x)


x = (3, 2)
x[0] / x[1]
x[0]

x = rational(3, 2)
rational_to_float(x)
numer(x)

x = {"n": 3, "d": 2}
x[0] / x[1]
x[0]

"""
no_looky also has:

extendedEuclid(x, y):
    Returns d, a, b such that d is the gcd of X and Y and d = aX + bY.
    X and Y must be integers.

    >>> extendedEuclid(3, 4)
    (1, -1, 1)
    # 1 = -1*3 + 1*4 and 1 is the greatest common denominator of 3 and 4

    >>> extendedEuclid(8, 4)
    (4, 0, 1)
    # 4 = 0*8 + 1*4 and 4 is the greatest common denominator of 8 and 4
"""

def gcd(x, y):
    """Returns the greatest common denominator of X and Y, given both are integers."""
    return ____



# imagine copy pasting this, then having to change this for each paste if you found a problem:
    swapped = False
    if x < y:
        swapped = True
        x, y = switched(x, y)
    eqs = {x: (1, 0),
           y: (0, 1)}
    while (x != 0):
        if (x < y) and (x != 1):
            x, y = switched(x, y)
        if (x == 1 or y == 0):
            if swapped:
                return (x, eqs[x][1], eqs[x][0])
            return (x, eqs[x][0], eqs[x][1])
        scaleBy = (x // y)
        eqs[x % y] = (eqs[x][0] - scaleBy * eqs[y][0], eqs[x][1] - scaleBy * eqs[y][1])
        x = x % y
    if swapped:
        return (y, eqs[y][1], eqs[y][0])
    return (y, eqs[y][0], eqs[y][1])
