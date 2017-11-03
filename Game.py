"""
Main game class
"""

from Neighborhood import Neighborhood
from Player import Player

class Game:

    @staticmethod
    def main():
        neighborhood = Neighborhood(3, 3)
        player = Player()

        while True:
            print(neighborhood, player)

            input("hold")


if __name__ == "__main__":
    Game.main()
