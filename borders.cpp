//
// Created by awesome on 06.12.20.
//

#include "borders.h"
#include "vector"


std::vector<Coord> get_island(int x_pos, int y_pos, int radius) {
    std::vector<Coord> island;
    for (int y = -radius; y <= radius; y++)
        for (int x = -radius; x <= radius; x++)
            if (x * x + y * y <= radius * radius)
                island.emplace_back(x + x_pos, y + y_pos);

    return island;
}
