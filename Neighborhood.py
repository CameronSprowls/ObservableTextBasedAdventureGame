from Home import Home
from Observer import Observer


class Neighborhood(Observer):

    monsters_left = 0

    def __init__(self, grid_width, grid_height):
        """
        Creates a neighborhood and populates it with homes in a 2d matrix
        :param grid_width: length of the neighborhood
        :param grid_height: height of the neighborhood
        """
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.homes = [[None for x in range(grid_height)] for y in range(grid_height)]

        for x in range(grid_width):
            for y in range(grid_height):
                self.homes[x][y] = Home(x, y, self)
                self.monsters_left += len(self.homes[x][y].get_monsters())

    def home(self, x, y):
        return self.homes[x][y]

    def update(self, *args, **kwargs):
        """
        When a monster is defeated in a house, let the neighborhood know so we can better
        keep track of how many monsters are left to slay.
        :param args: The number of monsters defeated this turn
        """
        self.monsters_left -= args[0]
