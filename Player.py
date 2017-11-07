"""
This represents the player of the game
"""

from Weapon import *
import random


class Player:

    is_dead = False

    def __init__(self):
        """
        Constructor for the player
        """
        self.health = random.randint(1000, 1250)
        self.attack_value = random.randint(10, 20)
        self.in_home = "in_home"
        self.is_dead = False

        # Generate the weapons the player starts with and them to his inventory
        self.inventory = []
        self.gen_weapons()

    @property
    def health(self):
        """
        Returns the player's health
        :return Int of the player's health
        """
        return self.__health

    @property
    def attack_value(self):
        """
        Gets the attack value of the player, used for calculating damage
        :return: int of the attack value of the player
        """
        return self.__attack_value

    @property
    def in_home(self):
        """
        Gets the home that the player is in
        :return: Home that the player is in
        """
        return self.__in_home

    @property
    def inventory(self):
        """
        Gets the inventory of the player
        :return: List of Weapons that are in the player's inventory
        """
        return self.__inventory

    @health.setter
    def health(self, health):
        """
        Sets the health of the player to a new value
        :param health: The new health to be set
        """
        self.__health = health

    @attack_value.setter
    def attack_value(self, attack_value):
        """
        Sets the attack value to a new value
        :param attack_value: The new attack value to be set
        :return:
        """
        self.__attack_value = attack_value

    def add_to_inventory(self, item):
        """
        Adds an Item to the player's inventory
        :param item: Thing that is to be added to the player's inventory
        """
        self.__inventory.append(item)

    @in_home.setter
    def in_home(self, in_home):
        """
        Sets the a new home that the player is in
        :param in_home: Home that the player is to be moved to
        """
        self.__in_home = in_home

    @inventory.setter
    def inventory(self, inventory):
        """
        Sets the inventory of the player to a whole new inventory
        :param inventory: Inventory that is to be the new invenotry
        :return:
        """
        self.__inventory = inventory

    def get_is_dead(self):
        """
        Returns if the player is dead or not
        :return: True if they are dead, false otherwise
        """
        return self.is_dead

    def gen_weapons(self):
        """
        Generator to create and add items to the players inventory, used on creation
        """
        # Add the default Hershey's Kiss to the players inventory
        self.add_to_inventory(HersheyKiss())
        # Create 9 weapons because one needs to be a hershey's kiss
        for x in range(1, 10):
            # Create random weapon and add it to inventory
            weapon_id = Weapons(random.randint(1, 3))

            if weapon_id is Weapons.SOUR_STRAW:
                self.add_to_inventory(SourStraw())
            elif weapon_id is Weapons.CHOCOLATE_BAR:
                self.add_to_inventory(ChocolateBar())
            elif weapon_id is Weapons.NERD_BOMB:
                self.add_to_inventory(NerdBomb())

    def attack(self, attack_weapon):
        """
        Calculates the damage that the player does with the weapon passed
        :param attack_weapon: The Weapon.TYPE of the weapon they're using to attack
        :return Int: the end result of the damage they dealt
        """
        # Make all of the monsters in the current home attack the player
        for x in self.in_home.get_monsters():
            self.health -= x.attack_strength

        if self.health < 0:
            self.is_dead = True

        # Find the weapon that attacked, handle it properly
        for x in self.inventory:
            # If the name of the attack matches a weapon in our inventory, use that weapon
            if x.get_type() is attack_weapon:
                x.uses -= 1

                damage_dealt = self.attack_value * x.attack_modifier

                # If that weapon has no more uses, get rid of it
                if x.uses is 0:
                    self.inventory.remove(x)

                return damage_dealt
