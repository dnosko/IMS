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


    def __init__(self,llon,llat,rlon,rlat):
        """Class constructor. llon,llat - down left corner of map, 
           rlon,rlat - upper right corner of map"""
        self.llon = llon
        self.llat = llat
        self.rlon = rlon
        self.rlat = rlat

    
    def set_data(self,lon,lat):
        """ Sets lon and lat attributes """
        self.lon = lon
        self.lat = lat


    def draw_map(self, paralles=None, meridians=None):
        """ Draws a map from coordinates given in constructor. Can be drawn with or without 
            parallels and meridians"""
        self.map = Basemap(self.llon, self.llat, self.rlon, self.rlat,
        resolution='h',epsg=4301)

        self.map.fillcontinents(color='green', lake_color='aqua')
        self.map.drawcoastlines()

        if paralles is not None:
            #paralels example np.arange(0.,141.,0.5)
            self.map.drawparallels(paralles, labels=[False,True,True,False])

        if meridians is not None:
            #meridians example np.arange(0.,351.,0.5)
            self.map.drawmeridians(meridians, labels=[True,False,False,True])

        return self.map

    
    def add_oil(self,coord_lon, coord_lat):
        """ Creates oil track. 
            Coord_lon is array of longtitude coordinates.
            Coord_lat is array of lattitude coordinates.
        """
        self.map.scatter(coord_lon, coord_lat, marker='.',cmap='Greys',alpha=0.5)


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
            fig = plt.figure()
            animation = FuncAnimation(fig = fig, func = self.animate, 
                           frames=3, interval=500, repeat = True, blit=False)

            animation.save('simulation.gif',writer='imagemagick',dpi=600) 

    
    def animate(self,i):
        """ Creates animation from array of data """
        if i == 1:
            print('Generating animation...')

        plt.clf()
        self.draw_map()
        x, y = self.map(lon[i], lat[i])
    
        self.map.scatter(x, y, marker='.',cmap='Greys',alpha=0.5)

        return plt
        

if __name__ == "__main__":
    Map = Map(132.56575702690475, 35.19266414615366, 139.6409525751002, 40.84789071506689)
    Map.draw_map()
    
    # example data
    lon = np.arange(135.,138., 0.1)
    lat = np.repeat(37., 30)

    lon = np.reshape(lon,(-1,10))
    lat = np.reshape(lat,(-1,10))

    Map.set_data(lon,lat)
    Map.add_oil(lon[0],lat[0])
    
    
    Map.show_map(animation=True)