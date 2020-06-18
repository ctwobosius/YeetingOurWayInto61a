def countdown(n):
    """ Recursively count down from n all the way to 0. If n is negative, you can print whatever.
    >>> countdown(3)
    3
    2
    1
    0
    """
    # base case
    if n <= 0:
        print(n) # or print 0

    # recursive case
    else:
        print(n)
        return countdown(n - 1)
