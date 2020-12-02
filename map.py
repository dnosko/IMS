import os
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib import colors as c
import matplotlib as m
from celluloid import Camera
from matplotlib.animation import FuncAnimation


class Map:

    def __init__(self, max_rows, max_columns, data):
        """Class constructor."""
        self.data = data

        data = data[0] #get first 2D matrix

        x = np.linspace(0, max_rows, data.shape[1])
        y = np.linspace(0, max_columns, data.shape[0]) 
        

        self.xx, self.yy = np.meshgrid(x, y)
        

    def add_oil(self, data):
        """ Creates oil mesh. 
            Takes 2D matrix.
                - 0  : white 
                - 7.9 : black
                - < 0 : green
        """

        cm = plt.get_cmap('binary')
        cm.set_under('green')

        return plt.pcolormesh(self.xx, self.yy, data, cmap=cm, vmin=0, vmax=7.9)


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
            output_path = os.path.join(save + '/map.png')
            plt.savefig(output_path, dpi=800)

        if show:
            plt.show()

        if animation:
            print('Generating animation...')
            fig = plt.figure()
            animation = FuncAnimation(fig=fig, func=self.animate,
                                      frames=animation, interval=200, repeat=True, blit=False)

            animation.save('simulation.gif', writer='imagemagick')
            print('Done')

    def animate(self, i):
        """ Creates animation from array of data """

        plt.clf()

        self.add_oil(self.data[i])

        return plt


if __name__ == "__main__":
    Map = Map(132.56575702690475, 35.19266414615366, 139.6409525751002, 40.84789071506689)
    Map.draw_map()

    # example data
    lon = np.arange(135., 138., 0.1)
    lat = np.repeat(37., 30)

    lon = np.reshape(lon, (-1, 10))
    lat = np.reshape(lat, (-1, 10))

    Map.set_data(lon, lat, data)
    Map.add_oil(lon[0], lat[0], data)

    Map.show_map(animation=True)
