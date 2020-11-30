import numpy as np
import copy

class Automata:

    max_concentration = 10 #max number of oil particles
    
    def __init__(self,x,y):
        """ Inits grid of cellular automata to x,y shape """
        self.grid = np.zeros(shape=(x,y))
        self.rows = x
        self.columns = y

    
    def init_oil(self,coordinates):
        """ Inits oil spill. Takes list of x1,y1,x2,y2 coordinates """
        x1,y1,x2,y2 = coordinates
        
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                self.grid[x,y] = self.max_concentration

    
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

        print(self.grid)


    def get_neighbors(self,coordinates):
        """ Gets neighbors based on von neumann neighborhood """
        row, column = coordinates

        neighbors = []
        neighbors.append([row-1, column]) #top
        neighbors.append([row, column-1]) #left
        neighbors.append([row, column+1]) #right
        neighbors.append([row+1, column]) # bottom
        
        return neighbors


    def nextGeneration(self):
        """ Creates new generation based on rules """
        newgen = copy.deepcopy(self.grid)
        for x in range(self.rows):
            for y in range(self.columns):
                newgen[x,y] = self.rules(self.get_neighbors([x,y]))
        
        self.grid = newgen

    
    def rules(self, neighborhood):
        
        sum = 0
        for x,y in neighborhood:
            # side neighbors
            if x == -1 or x > self.rows-1 or y == -1 or y > self.columns-1:
                continue
        #just some test rules for now
            if self.grid[x,y] == 10:
                sum = sum + 1
        
        if sum > 2:
            return 10
        if sum == 1:
            return 5
        else:
            return 0
    


if __name__ == "__main__":
    ca = Automata(5,5)
    ca.init_oil([1,1,3,3])
    ca.print_grid()
    for i in range(5):
        ca.nextGeneration()
        ca.print_grid()
