class Hooman():
    onions_eaten = 45
    birbs_seen = 0

    def __init__(self, n, d):
        self.name = n
        self.descrip = d
        self.health = 5

    def eat(self, hp):
        self.health += hp
        Hooman.onions_eaten += 1

    def yeet(self):
        Hooman.birbs_seen += 1

    def repeat(self):
        return "Somehow, we skipped waking up and sleeping"

class DoggoOwner(Hooman):
    birbs_seen = 100

    def repeat(self):
        return "Pet the doggo :3"

    def yeet(self):
        super().yeet()
        DoggoOwner.birbs_seen += 9
        print(DoggoOwner.birbs_seen)
