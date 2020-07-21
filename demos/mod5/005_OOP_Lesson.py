""" OOP! Not oops, OOP, Object Oriented Programming!
By Calvin Wong
"""

# Sidenote: what if we want to say a quote?
"George Washington once famously said, \"Yo bro I think my teeth be falling out or something\""
# \ means take literally, instead of creating quote, literally use the character "

"""
CLASSES: blueprints for objects, create "INSTANCES" of objects

    OBJECT: "upgraded" variables. Each object has:
        METHODS             functions
        ATTRIBUTES          variables
        CONSTRUCTOR         method that creates objects

    Imagine a Student blueprint, each student has own name and description. Ex:

        Joe = Student("Bad Joe-k", "Likes to say Joe Mama for some reason")

        SunTzu = Student("Sunny Boi", "Randomly spouts a lotta quotes")

"""
name = "joe"

class Hooman():
    # class variables/attributes
    onions_eaten = 0
    birbs_seen = 0

    # methods
    def __init__(self, n, d):
        # instance variables/attributes
        # self: instances vs classes
        self.name = n
        self.descrip = d
        self.health = 5

    def eat(self, hp):
        # which one?
        # health += hp
        self.health += hp

        # which one?
        # onions_eaten += 1
        Hooman.onions_eaten += 1

        # What's the difference?


    def yeet(self):
        # birbs_seen += 1
        Hooman.birbs_seen += 1

    def repeat(self):
        return "Somehow, we skipped waking up and sleeping"


"""
Also student highlights below :))) They're based on real people in the cohort!
You know who you are ;)
"""

h0 = Hooman("Bob", "Generically named person")
# Hooman.__init__(h0, "Bob", "Generically named person")
h0.repeat()

hidden = Hooman(
    "Nottel Lin Yu",
    "Very understanding when I forgot to follow up with him, " + \
    "and he likes Spider Man! I approve of this, one of my favorite " + \
    "shows has gear that\'s similar to Spider Man\'s abilities :)"
)

ohHeccYe = Hooman(
    "Anony Musk",
    "Sick Yoga-ist and Taiji-ist with a dope Kungfu and hiking background." + \
    " Asks great questions and I get the feeling this person loves to learn." + \
    " Did you notice the Hecc in the variable name? " + \
    "Obscure reference that this person likes dogs! "
)

yuNoKnow = Hooman(
    "Hu Isdis",
    "Artist (I want to see your work at some point)" + \
    " as well as an outdoors person. Asks the teacher how they\'re doing! "
    ":OOO !!! What a great human being :\')"
)

h1 = hidden
h2 = ohHeccYe
h3 = yuNoKnow

# h1.onions_eaten = 43
# h1.name = "billby bob joe"
# Hooman.onions_eaten = 434

# class vs instance variables
print("ohHeccYe.name",          h2.name)
print("ohHeccYe.descrip",       h2.descrip,         "\n")

print("hidden.onions_eaten",    h1.onions_eaten)
print("hidden.health",          h1.health,          "\n")

print("yuNoKnow.onions_eaten",  h3.onions_eaten)
print("yuNoKnow.health",        h3.health,          "\n")

h1.eat(5)
# h1.eat()

print("hidden.onions_eaten",    h1.onions_eaten)
print("hidden.health",          h1.health,          "\n")

print("yuNoKnow.onions_eaten",  h3.onions_eaten)
print("yuNoKnow.health",        h3.health,          "\n")

# print(Hooman.class_var)
Hooman.yeet(h1)
print("Hooman.birbs_seen",      Hooman.birbs_seen)
print("yuNoKnow.birbs_seen",    yuNoKnow.birbs_seen, "\n")


[1, 2, 3].pop()
"Big {word}".format(word="Chungus")

class DoggoOwner(Hooman):
    birbs_seen = 100

    def repeat(self): # methods "class functions"
        return "Pet the doggo :3"

    def yeet(self):
        super().yeet()
        DoggoOwner.birbs_seen += 9
        print(DoggoOwner.birbs_seen)


sam = DoggoOwner("Sam", "I am, with green eggs and ham!")
print("sam.onions_eaten",       sam.onions_eaten, "\n")

print(sam.eat(1))
print("sam.onions_eaten",       sam.onions_eaten)
print("hidden.onions_eaten",    h1.onions_eaten, "\n")

print(sam.yeet())
print(sam.repeat())
print("sam.birbs_seen",         sam.birbs_seen)
print("hidden.birbs_seen",      h1.birbs_seen)

print()
print(Hooman.yeet(sam))
sam.yeet()
