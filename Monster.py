"""
Huge file containing all of the monsters in the game


TODO: figure out if I want to make the Monster class implement the weaknesses and resistances or if I want the children
      to do it

"""
import random

from Observable import Observable


class Monster(Observable):
    """
    Parent class of all of the monsters, as generic as possible
    Home observes monster
    """

    def __init__(self, attack_range, health_range, weaknesses, resistances, home):
        super().__init__()
        super().sub(home)

        self.attack_strength = random.randint(attack_range[0], attack_range[1])
        self.health_points = random.randint(health_range[0], health_range[1])
        self.weaknesses = weaknesses
        self.resistances = resistances

    # Properties of the monster class
    @property
    def attack_strength(self):
        return self.__attack_strength

    @property
    def health_points(self):
        return self.__health_points

    # Setters for everything with a property because apparently you need them
    @attack_strength.setter
    def attack_strength(self, attack_strength):
        self.__attack_strength = attack_strength

    @health_points.setter
    def health_points(self, health_points):
        self.__health_points = health_points


class Person(Monster):
    """
    A Person, someone who helps the player by giving them candy.
    """

    def __init__(self, home):
        super().__init__((-1, -1), (100, 100), [], [], home)


class Zombie(Monster):
    """
    A Zombie, a basic monster weak to SourStraws.
    """

    def __init__(self, home):
        super().__init__((0, 10), (50, 100), [], [], home)


class Vampire(Monster):
    """
    A Vampire, a monster immune to ChocolateBars.
    """

    def __init__(self, home):
        super().__init__((10, 20), (100, 200), [], [], home)


class Ghoul(Monster):
    """
    A Ghoul, a monster weak to NerdBombs
    Child of Monster
    """

    def __init__(self, home):
        super().__init__((15, 30), (40, 80), [], [], home)


class Werewolf(Monster):
    """
    A Werewolf, a fierce monster immune to ChocolateBars and SourStraws.
    """

    def __init__(self, home):
        super().__init__((0, 40), (200, 200), [], [], home)
