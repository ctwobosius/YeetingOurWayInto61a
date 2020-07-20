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
print(x)
x
str(x)

def nonMutativeLink(l, func):
    if ____:
        return ____
    else:
        return ____

def mutativeLink(l, func):
    if ____:
        ____
    else:
        ____
        ____
        return ____

# https://inst.eecs.berkeley.edu/~cs61a/fa17/assets/pdfs/61a-fa17-mt2.pdf#page=4
# def splink(a, b, k):
#     """Return a Link containing the first k elements of s, then all of b, then the rest of a.
#
#     >>> splink(Link(2, Link(3)))
