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

def find(n, topNode):
    if not topNode or topNode.empty():
        return False
    elif topNode.val == n:
        return True
    else:
        return find(n, topNode.left) or find(n, topNode.right)

find(3, t1)
find(4, t1)
find(5, t1)



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
rar(2)(2)
w([1, 2, 3, 1, 8, 2])

f = lambda x: lambda y: lambda z: x+y+z
reduc(lambda g, x: g(x),[2, 4, 6], f)

# ED:
x = f(4)(3)
