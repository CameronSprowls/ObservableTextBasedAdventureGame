"""
Class for a home.

Homes observe the monsters living within, will be notified when a monster in defeated


"""

from Monster import *
from Observer import Observer
from Enums import Monsters


class Home(Observer):

    monsters = []

    @staticmethod
    def main():
        print(Home)

    def __init__(self):
        """
        Constructor of a home. Set up all the basic properties of one
        """

        # Create a random (0-10) number of monsters in the house
        self.gen_monsters(random.randint(1, 10))

    def gen_monsters(self, num_monsters):
        """
        Get random monsters an populate the house with them
        :param num_monsters: the number of monsters that is to be
                             place inside of the house
        """
        # Decide a random number of monsters to add to the home
        for x in range(0, num_monsters):
            # Create random monster, add to home
            monster_id = Monsters(random.randint(1, 4))
            if monster_id is Monsters.ZOMBIE:
                self.monsters.append(Zombie(self))
            elif monster_id is Monsters.VAMPIRE:
                self.monsters.append(Vampire(self))
            elif monster_id is Monsters.GHOUL:
                self.monsters.append(Ghoul(self))
            else:
                self.monsters.append(Werewolf(self))

    def notified_place_holder(self, monster):
        """
        Removes a monster from a house when notified that it was defeated and replaces
        that monster with a new person
        :param monster: The monster that is to be removed
        """
        # Remove monster, place person
        self.monsters[monster] = Person(self)
        print("notified_place_holder")

    def update(self, *args, **kwargs):
        pass
