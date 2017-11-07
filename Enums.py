"""
Some nice Enums for the game, for speed
"""

from enum import Enum


class Monsters(Enum):
    PERSON = 0
    ZOMBIE = 1
    VAMPIRE = 2
    GHOUL = 3
    WEREWOLF = 4


class Weapons(Enum):
    HERSHEY_KISS = 0
    SOUR_STRAW = 1
    CHOCOLATE_BAR = 2
    NERD_BOMB = 3
