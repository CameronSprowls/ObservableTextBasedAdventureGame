"""
File to hold the class for a home.

Homes observe the monsters living within, will be notified when a monster in defeated
"""

from Monster import *
from Observer import Observer
from Enums import Monsters


class Home(Observer, Observable):
    """
    Class for the home. Creates a home and has accessors and mutators.
    """

    # Instance variables
    monsters = []
    x_pos = 0
    y_pos = 0

    def __init__(self, x_pos, y_pos):
        """
        Constructor of a home. Set up all the basic properties of one
        """
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.monsters = []

        # Create a random (0-10) number of monsters in the house
        self.gen_monsters(random.randint(1, 10))

    def sub(self, new_sub):
        """Subscribe the new sub to the house service"""
        super().sub(new_sub)

    def gen_monsters(self, num_monsters):
        """
        Get random monsters an populate the house with them
        :param num_monsters: the number of monsters that is to be
                             place inside of the house
        """
        # Decide a random number of monsters to add to the home
        for x in range(num_monsters):
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

    def get_monsters(self):
        """
        Getter for the monsters.
        """
        return self.monsters

    def get_x_pos(self):
        """
        Gets the x position of house. Useful to figure out where the house is
        for movement.
        """
        return self.x_pos

    def get_y_pos(self):
        """
        Gets the y position of house. Useful to figure out where the house is
        for movement.
        """
        return self.y_pos

    def update(self, *args, **kwargs):
        """
        Called when a monster dies, replaces that monster with a person, and lets the game know
        that a monster is gone and they should update the number of monsters they have
        :param args: Monsters that were killed
        """
        # Get rid of the monsters that were passed in, replace them with Persons
        defeated = 0
        for x in args:
            for y in self.get_monsters():
                if x is y:
                    self.monsters.remove(x)
                    self.monsters.append(Person(self))
                    defeated += 1
                    break

        # Let the game know that a monster was defeated
        super().update_observers(defeated)
