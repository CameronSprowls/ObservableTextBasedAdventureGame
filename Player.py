"""
This represents the player of the game
"""

from Weapon import *
import random


class Player:

    is_dead = False

    def __init__(self):
        # TODO: make the player not a god anymore (remove three zeros from randoms)
        self.health = random.randint(100000, 125000)
        self.attack_value = random.randint(1000, 2000)
        self.in_home = "in_home"
        self.is_dead = False

        # Generate the weapons the player starts with and them to his inventory
        self.inventory = []
        self.gen_weapons()

    @property
    def health(self):
        return self.__health

    @property
    def attack_value(self):
        return self.__attack_value

    @property
    def in_home(self):
        return self.__in_home

    @property
    def inventory(self):
        return self.__inventory

    @health.setter
    def health(self, health):
        self.__health = health

    @attack_value.setter
    def attack_value(self, attack_value):
        self.__attack_value = attack_value

    def add_to_inventory(self, item):
        self.__inventory.append(item)

    @in_home.setter
    def in_home(self, in_home):
        self.__in_home = in_home

    @inventory.setter
    def inventory(self, inventory):
        self.__inventory = inventory

    def get_is_dead(self):
        return self.is_dead

    def gen_weapons(self):
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

    def attack(self, name_of_attack):
        # Make all of the monsters in the current home attack the player
        for x in self.in_home.get_monsters():
            self.health -= x.attack_strength

        if self.health < 0:
            self.is_dead = True

        # Find the weapon that attacked, handle it properly
        for x in self.inventory:
            # If the name of the attack matches a weapon in our inventory, use that weapon
            if x.name == name_of_attack:
                x.uses -= 1

                damage_dealt = self.attack_value * x.attack_modifier

                # If that weapon has no more uses, get rid of it
                if x.uses is 0:
                    self.inventory.remove(x)

                return damage_dealt
