"""
Huge file to hold all of the weapons
"""

import math
import random

from Enums import Weapons


class Weapon:

    def __init__(self, name, attack_modifier, uses, type):
        self.name = name
        self.attack_modifier = attack_modifier
        self.uses = uses
        self.type = type

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

    def get_type(self):
        return self.type

    def use_weapon(self):
        print("Weapon uses ", self.uses)
        self.uses -= 1


class HersheyKiss(Weapon):
    """
    A Hershey's Kiss, a basic weapon that deals low damage but has unlimited uses.
    """

    def __init__(self):
        super().__init__("Hershey's Kiss", 1, math.inf, Weapons.HERSHEY_KISS)

    def use_weapon(self):
        super().use_weapon()


class SourStraw(Weapon):
    """
    A Sour Straw, a decent weapon that has a limited number of uses
    """

    def __init__(self):
        super().__init__("Sour Straw", float(random.randint(100, 175)/100), 2, Weapons.SOUR_STRAW)

    def use_weapon(self):
        super().use_weapon()


class ChocolateBar(Weapon):
    """
    A chocolate bar, a decent weapon that has a lot of uses
    """
    def __init__(self):
        super().__init__("Chocolate Bar", float(random.randint(200, 240)/100), 4, Weapons.CHOCOLATE_BAR)

    def use_weapon(self):
        super().use_weapon()


class NerdBomb(Weapon):
    """
    A Nerd Bomb, an amazing weapon, unfortunately they only have one use
    """
    def __init__(self):
        super().__init__("Nerd Bomb", float(random.randint(350, 500)/100), 1, Weapons.NERD_BOMB)

    def use_weapon(self):
        super().use_weapon()
