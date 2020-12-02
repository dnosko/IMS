import timeit
import numpy as np

import borders
from automata import Automata


def run_20(ca, data):
    for i in range(5):
        ca.next_generation()
        data = np.append(data, ca.swap_rows())


if __name__ == "__main__":
    b = borders.get_ca_borders('Japan')
    width = b['x'].max() + 1
    height = b['y'].max() + 1

    CA = Automata(width, height)
    CA.init_borders(b['x'], b['y'])

    x, y = borders.point_to_cell(140, 40)

    data = CA.init_oil([1, 1, 4, 4])
    # CA.print_grid()
    data = CA.swap_rows()

    run_20(CA, data)

