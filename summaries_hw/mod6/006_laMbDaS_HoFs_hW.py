""" Higher Order Lambdas: The Fun-ing
By Calvin Wong

Once upon a time,
Somebody created homework (optional)
Then asked first what does the last line do
Then asked for the environment diagram
And then everyone had fun
The end

Lol
"""

def elf(hat):
    print(hat)
    return 30

def beardless(hagrid):
    hair = lambda what: what + hagrid
    return hair

print(beardless(5)(elf(3)))
