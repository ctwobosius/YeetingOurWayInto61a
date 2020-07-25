"""BIG OOPs"""

"""
class Classname:
    class_attributes = "available for any instance"

    def __init__(self, args):
        # called whenever you create an instance of Classname
        # usually you define initial attributes here
        self.attribute = "something"
        doSomethingElse()

    def method(self, args):
        # this works like any other function, except for the part where you pass in self
        # here you do stuff you want self, the instance to be able to do after initializing
        self.attribute += "something else"
        self.class_attribute = "class_attribute gets overriden just for this instance"
        return 1 + 34 - 3

    def get_attribute(self):
        # This is just another way to get self.attribute using abstraction
        return self.attribute

    def set_attribute(self, val):
        self.attribute = val + "color"


mice1.color = "red"
mice1.set_color("red")
mice.color
mice2.color = "red"




instance1 = Classname(args) # make an instance of Classname named instance1
# Classname.__init__(instance1, args)
bob = Student("bob", "afro")

class Mouse():
    has_wire = "yes"

    def __init__(self, diggitydoo):
        self.color = diggitydoo
        # mice1.color = "red"
        # mice1.color

mice1 = Mouse("red")
Mouse.__init__(mice1, "red")

instance1.method()
num_hotdogs_eaten = bob.eat(args)

Student.eat(bob, args)

instance1.attribute         # if it can't find attribute in instance1, looks in Classname's class_attributes
Classname.class_attribute
instance1.method(args)      # instance1 is automatically passed in as self using the dot notation
                            # equivalent to Classname.method(instance1, args)
instance1.get_attribute() = 3   # bad, this tries to set the return value of a function
instance1.set_attribute(3)      # do this instead, or directly do
instance1.attribute = 3
"""


class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)
    >>>  "<5 7 <8 9>>"
    <5 7 <8 9>>
        print str -> __str__
        instance -> __repr__

        empty = ()
    """


    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2
        Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        print(t2)
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()



def f():

    sum = 33
    if b == true:
        sum(3)
        return 4
    elif b == false:
        return 3
    else:
        return 32


if b:
    return 4
return 3
