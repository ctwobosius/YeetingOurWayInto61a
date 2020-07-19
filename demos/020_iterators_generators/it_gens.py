"""It rains, it pours, it gens, it-erators gen-erators"""

"""

"""

lst = [1, 2, 3]
x = iter(lst)
next(x)
1
next(x)
2
next(x)
3
# next(x)
# StopIteration Error

y = iter(lst)
next(y)
1
x


y[0]



pizza = ["r", "i", "p", "p", "e", "r", "o", "n", "i"]
# can you call next on iterables?
print(next(pizza))
# iterables vs iterators
error

weird = iter(pizza) # iter creates iterator
print(pizza[0])
# r
print(weird[0])
# error

print(next(weird))

lst
dictionary = {0: "jesus"}
string = "st"
"string"[0]
>>> dictionary[0]
"jesus"

dictionary.values()
for key in dict:
    if dict[key] == value:
        return key

iter(dictionary.values())
iter(dictionary.keys())
"fire"
1
d = {0: "water", 1: "fire", 2: "earth"}

# v = {"water", "fire", "earth"}
v = iter(d.values())

# k = {0, 1, 2}
k = iter(d.keys())

for value in v:
    naming_is_hard = next(k)
    if value == "fire":
        print(naming_is_hard)


print(next(weird)) r
next(weird) i
next(weird) p

print([pepper for pepper in weird])
print([pepper for pepper in pizza])
