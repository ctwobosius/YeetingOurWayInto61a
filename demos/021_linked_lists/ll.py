# https://inst.eecs.berkeley.edu/~cs61a/sp19/disc/disc07.pdf

class Foolz:
    def __init__(self, rawr):
        self.lol = "dunno"
        print(rawr)

    def __repr__(self):
        return "1/0.1"

    def __str__(self):
        return "Division Error?"

x = Foolz("dino")
# dino

print(x)
# Division Error?


# str(3)
# "3" + "55"
# "355"
# 3 + 55 == 58


# print()
# str()
# First look for __str__
# Then you look for __repr__
# Get the return value of __str__ or __repr__

# obj
# gets rid of quotes
# First look at __repr__
# Then look for __str__

str(x)
# "Division Error?"

x
1/0.1

l1 = Link(1)
l2 = Link(2)
l1.rest = l2 # mutating

l = Link(1, Link(2)) # non-mutating



def nonMutativeLink(l, func):
    """
    Take in l, a link, apply func to the first of each link in l,
    then return the modified linked list
    >>> l = Link(2, Link(3, Link(4)))
    >>> add2 = lambda x: x + 2
    >>> x = nonMutativeLink(l, add2)
    >>> str(x)
    <4, 5, 6>
    >>> str(l)
    <2, 3, 4>
    """

    if l is Link.empty: # () == ()
        return Link.empty # l
    else: # l is a link of 1 or more links
        return Link(func(l.first), nonMutativeLink(Link.rest, func))
        # Link(add2(2))
        # Link(4, Link(5, Link(6)))

def mutativeLink(l, func):
    """
        Take in l, a link, apply func to the first of each link in l,
        then return the modified linked list
        >>> l = Link(2, Link(3, Link(4)))
        >>> add2 = lambda x: x + 2
        >>> x = nonMutativeLink(l, add2)
        >>> str(x)
        <4, 5, 6>
        >>> str(l)
        <4, 5, 6>
    """
    if l is Link.empty:
        return l # Link.empty
    else: # l = Link(2)
        l.first = func(l.first)
        mutativeLink(l.rest, func)
        return l

def wonderificandogeneratorswithlinks...():


# https://inst.eecs.berkeley.edu/~cs61a/fa17/assets/pdfs/61a-fa17-mt2.pdf#page=4
# def splink(a, b, k):
#     """Return a Link containing the first k elements of s, then all of b, then the rest of a.
#
#     >>> splink(Link(2, Link(3)))
