from Home import Home


class Neighborhood:

    def __init__(self, grid_width, grid_height):
        """
        Creates a neighborhood and populates it with homes in a 2d matrix
        :param grid_width: length of the neighborhood
        :param grid_height: height of the neighborhood
        """
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.homes = [[0 for x in range(grid_height)] for y in range(grid_height)]

        for x in range(grid_width):
            for y in range(grid_height):
                self.homes[x][y] = Home(x, y)

    def home(self, x, y):
        return self.homes[x][y]
