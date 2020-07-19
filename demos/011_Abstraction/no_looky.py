def switched(x, y):
    """Returns Y, X."""
    return (y, x)

def extendedEuclid(x, y):
    """Returns d, a, b such that d is the gcd of X and Y and d = aX + bY. """
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

# def rational(num, den):
#     # Returns the representation of a rational number
#     return num, den

def rational(num, den):
    return {"n": num, "d": den}

def numer(r):
    # Returns the numerator of R, a rational number
    # return r[0]
    return r["n"]

def denom(r): # Returns the denominator of R, a rational number
    # return r[1]
    return r["d"]

def rational_to_float(r): # Returns the float of R, a rational number
    return numer(r) / denom(r)
