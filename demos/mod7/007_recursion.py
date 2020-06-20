""" Recursively doing Recursion...hm...
By Calvin Wong
"""

""" Recursion is simply calling the function in your definition!
You need at least 2 things:
Base case: This stops the function from continuing to call itself forever.
Recursive case(s): This does the stuff in between the base case and your first case.
"""

def dream_within_a(dream):
    if dream < 0:
        return
    print(dream)
    return dream_within_a(dream - 1)


def sum_from_zero_to(n):
    if n <= 0:
        return 0
    else:
        return n - 1  + sum_from_zero_to(n - 1)

# Leap of method:
"""
Assuming arg < original n
sum_from_zero_to(arg)
sum_from_zero_to(n - 1) -> n - 1 + n - 2 +

"""

print(sum_from_zero_to(3))


""" 100 factorial (written as 100!) is 100 * 99 * 98 * ... * 2 * 1.
0! is 1.
Could use for loop; but there is another.
"""
def factorial(n):
    if n <= 1:
        return 1
    return factorial(n - 1) * n
# 3 * 2 * 1
# factorial(-1)

def factorial_iter(n):
    if n <= 1:           # to deal with negative n
        return 1
    product = n             # start product at n
    for poop in range(1, n):   # for each number from 1 all the way to n-1,
        product *= poop        # multiply it with our product
    return product

print(factorial(6))
print(factorial_iter(6))
