import os
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib import colors as c
import matplotlib as m
from celluloid import Camera
from matplotlib.animation import FuncAnimation


class Map:


    lon = []
    lat = []
    data = []


    def __init__(self,llon,llat,rlon,rlat):
        """Class constructor. llon,llat - down left corner of map, 
           rlon,rlat - upper right corner of map"""

        self.llon = llon
        self.llat = llat
        self.rlon = rlon
        self.rlat = rlat

    
    def set_data(self,lon,lat,data):
        """ Sets data, lon and lat attributes """
        self.data = data
        self.lon = lon
        self.lat = lat


    def draw_map(self, paralles=None, meridians=None):
        """ Draws a map from coordinates given in constructor. Can be drawn with or without 
            parallels and meridians"""

        self.map = Basemap(self.llon, self.llat, self.rlon, self.rlat,
        resolution='h')

        self.map.fillcontinents(color='green', lake_color='aqua')
        self.map.drawcoastlines()

        if paralles is not None:
            #paralels example np.arange(0.,141.,0.5)
            self.map.drawparallels(paralles, labels=[False,True,True,False])

        if meridians is not None:
            #meridians example np.arange(0.,351.,0.5)
            self.map.drawmeridians(meridians, labels=[True,False,False,True])

    
    def add_oil(self,coord_lon, coord_lat,data):
        """ Creates oil mesh. 
            Coord_lon is array of longtitude coordinates.
            Coord_lat is array of lattitude coordinates.
            Data is matrix with values at given squares
                - 0  : white 
                - 10 : black
                - else shades of greys
            Data values must be vertically inverted. 
            Colormesh prints only n-1 cols and rows.
        """
        
        
        x = np.linspace(coord_lon[0],coord_lon[-1], data.shape[1])
        y = np.linspace(coord_lat[0], coord_lat[0]+1, data.shape[0])

        xx, yy = np.meshgrid(x, y)
        
        cm = plt.get_cmap('binary')
        cm.set_under('white')

        return self.map.pcolormesh(xx, yy, data,cmap=cm,vmin=0, vmax=10)


    def show_map(self, show=True, save=None, animation=False):
        """ Plots map.
            Shows figure if show=True.
            Saves map to given location in argument save.
            If animation True, creates animation.
        """
        if save:
            try:
                os.mkdir(save)
            except FileExistsError:
                pass
            output_path = os.path.join(save+'/map.png')
            plt.savefig(output_path,dpi=800)  

        if show:
            plt.show()

        if animation:
            print('Generating animation...')
            fig = plt.figure()
            animation = FuncAnimation(fig = fig, func = self.animate, 
                           frames=animation, interval=200,repeat=True, blit=False)

            animation.save('simulation.gif',writer='imagemagick',dpi=600)
            print('Done') 

    
    def animate(self,i):
        """ Creates animation from array of data """
        
        #if i == 1:
        #    print('Generating animation...')

        plt.clf()
        self.draw_map()
        
        self.add_oil(self.lon[i], self.lat[i],self.data[i]) 

        return plt

if __name__ == "__main__":
    Map = Map(132.56575702690475, 35.19266414615366, 139.6409525751002, 40.84789071506689)
    Map.draw_map()
    
    # example data
    lon = np.arange(135.,138., 0.1)
    lat = np.repeat(37., 30)

    lon = np.reshape(lon,(-1,10))
    lat = np.reshape(lat,(-1,10))

    Map.set_data(lon,lat,data)
    Map.add_oil(lon[0],lat[0],data)
    
    
    Map.show_map(animation=True)