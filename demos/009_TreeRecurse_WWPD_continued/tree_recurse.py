""" Tree Recursion: Recursion, except there's trees?
By Calvin
"""
def f(n):
    if n < 3:
        return 3
    return f(n-1)

# 0 = 1
# 1 = 1
# 2 = 1 + 1 = 2
# 3 = 2 + 1 = 3 = f(3) + f(2)
# 4 = 3 + 2 = 5
# f(5) = 5 + 3 = f(4) + f(3)
# f(500) = f(499) + f(498)
# f(501) = f(500) + f(499)

def fib(n):
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)
    # memoization


class Node():

    def __init__(self, val=0, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

    def empty(self):
        return not self.left and not self.right


t1 = Node(1)
t3 = Node(3)
t5 = Node(5)
t9 = Node(9)
t1.left = t3
t1.right = t9
t3.left = t5

# def find(n, topNode):
#     if ____:
#         return ____
#     elif ____:
#         return True
#     else:
#         return find(____, ____) ____ find(____, ____)

# find(3, t1)
# find(4, t1)
# find(5, t1)

# WWPD

def w(L):
    if len(L) == 0:
        return L
    elif L[0] in L[1:]:
        return w(L[1:])
    else:
        return [L[0]] + w(L[1:])

def reduc(e, L, first):
    if len(L) <= 0:
        return first
    else:
        return reduc(e, L[1:], e(first, L[0]))

print(0) and print(98)
range(1, 50)[-1]
(6 and 7) or (4 or 3) + (0 and 2)
mp4 = lambda asdf: asdf
rar = lambda movie: mp4(rar)
# def rar(movie):
#     return mp4(rar)
rar(2)(2) = function rar
w([1, 2, 3, 1, 8, 2])

f = lambda x: lambda y: lambda z: x+y+z
reduc(lambda g, x: g(x),[2, 4, 6], f)

# ED:
x = f(4)(3)
