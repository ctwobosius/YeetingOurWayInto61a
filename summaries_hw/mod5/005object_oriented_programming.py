""" Object Oriented Programming, or as CS peeps like to say, OOP
By Calvin Wong
"""

"""
EVERYTHING in Python is an Object! But what is an object?
    You can think of objects as "upgraded" variables.
    A box that holds its own:
        methods         A method is just a FUNCTION that
                        belongs to an object
        attributes      A VARIABLE that belongs to an object (can be instance or class)
        constructor     The function that allows you to create that object

Classes are the blueprints for objects. You use classes to create "instances"
of an object. Let's try to put this in English:

    We want a Student blueprint, where if we create new students, they each
    have a name and a description.

    If we wanted to create two such students:

    Joe = Student("Bad Joe-k", "Likes to say Joe Mama for some reason")

    SunTzu = Student("Sunny Boi", "Randomly spouts a lotta quotes")

    Here's how we do create the Student class:

"""
class Student():
    # class variables, becomes more clear below
    skool = "UC Broccoli"
    num_dogs = 1
    # skool is the class variable/attribute "skool", the indent signifies it's
    # part of the Student class

    # functions within the class are called methods
    def __init__(self, name, description): # the underscores __ are just Python naming convention
        """
        The init method, also known as the constructor method, is what is called
        when you create an instance. You always need the self argument for each
        method, and self refers to the instance.

        This will become more clear below!
        """
        self.name = name # self.name refers to the instance variable "name"
        # these instance variables are also called "instance attributes"
        self.descrip = description
        self.num_gorillas = 0
        self.fuds_eated = 1

    def set_school(self, s): # another method
        self.skool = s

    def gorilla_UP(self):
        self.num_gorillas += 1

    def eat(self):
        self.fuds_eated *= 2

    def lol(self):
        cake = 3


# also to put a quote within a string, you do:
"George Washington once famously said, \"Yo bro I think my teeth be falling out or something\""

# On to instances!
Joe = Student("Bad Joe-k", "Likes to say Joe Mama for some reason")
"""
This is the same as calling

Student.__init__(Joe, "Bad Joe-k", "Likes to say Joe Mama for some reason")

and Joe, the variable, becomes an "instance" of the class Student that stores
    "Joe" as Joe.name
    "Likes to say Joe Mama for some reason" as Joe.descrip

Do you see how we passed in Joe as self, so "self.descrip" became the equivalent of "Joe.descrip"?


Whenever you do instance.variable, it first looks if it has any attributes
of that name. Then, if it can't find it, it looks in the class variables. Then it
errors if it still can't find it.

>>> Joe.name
"Bad Joe-k"
    This looks in the "self" first to see if it has a self.name.
    We set self.name to "Bad Joe-k" when we called the __init__ constructor in line 57,
    so that's what it returns.

>>> Joe.num_dogs
1
    There's no self.num_dogs, but it looks in class variables and finds num_dogs there.

>>> Joe.answer_to_life
Error!
    Because there's no such variable. Also, there probably is no satisfactory answer.

The special thing about class variables is that you can use the Class without
instances to get the variable! For example:

>>> Student.num_dogs
1

>>> Student.name
Error
    There's no class variable called name.

The way you call a method is by using
>>> instance.method(arguments*)
and instance is automatically passed in as self, so don't put an argument for self!

For example:

>>> Joe.set_school("idk") # Joe is automatically passed in as self, "idk" is passed as s
>>> Joe.skool
"idk"
"""

# Take a look at this:
"Hello {name}".format(name="World!")
"""
Everything is an object! "Hello {name}" is an instance of the String class,
and format is a method of the String class!

[3, 4].pop() <- Lists too! EVERYTHING is an object in Python!

Did I blow your mind? ;D
"""

# Note: \ allows you to continue a line so you don't have to put it all in one line
Calvin = Student(
    "Fat Reptile",
    "Sits around all day and gets called Fat Reptile" + \
    "by his roomate, who claims Calvin \"has no feet.\" Throws " + \
    "weird insults back, like calling his roommate a Stinky Amphibian."
)


"""
Homework: create your own Student instance! You can do one of yourself, or your
friends, or maybe pretend your parents are students and do one for them!

I created mine as Fat Reptile lol, if you'd like email me your instance
(also so I can know yall better halp wit dat plez)

After that, answer the following What Would Python Print?
(in 61a it's called WWPD, What Would Python Display)
"""
# What would these print?

print(Calvin.name)
print(Calvin.descrip)
print(Calvin.skool)

Calvin.set_school("Stanfurd lol")
print(Calvin.skool)

print(Joe.skool)

print(Calvin.gorilla_UP())
print(Calvin.num_gorillas)
print(Joe.num_gorillas)

Joe.lol()
# print(Joe.cake)

print(Student.num_dogs)
print(Joe.num_dogs)
print(Calvin.num_dogs)

Student.num_dogs += 99
print(Student.num_dogs)
print(Joe.num_dogs)
print(Calvin.num_dogs)

Calvin.num_dogs -= 50
print(Student.num_dogs)
print(Joe.num_dogs)
print(Calvin.num_dogs)
