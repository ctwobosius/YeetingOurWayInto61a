""" Object Oriented Programming, or as cs peeps like to say, OOP """

"""
EVERYTHING in Python is an Object! But what is an object?
    You can think of objects as "upgraded" variables.
    A box that holds its own:
        methods         A method is just a FUNCTION that
                        belongs to an object
        attributes      A VARIABLE that belongs to an object
        constructor     The function that allows you to create that object

Classes are the blueprints for objects. You use classes to create "instances"
of an object. Let's try to put this in English:

    We want a Student blueprint, where if we create new students, they each
    have a name and a description.

    If we wanted to create two such students:

    Benel = Student("Benel", "Sick Yoga-ist and Taiji-ist with some dope Kungfu
    and hiking background. Asks great questions and loves to learn.")

    Calvin = Student("Fat Reptile", "Sits around all day and gets called Fat Reptile
    by his roomate, who claims Calvin "has no feet." Throws weird insults back, like
    calling his roommate a Gross Amphibian.")

    Here's how we do create the Student class:

"""
class Student(): # equivalent to class Student(object), the default parent is class
    num_wheels = 4
    gas = 30
    headlights = 2
    size = 'Tiny'

    def __init__(self, name, description):
        pass


# Note: \ allows you to continue a line so you don't have to put it all in one line
# also to put a quote within a string, you do:
"Sun Tzu once famously said, \"\""

Joe = Student("Joe", "Likes to say Joe Mama for some reason")

Benel = Student("Benel", """Sick Yoga-ist and Taiji-ist with some dope Kungfu" + \
and hiking background. Asks great questions and loves to learn.""")

Calvin = Student("Fat Reptile",
    "Sits around all day and gets called Fat Reptile" + \
    "by his roomate, who claims Calvin \"has no feet.\" Throws " + \
    "weird insults back, like calling his roommate a Gross Amphibian.")
