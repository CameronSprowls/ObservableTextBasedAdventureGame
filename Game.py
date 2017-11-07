"""
Main game class
"""

from Neighborhood import Neighborhood
from Observer import Observer
from Player import Player
from Enums import *
from random import randint


class Game(Observer):

    # Instance variables for the sole use of this class
    padding = "    "
    invalid_directions = ["north", "south", "east", "west"]
    neighborhood = []
    player = []
    has_won = False
    is_dead = False
    monsters_left = 0

    # Board size out here so we can change it whenever we want
    board_x_size = randint(2, 5)
    board_y_size = randint(2, 5)

    def main(self):
        """
        Main body of the program. It's the controller that handles everything and calls
        the appropriate method to handle all of the actions the player can take.
        """
        # Create board and player
        self.neighborhood = Neighborhood(self.board_y_size, self.board_x_size)
        self.player = Player()
        self.player.in_home = self.neighborhood.homes[0][0]

        for x in self.neighborhood.homes:
            for y in x:
                self.monsters_left += len(y.get_monsters())
                y.sub(self)

        # Start the game and the game-loop
        self.show_start_description()
        while not self.has_won and not self.is_dead:
            print("\n\nYou see: ")
            self.show_monsters_in_house()
            print("Your health is: ", self.player.health)
            print("There are {monster_num} monsters left in the neighborhood"
                  .format(monster_num=self.monsters_left))
            self.do_action(self.get_action())

            # Check to see if the player has died, if they have, display the died message
            if self.is_dead:
                self.end_game_through_death()

            # See if all of the monsters are dead
            if self.monsters_left < 1:
                self.has_won = True

            # Check to see if the player has won, if they have, display the victory message
            if self.has_won:
                self.end_game_through_victory()

    @staticmethod
    def end_game_through_victory():
        """
        Displays a message that the player has won
        """
        print("After the trials and tribulations placed before you, you slowly slayed\n"
              "the monsters one by one, converting them back to normal along the way.\n"
              "It seems as if everyone in the neighborhood has returned to normal,\n"
              "your work here is done. That is... until next Halloween. *dramatic music*")

    @staticmethod
    def end_game_through_death():
        """
        Displays a message that the player has died
        """
        print("It appears you have died. Game over.")

    @staticmethod
    def show_start_description():
        """
        Literally just shows the starting message for the game.
        Keeps it clean because the message will be huge
        """
        print("It seemed like a normal Halloween Eve. You bought a lot candy, ate a lot\n"
              "of candy, and went to bed early. You had a lot of trick-or-treating to do\n"
              "the next day.\n\n"
              "Unfortunately, when you woke up you discovered that the world was not how\n"
              "you left it. Batches of bad candy had transformed your friends and neighbors\n"
              "into all sorts of crazy monsters. Somehow you missed the tainted candy; it\n"
              "is therefore up to you to save your neighborhood and turn everyone back to normal.\n\n"
              "You prep your plan, grab your trustee weapons, and head to your first house...")

    def do_action(self, action):
        """
        Finds the action performed by the player, calls the appropriate method afterwards
        :param action: Action that the player performed, finds the correct function to
                        that corresponds to that action
        """
        if action.lower() in self.invalid_directions:
            print("{action} isn't a valid direction right now.".format(action=action))
            return

        if action.lower() == "east":
            # Move the player's house one to the east
            self.player.in_home = self.neighborhood.home(self.player.in_home.get_x_pos() + 1,
                                                         self.player.in_home.get_y_pos())
            print("You traveled east.")
        elif action.lower() == "west":
            # Move the player's position one to the west
            self.player.in_home = self.neighborhood.home(self.player.in_home.get_x_pos() - 1,
                                                         self.player.in_home.get_y_pos())
            print("You traveled west.")
        elif action.lower() == "north":
            # Move the player's position one to the north
            self.player.in_home = self.neighborhood.home(self.player.in_home.get_x_pos(),
                                                         self.player.in_home.get_y_pos() - 1)
            print("You traveled north.")
        elif action.lower() == "south":
            # Move the player's position one to the south
            self.player.in_home = self.neighborhood.home(self.player.in_home.get_x_pos(),
                                                         self.player.in_home.get_y_pos() + 1)
            print("You traveled south.")
        elif action.lower() == "attack":
            self.attack()
        elif action.lower() == "inventory":
            self.open_inventory()
        elif action.lower() == "map":
            self.open_map()
        else:
            print("I don't know what", action, "means.")

    def open_map(self):
        """
        Shows a nice representation of the map for the player
        """
        for y in range(self.board_y_size):
            for x in range(self.board_x_size):
                print("X ", end='')
            print("")
        print()

    def attack(self):
        """
        Prompts the user to provide a valid weapon of which to attack.
        Calls the valid attack function if the weapon is valid.
        Will continue to ask until a valid input is provided, or 'back'
        is entered.
        :return: nothing only when the 'back' button is pressed
        """
        print("Attack with what?")
        self.open_inventory()
        weapon = input("").lower()

        valid_weapon = False
        num_item = 0

        # find the weapon the player wants to attack with, don't allow them to use invalid weapons or weapons
        # that have no more uses
        while not valid_weapon:
            if weapon == "hk" or weapon == "hershey's kisses" or weapon == "hershey's kiss":
                for x in self.player.inventory:
                    if x.get_type() is Weapons.HERSHEY_KISS:
                        num_item += 1
                        weapon = Weapons.HERSHEY_KISS
                        valid_weapon = True
            elif weapon == "ss" or weapon == "sour straws" or weapon == "sour straw":
                for x in self.player.inventory:
                    if x.get_type() is Weapons.SOUR_STRAW:
                        num_item += 1
                        weapon = Weapons.SOUR_STRAW
                        valid_weapon = True
            elif weapon == "cb" or weapon == "chocolate bars" or weapon == "chocolate bar":
                for x in self.player.inventory:
                    if x.get_type() is Weapons.CHOCOLATE_BAR:
                        num_item += 1
                        weapon = Weapons.CHOCOLATE_BAR
                        valid_weapon = True
            elif weapon == "nb" or weapon == "nerd bombs" or weapon == "nerd bomb":
                for x in self.player.inventory:
                    if x.get_type() is Weapons.NERD_BOMB:
                        num_item += 1
                        weapon = Weapons.NERD_BOMB
                        valid_weapon = True
            elif weapon == "back":
                print("Attack aborted.")
                return
            else:
                print("{weapon} is not a weapon you posses".format(weapon=weapon))
                weapon = input("Attack with what? (You can cancel this attack with 'back')\n").lower()

            if num_item == 0:
                print("You don't have any {item}".format(item=weapon))
                weapon = input("Attack with what? (You can cancel this attack with 'back')\n").lower()

        # Finds the weapon that the player would attack with
        for x in self.player.inventory:
            if x.get_type is weapon:
                weapon = x
            elif x.get_type == x:
                weapon = x
            elif x.get_type is weapon:
                weapon = x
            elif x.get_type is weapon:
                weapon = x

        damage = self.player.attack(weapon)

        # This is here because I'm mean and let the monsters attack first
        if self.player.get_is_dead():
            self.is_dead = True
            print("You tried to attack, but the monsters got to you first...")
            return

        # Attack all monsters in the house, monsters should calculate weaknesses and resistances
        # Make a copy of the list so we can attack them separately
        temp = self.player.in_home.get_monsters()[:]
        for monster in temp:
            monster.is_attacked(damage, weapon)

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
        self.get_directions()
        self.get_actions()
        player_action = input()
        return player_action

    def get_actions(self):
        """
        Shows all of the actions available that aren't move actions
        """
        if len(self.player.inventory) > 1:
            print(self.padding, "Inventory")
        if len(self.player.in_home.get_monsters()) > 1:
            print(self.padding, "Attack")

    def get_directions(self):
        """
        Prints all of the valid movable directions to the screen, also marks all
        of the invalid directions for future use.
        """
        self.invalid_directions = ["north", "south", "east", "west"]
        if self.player.in_home.get_y_pos() - 1 >= 0:
            print(self.padding, "North")
            self.invalid_directions.remove("north")
        if self.player.in_home.get_y_pos() + 1 < self.board_y_size:
            print(self.padding, "South")
            self.invalid_directions.remove("south")
        if self.player.in_home.get_x_pos() + 1 < self.board_x_size:
            print(self.padding, "East")
            self.invalid_directions.remove("east")
        if self.player.in_home.get_x_pos() - 1 >= 0:
            print(self.padding, "West")
            self.invalid_directions.remove("west")

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
                print(self.padding, "{person} persons".format(person=person))
            else:
                print(self.padding, "{person} person".format(person=person))
        if zombies > 0:
            if zombies > 1:
                print(self.padding, "{zombies} zombies".format(zombies=zombies))
            else:
                print(self.padding, "{zombies} zombie".format(zombies=zombies))
        if vampires > 0:
            if vampires > 1:
                print(self.padding, "{vampires} vampires".format(vampires=vampires))
            else:
                print(self.padding, "{vampires} vampire".format(vampires=vampires))
        if ghouls > 0:
            if ghouls > 1:
                print(self.padding, "{ghouls} ghouls".format(ghouls=ghouls))
            else:
                print(self.padding, "{ghouls} ghoul".format(ghouls=ghouls))
        if werewolves > 0:
            if werewolves > 1:
                print(self.padding, "{werewolves} werewolves".format(werewolves=werewolves))
            else:
                print(self.padding, "{werewolves} werewolf".format(werewolves=werewolves))

    def update(self, *args, **kwargs):
            # Update number of monsters still in the game
            self.monsters_left -= args[0]


# Start the game
if __name__ == "__main__":
    game = Game()
    game.main()
