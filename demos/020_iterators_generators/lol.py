d = {0: "water", 1: "fire", 2: "earth", 3: "nitrogen"}

# v = {"water", "fire", "earth"}
v = iter(d.values())

# k = {0, 1, 2}
k = iter(d.keys())

for value in v:
    naming_is_hard = next(k)
    if value == "nitrogen":
        print(naming_is_hard)


def g():
    return 1
    return 2


def gen():
    yield 1
    yield 2
    yield 3



x = iter([23])
x = gen()
next(x) # 1
next(x) # 2
next(x) # 3
y = gen()
z = gen()
next(y)
next(z)
next(y)


def big_name():
    lst = [1, 2, 3]
    for i in lst:
        yield i

def big_name():
    lst = [1, 2, 3]
    yield from lst

x = big_name()
next(x)
1
next(x)
2
next(x)
3
next(x)
StopIteration error


# Infinite generation: Create a function that yields a cycle of LST:
# lst = [1, 2, 3]
# x = gen(lst)
# next(x)
# 1
# next(x)
# 2
# next(x)
# 3
# next(x)
# 1
# next(x)
# 2
# next(x)
# 3
# next(x)
# 1
# next(x)
# 2
# ...
def gen(lst):
    i = ____
    while ____:
        if _____:
            yield lst[i] # lst[0]
            _____
        else:

            yield lst[____]
            ____





























# solution:
# def gen(lst):
#     i = 0
#     while True:
#         if i < len(lst):
#
#             yield lst[i] # lst[0]
#             i += 1
#         else: # if hit end
#
#             yield lst[0] # lst[0]
#             i = 1
