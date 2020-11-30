import numpy as np

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
        #neighbors = self.get_neighbors([4,4])
        #for x,y in neighbors:
        #    self.grid[x,y] = 1
        print(self.grid)


    def get_neighbors(self,coordinates):
        """ Gets neighbors based on von neumann neighborhood """
        row, column = coordinates

        neighbors = []
        if row != 0:
            neighbors.append([row-1, column]) #top
        if column != 0:
            neighbors.append([row, column-1]) #left
        if column != self.columns-1:
            neighbors.append([row, column+1]) #right
        if row != self.rows-1:
            neighbors.append([row+1, column]) # bottom

        return neighbors


    def nextGeneration(self):
        pass
    


if __name__ == "__main__":
    ca = Automata(5,5)
    ca.init_oil([1,1,3,3])
    ca.print_grid()
