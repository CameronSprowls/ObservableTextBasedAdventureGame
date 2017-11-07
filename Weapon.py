"""
Huge file to hold all of the weapons
"""

import math
import random

from Enums import Weapons


class Weapon:

    def __init__(self, name, attack_modifier, uses, type):
        """
        Constructor for a generic weapon
        :param name: Name of the weapon
        :param attack_modifier: How much this weapon will multiply the players damage by
        :param uses: How many times the weapon can be used
        :param type: Enum type of the weapon
        """
        self.name = name
        self.attack_modifier = attack_modifier
        self.uses = uses
        self.type = type

    # Properties of the weapon class
    @property
    def name(self):
        """
        Returns the name of the weapon
        :return: name of the weapon
        """
        return self.__name

    @property
    def attack_modifier(self):
        """
        Returns the attack modifier of the weapon
        :return: attack modifier of the weapon
        """
        return self.__attack_modifier

    @property
    def uses(self):
        """
        Returns the remaining uses of the weapon
        :return: remaining uses of the weapon
        """
        return self.__uses

    # Setters for everything with a property because apparently you need them
    @name.setter
    def name(self, new_name):
        """
        Changes the name of the weapon to something new
        :param new_name: New name of the weapon
        """
        self.__name = new_name

    @attack_modifier.setter
    def attack_modifier(self, new_attack_modifier):
        """
        Changes the attack modifier of the weapon to something new
        :param new_attack_modifier: New attack modifier of the weapon
        """
        self.__attack_modifier = new_attack_modifier

    @uses.setter
    def uses(self, new_uses):
        """
        Changes the uses of a weapon to something new
        :param new_uses: New uses of the weapon
        """
        self.__uses = new_uses

    def get_type(self):
        """
        Returns the Enum type of the weapon
        :return: Enum type of the weapon
        """
        return self.type

    def use_weapon(self):
        """
        Uses the weapon, call when need to use it for an attack
        """
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
