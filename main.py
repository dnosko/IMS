import timeit
import numpy as np

import borders
from automata import Automata


def run_20(ca, data):
    for i in range(20):
        ca.next_generation()
        data = np.append(data, ca.swap_rows())


if __name__ == "__main__":
    b = borders.get_ca_borders('Japan')
    width = b['x'].max() + 1
    height = b['y'].max() + 1

    CA = Automata(width, height, 100)
    CA.init_borders(b['x'].values, b['y'].values)

    x, y = borders.point_to_cell(133.0, 37.0)
    data = CA.init_oil([x, y, x + 3, y + 3])
    data = CA.get_N_generations(5)
    CA.make_animation(data, 5)

    # CA = Automata(100, 100)
    # CA.init_oil([10, 10, 10, 10])
    # # ca.print_grid()
    # data = CA.get_N_generations(5, 'E')
    # print(timeit.timeit(lambda: CA.get_N_generations(5, 'E'), number=4))
    # print('a')
