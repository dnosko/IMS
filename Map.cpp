//
// Created by dasa on 5. 12. 2020.
//

#include "Map.h"
#include <utility>
using namespace std;

Map::Map() {

}


void Map::show_map() {
    char map_grid[height][width];

    for(int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++){
            map_grid[i][j] = 'X';
            std::cout << " " << map_grid[i][j];
        }
        std::cout << '\n';
    }
}

