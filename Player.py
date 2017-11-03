"""
This represents the player of the game
"""

from Enums import Weapons
from Weapon import *
import random


class Player:

    weapons = []

    def __init__(self):
        self.health = random.randint(100, 125)
        self.attack_value = random.randint(10, 20)

        # Generate the weapons the player starts with and them to his inventory
        self.gen_weapons()

    def gen_weapons(self):
        # Add the default Hershey's Kiss to the players inventory
        self.weapons.append(HersheyKiss())

        # Create 9 weapons because one needs to be a hershey's kiss
        for x in range(1, 10):
            # Create random weapon and add it to inventory
            weapon_id = Weapons(random.randint(1, 3))

            if weapon_id is Weapons.SOUR_STRAW:
                self.weapons.append(SourStraw())
            elif weapon_id is Weapons.CHOCOLATE_BAR:
                self.weapons.append(ChocolateBar())
            elif weapon_id is Weapons.NERD_BOMB:
                self.weapons.append(NerdBomb())

    def attack(self, name_of_attack):
        # Make the string upper case so case isn't an issue
        name_of_attack = name_of_attack.lower()

        # Find the weapon that attacked, handle it properly
        for x in self.weapons:
            # If the name of the attack matches a weapon in our inventory, use that weapon
            if x.name() is name_of_attack:
                x.use_weapon()

                damage_dealt = self.attack_value * x.attack_modifier

                # If that weapon has no more uses, get rid of it
                if x.uses is 0:
                    self.weapons.remove(x)

                return damage_dealt
