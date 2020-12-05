//
// Created by dasa on 5. 12. 2020.
//

#include "Map.h"

using namespace std;


Map::Map() {
    width = 70;
    height = 70;
    init_map();
}

Map::Map(int x, int y) {
    //TODO PRIDAT OBMEDZENIE
    width = x;
    height = y;
    init_map();
}


void Map::show_map() {

    for(int y = 0; y < height; y++) {
        for (int j = 0; j < width; j++){
            std::cout << " " << map_grid[y][j];
        }
        std::cout << '\n';
    }
}

void Map::add_oil(vector<vector<int>> oil, int max_mass) {

    int half_mass = max_mass / 2;

    int x_size = oil.size();
    int y_size = oil.front().size();

    for(int x = 0; x < x_size; x++){
        for (int y = 0; y < y_size; y++) {
        int cell = oil[x][y];
        // oil cant be out of map
        if(x < height && y < width) {
            // oil cant be on borders
            if (map_grid[x][y] != '-') {
                if (cell > half_mass )
                    map_grid[x][y] = 'X';
                else if(cell > 0 && cell <= half_mass )
                    map_grid[x][y] = 'x';
                else
                    map_grid[x][y] = ' ';
            }
        }
    }
    }
}

void Map::init_map() {

    for(int y = 0; y < height; y++) {
        vector<char> cell;
        for (int x = 0; x < width; x++){
            //TODO borders pravidlo
            if (y == 0 || y == height - 1 || x == 0 || x == width - 1) {
                // borders
                cell.push_back('-');
            }
            else {
                // water
                cell.push_back(' ');
            }
        }
        map_grid.push_back(cell);
    }
}



