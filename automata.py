import numpy as np
import copy
from map import Map
import timeit


class Automata:
    """ neighboorhood order
        NW N WE    4 0 5
        W  X E   = 1 X 2
        SW S SE    6 3 7
    """

    max_mass = 7.9  # max kg mass of oil
    water = 0.0

    # constants
    m = 0.098  # spreading in the four adjacent cells
    d = 0.0176  # spreading constant for diagonal cells
    wind_dict = {"NW": None, "N": ([1, 2, 3], [6, 7]), "NE": None, "W": ([0, 2, 3], [5, 7]),
                 "E": ([0, 1, 3], [4, 6]), "SW": None, "S": ([0, 1, 2], [4, 5]), "SE": None,
                 "NOWIND": ([0, 1, 2, 3], [4, 5, 6, 7])}


    def __init__(self, x, y):
        """ Inits grid of cellular automata to x,y shape """
        self.grid = np.zeros(shape=(x, y))
        self.rows = x
        self.columns = y

    def init_oil(self, coordinates):
        """ Inits oil spill. Takes list of x1,y1,x2,y2 coordinates """
        x1, y1, x2, y2 = coordinates

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self.grid[x, y] = self.max_mass

        return self.grid

    def init_borders(self, x, y):
        self.grid[x][y] = -1.0

    def print_grid(self):
        """neighbors = self.get_neighbors([4,4])

        for x,y in neighbors:
            if x == -1 or y == -1:
                continue
            # side neighbors
            try:
                self.grid[x,y] = 1
            except IndexError:
                continue """
        print(self.grid[::-1])

    def get_neighbors(self, coordinates):
        """ Gets neighbors based on von neumann neighborhood """
        row, column = coordinates

        neighbors = []
        neighbors.append([row - 1, column])  # top
        neighbors.append([row, column - 1])  # left
        neighbors.append([row, column + 1])  # right
        neighbors.append([row + 1, column])  # bottom
        neighbors.append([row - 1, column - 1])  # top left
        neighbors.append([row - 1, column + 1])  # top right
        neighbors.append([row + 1, column - 1])  # bottom left
        neighbors.append([row + 1, column + 1])  # bottom rught

        return neighbors

    def next_generation(self, direction='NOWIND'):
        """ Creates new generation based on wind direction. 
            Direction must be string from this list: NW,W,NE,W,E,SW,S,SE,NOWIND.
            Implicitly set to NOWIND.
        """

        self.wind = direction

        newgen = copy.deepcopy(self.grid)
        for x in range(self.rows):
            for y in range(self.columns):
                newgen[x, y] = self.__rules(self.get_neighbors([x, y]), self.grid[x, y])

        self.grid = newgen

    def __rules(self, neighborhood, actual_cell):

        new_mass = self.__wind(neighborhood, actual_cell)
        if new_mass > self.max_mass:
            new_mass = self.max_mass

        return new_mass

    def __wind(self, neighborhood, actual_cell):
        """ Returns new value of cell, when wind is taken into consideration. 
        """

        adj_cells = 0
        diag_cells = 0

        adj_list = [neighborhood[x] for x in self.wind_dict[self.wind][0]]
        dig_list = [neighborhood[x] for x in self.wind_dict[self.wind][1]]

        # adjacent cells
        for x, y in adj_list:
            # side neighbors
            if x == -1 or x > self.rows - 1 or y == -1 or y > self.columns - 1:
                adj_cells = - actual_cell
            else:
                adj_cells += (self.grid[x, y] - actual_cell)

        # diagonal cells
        for x, y in dig_list:
            if x == -1 or x > self.rows - 1 or y == -1 or y > self.columns - 1:
                diag_cells = - actual_cell
            else:
                diag_cells = (self.grid[x, y] - actual_cell)

        return actual_cell + self.m * adj_cells + self.d * diag_cells

    def swap_rows(self):

        return self.grid[::-1]

    def make_animation(self, data, N):
        """ Makes animation from data with N frames. """

        # reshape to 3D matrix
        data = np.reshape(data, (-1, self.rows, self.columns))

        map = Map(self.rows,self.columns, data)
        
        map.show_map(show=False,animation=N)


    def get_N_generations(self, N, direction):
        """ Makes N generations of CA. """
        data = self.grid
        for i in range(N):
            self.next_generation(direction)
            data = np.append(data,self.grid)

        return data


def run_20(ca, data):
    for i in range(2):
        ca.next_generation()
        data = np.append(data, ca.swap_rows())


if __name__ == "__main__":
    # actual value 120,120 = 600*600 km
    # tanker position = 133 52' East,Latitude 37 10' North
    # 5000–6500 m3  of oil spill

    ca = Automata(200, 200)
    data = ca.init_oil([1, 1, 50, 50])
    #ca.print_grid()
    data = ca.get_N_generations(2, 'S')
    ca.make_animation(data,2)
    
