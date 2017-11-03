"""
Huge file to hold all of the weapons
"""

import math
import random


class Weapon:

    def __init__(self, name, attack_modifier, uses):
        self.name = name
        self.attack_modifier = attack_modifier
        self.uses = uses

    # Properties of the weapon class
    @property
    def name(self):
        return self.__name

    @property
    def attack_modifier(self):
        return self.__attack_modifier

    @property
    def uses(self):
        return self.__uses

    # Setters for everything with a property because apparently you need them
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @attack_modifier.setter
    def attack_modifier(self, new_attack_modifier):
        self.__attack_modifier = new_attack_modifier

    @uses.setter
    def uses(self, new_uses):
        self.__uses = new_uses

    def use_weapon(self):
        self.uses -= 1


class HersheyKiss(Weapon):
    """
    A Hershey's Kiss, a basic weapon that deals low damage but has unlimited uses.
    """

    def __init__(self):
        super().__init__("Hershey Kiss", 1, math.inf)

    def use_weapon(self):
        super().use_weapon()


class SourStraw(Weapon):
    """
    A Sour Straw, a decent weapon that has a limited number of uses
    """

    def __init__(self):
        super().__init__("Sour Straw", 2, float(random.randint(100, 175)/100))

    def use_weapon(self):
        super().use_weapon()


class ChocolateBar(Weapon):
    """
    A chocolate bar, a decent weapon that has a lot of uses
    """
    def __init__(self):
        super().__init__("Chocolate Bar", 4, float(random.randint(200, 240)/100))

    def use_weapon(self):
        super().use_weapon()


class NerdBomb(Weapon):
    """
    A Nerd Bomb, an amazing weapon, unfortunately they only have one use
    """
    def __init__(self):
        super().__init__("Nerd Bomb", 1, float(random.randint(350, 500)/100))

    def use_weapon(self):
        super().use_weapon()
