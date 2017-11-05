"""
Main game class
"""

from Neighborhood import Neighborhood
from Player import Player
from Observer import Observer
from Enums import *


class Game(Observer):

    neighborhood = []
    player = []

    has_won = False
    is_dead = False

    # Board size out here so we can change it whenever we want
    board_x_size = 3
    board_y_size = 3

    def main(self):
        """
        Main body of the program. It's the controller that handles everything and calls
        the appropriate method to handle all of the actions the player can take.
        """
        self.neighborhood = Neighborhood(self.board_x_size, self.board_y_size)
        self.player = Player()

        self.player.in_home = self.neighborhood.homes[0][0]

        self.show_start_description()

        while not self.has_won or not self.is_dead:
            print("You see: ")
            self.show_monsters_in_house()
            self.do_action(self.get_action())
            # Continue the game

    @staticmethod
    def show_start_description():
        """
        Literally just shows the starting message for the game.
        Keeps it clean because the message will be huge
        """
        print("You started the game, congrats.")

    def do_action(self, action):
        """
        Finds the action performed by the player, calls the appropriate method afterwards
        :param action: Action that the player performed, finds the correct function to
                        that corresponds to that action
        """
        if action.lower() == "east" or action.lower() == 'e':
            # Move the player's house one to the east
            self.player.in_home = self.neighborhood.home(self.player.in_home.get_x_pos() + 1,
                                                         self.player.in_home.get_y_pos())
        elif action.lower() == "west" or action.lower() == 'w':
            # Move the player's position one to the west
            self.player.in_home = self.neighborhood.home(self.player.in_home.get_x_pos() - 1,
                                                         self.player.in_home.get_y_pos())
        elif action.lower() == "north" or action.lower() == 'n':
            # Move the player's position one to the north
            self.player.in_home = self.neighborhood.home(self.player.in_home.get_x_pos(),
                                                         self.player.in_home.get_y_pos() - 1)
        elif action.lower() == "south" or action.lower() == 's':
            # Move the player's position one to the south
            self.player.in_home = self.neighborhood.home(self.player.in_home.get_x_pos(),
                                                         self.player.in_home.get_y_pos() + 1)
        elif action.lower() == "attack":
            self.attack()
        elif action.lower() == "inventory":
            self.open_inventory()
        else:
            print("I don't know what", action, "means.")

    def attack(self):
        print("Attack with what?")
        self.open_inventory()
        weapon = input("").lower()

        # Need error checking

        for x in self.player.inventory:
            if x.name.lower() == weapon:
                weapon = x
            elif x.name.lower() == weapon:
                weapon = x
            elif x.name.lower() == weapon:
                weapon = x
            elif x.name.lower() == weapon:
                weapon = x

        damage = self.player.attack(weapon.name)

        # Attack all monsters in the house, monsters should calculate weaknesses and resistances
        for monster in self.player.in_home.get_monsters():
            monster.is_attacked(damage, weapon.get_type())

    def open_inventory(self):
        """
        Shows all of the items in the player's inventory
        """
        hk = 0
        ss = 0
        cb = 0
        nb = 0

        for x in self.player.inventory:
            if x.get_type() is Weapons.HERSHEY_KISS:
                hk += x.uses
            elif x.get_type() is Weapons.SOUR_STRAW:
                ss += x.uses
            elif x.get_type() is Weapons.CHOCOLATE_BAR:
                cb += x.uses
            elif x.get_type() is Weapons.NERD_BOMB:
                nb += x.uses

        if hk > 0:
            print("--Hershey's Kiss (x{uses})".format(uses=hk))
        if ss > 0:
            print("--Sour Straw (x{uses})".format(uses=ss))
        if cb > 0:
            print("--Chocolate Bars (x{uses})".format(uses=cb))
        if nb > 0:
            print("--Nerd Bombs (x{uses})".format(uses=nb))

    def get_action(self):
        """
        Gets the action of the player so the game can progress
        """
        print("What will you do?")
        print("Actions: ")
        self.get_directions()
        self.get_actions()
        player_action = input()
        return player_action

    def get_actions(self):
        """
        Shows all of the actions available that aren't move actions
        """
        if len(self.player.inventory) > 1:
            print("Inventory")
        if len(self.player.in_home.get_monsters()) > 1:
            print("Attack")

    def get_directions(self):
        if self.player.in_home.get_y_pos() - 1 >= 0:
            print("North")
        if self.player.in_home.get_y_pos() + 1 < self.board_y_size:
            print("South")
        if self.player.in_home.get_x_pos() + 1 < self.board_x_size:
            print("East")
        if self.player.in_home.get_x_pos() - 1 >= 0:
            print("West")

    def show_monsters_in_house(self):
        """
        Iterates through all of the monsters in the house and shows how many of
        each monster there are left. Doesn't print if the house is empty
        """
        person = 0
        zombies = 0
        vampires = 0
        ghouls = 0
        werewolves = 0

        for x in self.player.in_home.get_monsters():
            if x.get_type() is Monsters.PERSON:
                person += 1
            elif x.get_type() is Monsters.ZOMBIE:
                zombies += 1
            elif x.get_type() is Monsters.VAMPIRE:
                vampires += 1
            elif x.get_type() is Monsters.GHOUL:
                ghouls += 1
            elif x.get_type() is Monsters.WEREWOLF:
                werewolves += 1

        if person > 0:
            if person > 1:
                print("{person} persons".format(person=person))
            else:
                print("{person} person".format(person=person))
        if zombies > 0:
            if zombies > 1:
                print("{zombies} zombies".format(zombies=zombies))
            else:
                print("{zombies} zombie".format(zombies=zombies))
        if vampires > 0:
            if vampires > 1:
                print("{vampires} vampires".format(vampires=vampires))
            else:
                print("{vampires} vampire".format(vampires=vampires))
        if ghouls > 0:
            if ghouls > 1:
                print("{ghouls} ghouls".format(ghouls=ghouls))
            else:
                print("{ghouls} ghoul".format(ghouls=ghouls))
        if werewolves > 0:
            if werewolves > 1:
                print("{werewolves} werewolves".format(werewolves=werewolves))
            else:
                print("{werewolves} werewolf".format(werewolves=werewolves))

    def update(self, *args, **kwargs):
        # Update house population? What the hell?
        pass


if __name__ == "__main__":
    game = Game()
    game.main()
