import os
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib import colors as c
import matplotlib as m
from celluloid import Camera
from matplotlib.animation import FuncAnimation


class Map:

    def __init__(self, max_rows, max_columns, data,max_mass):
        """Class constructor."""
        self.data = data

        data = data[0]  # get first 2D matrix

        x = np.linspace(0, max_rows, data.shape[1])
        y = np.linspace(0, max_columns, data.shape[0]) 
        

        self.xx, self.yy = np.meshgrid(x, y)
        self.max_mass = max_mass
        

    def add_oil(self, data):
        """ Creates oil mesh. 
            Takes 2D matrix.
                - 0  : white 
                - max_mass : black
                - < 0 : green - borders
        """

        cm = plt.get_cmap('binary')
        cm.set_under('green')

        return plt.pcolormesh(self.xx, self.yy, data, cmap=cm, vmin=0, vmax=self.max_mass)


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
            fig = plt.gca()
            fig.axes.get_xaxis().set_visible(False)
            fig.axes.get_yaxis().set_visible(False)
            self.add_oil(self.data[0])
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
        plt.xticks([])
        plt.yticks([])

        self.add_oil(self.data[i])

        return plt


if __name__ == "__main__":
    Map = Map(10,10,np.array([[[1,2,3],[4,5,6]]]))

    Map.add_oil([[1,2,3],[4,5,6]])

    Map.show_map(animation=False)
