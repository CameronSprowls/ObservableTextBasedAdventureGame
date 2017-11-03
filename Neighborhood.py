from Home import Home

class Neighborhood:

    def __init__(self, grid_width, grid_height):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.home = [[Home() for x in range(grid_width)] for y in range(grid_height)]
