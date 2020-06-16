""" OOP part 2! Inheritance (No, it's not a large sum of money)
--------------------------------------------------------------------------------
There can be a heirarchy of classes! If class 2 inherits from class 1, then
class 2 has all of class 1's properties (methods, attributes, etc.)

The topmost class that everything inherits from is object. That's why everything
is an object. Mind = "blown again"

We say that object is the "parent class."

From there, the "child classes" inherit from the parent class.
"""

class Student(): # equivalent to class Student(object), the default parent class is object
    skool = "random school"
    num_dogs = 1

    def __init__(self, name, description):
        self.name = name
        self.descrip = description
        self.num_gorillas = 0
        self.fuds_eated = 1

    def study(self):
        print("Needa snack")
        self.fuds_eated += 1

    def chant(self):
        print("Generic school chant!")

class BroccoliStudent(Student): # inherits from Student class!
    skool = "UC Broccoli"

    def chant(self):
        print("Go bears lol")

class cs61a(BroccoliStudent):
    def study(self):
        print("I heard this is the part where EECS kids forget to shower")
        # super() uses the parent class, so
        super().study() # this is equivalent to self.study() but as if we
                        # were in the parent class (BroccoliStudent)

jimmy = Student("Jimmy", "High school student, never tardy.")
upgraded_jimmy = BroccoliStudent("Jim", "Goes to school. Most of the time. Probably.")
ascended_jimmy = cs61a("J-man", "Webcasts everything, sleeps in til 3pm")
# disclaimer: It is advisable NOT to be like ascended_jimmy

# WWPD (What Would Python Display)? Are there any errors?
jimmy.chant() # don't forget to check if the methods print something!
upgraded_jimmy.chant()
ascended_jimmy.chant()

jimmy.study()
upgraded_jimmy.study()
ascended_jimmy.study()

print(jimmy.fuds_eated)
print(ascended_jimmy.fuds_eated)

Student.study(jimmy)
Student.study("Unknown student")

Student.num_dogs = 3
print(Student.num_dogs)
print(BroccoliStudent.num_dogs)
print(cs61a.num_dogs)

BroccoliStudent.num_dogs = 50
print(Student.num_dogs)
print(BroccoliStudent.num_dogs)
print(cs61a.num_dogs)
