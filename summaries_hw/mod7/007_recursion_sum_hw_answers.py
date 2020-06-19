""" Recursively doing Recursion...hm...Version: homework"""

import random

def countdown(n):
    if n <= 0:
        print(n) # or print(0) works
        print("Blastoff!")
        print("...")
        print("I said blastoff, ya monkeys, why aren't we moving?! Push the button!!!")
    else:
        print(n)
        return countdown(n - 1)

print("Counting down:")
countdown(3)

def random_sum(n):
    if n <= 0:
        return 0 # technically you could say n but the sum of -2 numbers doesn't make sense anyway
    else:
        return random.randint(1, 10) + random_sum(n - 1)

print()
print("Random sum: ")
print(random_sum(3)) # Should be between 3 and 27 (each random number is min 1, max 9, so min is 1 * 3, max 9 * 3)
