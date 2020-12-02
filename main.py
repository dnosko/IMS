import timeit
import numpy as np

import borders
from automata import Automata


def run_20(ca, data):
    for i in range(20):
        ca.next_generation()
        data = np.append(data, ca.swap_rows())


if __name__ == "__main__":
    borders = borders.get_ca_borders('Japan')
    width = borders['x'].max() + 1
    height = borders['y'].max() + 1

    CA = Automata(width, height)
    CA.init_borders(borders['x'], borders['y'])

    x, y = borders.point_to_cell(140, 40)
    #
    # data = CA.init_oil([1, 1, 4, 4])
    # # CA.print_grid()
    # data = CA.swap_rows()
    #
    # print(timeit.timeit(lambda: run_20(CA, data), number=5))
