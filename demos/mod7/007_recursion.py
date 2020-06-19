""" Recursively doing Recursion...hm... """

def dream_within_a(dream):
    print(dream)
    return dream_within_a(dream)


# def sum_from_zero_to(n):
#     if ____ <= 0:
#         return 0
#     else:
#         return ____
#
#
# print(sum_from_zero_to(5))


# """ 100 factorial (written as 100!) is 100 * 99 * 98 * ... * 2 * 1.
# 0! is 1.
# Could use for loop; but there is another.
# """
# def factorial(n):
#     if n <= ____:
#         return ____
#     return factorial(____) * ____
#
#
#
# def factorial_iter(n):
#     if n <= ____:           # to deal with negative n
#         return 1
#     product = n             # start product at n
#     for i in range(____, ____):   # for each number from 1 all the way to n-1,
#         product *= i        # multiply it with our product
#     return ____
#
# print(factorial(5))
# print(factorial_iter(5))
