import borders
from automata import Automata

if __name__ == "__main__":
    borders = borders.get_ca_borders('Japan')
    width = borders['x'].max() + 1
    height = borders['y'].max() + 1

    CA = Automata(width, height)
    CA.init_borders(borders['x'], borders['y'])
