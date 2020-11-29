import os
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib import colors as c
import matplotlib as m
from celluloid import Camera


class Map:


    def __init__(self,llon,llat,rlon,rlat):
        """Class constructor. llon,llat - down left corner of map, 
           rlon,rlat - upper right corner of map"""

        self.llon = llon
        self.llat = llat
        self.rlon = rlon
        self.rlat = rlat


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

        #10 cierna, 0 biela, kresli sa zdola hore a vykresluje iba n-1 teda jeden riadok a stlpec sa vynechava
        

        x = np.linspace(coord_lon[0],coord_lon[-1], data.shape[1])
        y = np.linspace(coord_lat[0], coord_lat[0]+1, data.shape[0])

        xx, yy = np.meshgrid(x, y)
        
        cm = plt.get_cmap('binary')
        cm.set_under('white')

        return self.map.pcolormesh(xx, yy, data,cmap=cm,vmin=0, vmax=10)


    def show_map(self, show=True, save=None):
        """ Plots map.
            Shows figure if show=True.
            Saves map to given location in argument save """

        if save:
            try:
                os.mkdir(save)
            except FileExistsError:
                pass
            output_path = os.path.join(save+'/map.png')
            plt.savefig(output_path)  

        if show:
            plt.show()

    
    def animate(self,start,frames,data):
        """ Creates animation from starting point = start. Creates N frames. """

        fig = plt.figure()
        
        camera = Camera(fig)
        for i in range(frames):
            self.draw_map()
            #TODO upravit parametre
            lon = np.arange(start+i,start+i+1,0.1)
            lat = np.repeat(37., 10)
            self.add_oil(lon,lat,data) 
            plt.plot()
            camera.snap()

        animation = camera.animate(interval=500)
        animation.save('simulation.gif', writer = 'imagemagick')
        

        




if __name__ == "__main__":
    Map = Map(132.56575702690475, 35.19266414615366, 139.6409525751002, 40.84789071506689)
    Map.draw_map()
    lon = np.arange(135.,136., 0.1)
    lat = np.repeat(37., 10)
    data = np.array([
            [9.21954446, 8.60232527, 8.06225775, 7.61577311, 7.28010989,
            7.07106781, 0.        , 7.07106781, 7.28010989, 7.61577311],
        [8.48528137, 7.81024968, 7.21110255, 6.70820393, 6.32455532,
            6.08276253, 6.        , 6.08276253, 6.32455532, 6.70820393],
        [7.81024968, 7.07106781, 6.40312424, 5.83095189, 5.38516481,
            5.09901951, 5.        , 5.09901951, 5.38516481, 5.83095189],
        [7.21110255, 6.40312424, 5.65685425, 5.38516481, 4.47213595,
            4.12310563, 4.        , 4.12310563, 4.47213595, 5.        ],
        [6.70820393, 5.83095189, 5.        , 4.24264069, 3.60555128,
            3.16227766, 3.        , 3.16227766, 3.60555128, 4.24264069],
        [6.32455532, 5.38516481, 4.47213595, 3.60555128, 2.82842712,
            2.23606798, 2.        , 2.23606798, 2.82842712, 3.60555128],
        [6.08276253, 5.09901951, 4.12310563, 3.16227766, 2.23606798,
            1.41421356, 1.41421356, 1.41421356, 2.23606798, 3.16227766],
        [6.        , 5.        , 4.        , 3.        , 2.        ,
            1.        , 0.        , 1.        , 2.        , 3.        ],
        [6.08276253, 5.09901951, 4.12310563, 3.16227766, 2.23606798,
            1.41421356, 1.        , 1.41421356, 2.23606798, 3.16227766],
        [6.32455532, 5.38516481, 4.47213595, 3.60555128, 2.82842712,
            2.23606798, 2.        , 2.23606798, 2.82842712, 3.60555128]])
    Map.add_oil(lon,lat,data)
    
    Map.animate(135.,3,data)
    #Map.show_map()
