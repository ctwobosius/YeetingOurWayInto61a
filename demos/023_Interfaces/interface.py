"""Inter-face, enter the face"""

class Villain():
    """The interface for Villains"""

    def __init__(self, name, skillz):
        self.name = name
        self.skillz = skillz
        self.dead = False

    def attack(self):
        """Prints out the villain's attack message"""
        assert False, "Haven't defined attack() yet"

    def laugh(self):
        """Prints out the villain's signature laugh"""
        assert False, "Haven't defined laugh() yet"

    def launchNuke(self):
        """Prints out the villain's nuclear power"""
        assert False, "If your python program was dealing with nuclear launch codes, assert becomes way more important (stopping program if wrong input)"

    def set_dead(self, ded):
        """
        Sets the villain to be DED

        (Sets the attribute dead to be DED)"""
        self.dead = ded


class DarthVader(Villain):
    def attack(self):
        print("Tschhh Hum Bzzzt")

    def laugh(self):
        print("I do not laugh.")

    def forcePush(self):
        print("Fwoosh (no that's not the toilet)")

    def launchNuke(self):
        print("You may fire when ready...wait that's Tarkin's line")

class Zombie(Villain):
    def attack(self):
        print("Grahhh!")
        return "bitten"

    def laugh(self):
        print("Rawrgh?")

    def launchNuke(self):
        print("There is no nuke here")


# bob = Villain("bob", "name without caps")
# bob.laugh()
#
# dv = DarthVader("Darth Vader", "Big scary force powers")
# dv.laugh()
# dv.forcePush()
#
# z1 = Zombie("zomb1", "slow movement, lack of brain")
# z1.laugh()
