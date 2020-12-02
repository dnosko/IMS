import numpy as np
import copy
from map import Map

class Automata:

    max_mass = 7.9  #max kg mass of oil
    #constants
    m = 0.098  #spreading in the four adjacent cells
    d = 0.0176  #spreading constant for diagonal cells
    
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
                self.grid[x,y] = self.max_mass

        return self.grid

    
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


    def get_neighbors(self,coordinates):
        """ Gets neighbors based on von neumann neighborhood """
        row, column = coordinates

        neighbors = []
        neighbors.append([row-1,column-1]) #top left
        neighbors.append([row-1, column]) #top
        neighbors.append([row-1,column+1]) #top right
        neighbors.append([row, column-1]) #left
        neighbors.append([row, column+1]) #right
        neighbors.append([row+1,column-1]) #bottom left
        neighbors.append([row+1, column]) # bottom
        neighbors.append([row+1,column+1]) #bottom rught

        return neighbors


    def next_generation(self):
        """ Creates new generation based on rules """
        newgen = copy.deepcopy(self.grid)
        for x in range(self.rows):
            for y in range(self.columns):
                newgen[x,y] = self.rules(self.get_neighbors([x,y]), self.grid[x,y])
        
        self.grid = newgen

    
    def rules(self, neighborhood, actual_cell):
        
        for x,y in neighborhood:
            # side neighbors
            if x == -1 or x > self.rows-1 or y == -1 or y > self.columns-1:
                continue

        
        return new_mass
        

    def swap_rows(self):

        return self.grid[::-1]


    def make_animation(self,data):
        #draw animation

        #reshape to 3D matrix
        data=np.reshape(data,(-1,10,10)) 
        #TODO swap rows
    
        map = Map(132.56575702690475, 35.19266414615366, 139.6409525751002, 40.84789071506689)
        map.draw_map()
        # example data
        lon = np.arange(135.,137., 0.04)
        lat = np.repeat(37., 50)

        lon = np.reshape(lon,(-1,10))
        lat = np.reshape(lat,(-1,10))

        map.set_data(lon,lat,data)
        #Map.add_oil(lon[0],lat[0],data)
        
        
        map.show_map(show=False,animation=5) 


if __name__ == "__main__":
    ca = Automata(10,10)
    data = ca.init_oil([1,1,4,4])
    #ca.print_grid()
    
    
    for i in range(5):
        ca.next_generation()
        data = np.append(data,ca.swap_rows())
    
    ca.make_animation(data)
    
