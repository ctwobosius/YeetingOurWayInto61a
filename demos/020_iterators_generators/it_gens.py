"""It rains, it pours, it gens, it-erators gen-erators"""

"""

"""

pizza = ["r", "i", "p", "p", "e", "r", "o", "n", "i"]
print(next(pizza))
weird = iter(pizza)
print(pizza[0])
print(weird[0])

print(next(weird))
next(weird)
next(weird)

print([pepper for pepper in weird])
print([pepper for pepper in pizza])
