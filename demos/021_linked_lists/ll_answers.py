x = Foolz("dino")
# prints dino


print(x)
# Division Error?

x
# 1/0.1

str(x)
# "Division Error?"



def nonMutativeLink(l, func):
    if l is Link.empty:
        return Link.empty
    else:
        return Link(func(link.first), nonMutativeLink(l.rest, func))

def mutativeLink(l, func):
    if l is Link.empty:
        return l
    else:
        l.first = func(l.first)
        mutativeLink(l.rest, func)
        return l
