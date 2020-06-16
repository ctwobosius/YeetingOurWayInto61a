"""
Create a dictionary for our next ice breaker (June 17). The problem is:
    Make a dictionary that contains two key-value pairs with the keys being the
    name of someone in your cohort as a string and the value being a string of
    something you like about them.

You can pop a value by it's index by putting the index between the parentheses.
"""

>>> list1 = [1,2,3,4]
>>> list1.pop(2)
3
>>> list1
[1,2,4]

"""
Remove only removes by element. If there are multiple of the same element in the
list, it removes the first one.
"""
>>> list2 = ["b", "a", "n", "a", "n", "a"]
>>> list2.remove("a")
>>> list2
["b", "n", "a", "n", "a"]

"""
And here's a link on more about dictionaries (everything in the link is covered in 61A).
https://www.w3schools.com/python/python_dictionaries.asp

Something important that the website does not include is that you can use:
dictionary.get(key, value)
Which will give you value if key doesn't exist. For example:
"""
>>> dict = {"apple": "red", "pineapple": "yellow"}
>>> dict.get("peaches", 0)
0
