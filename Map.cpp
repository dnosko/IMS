//
// Created by dasa on 5. 12. 2020.
//

#include "Map.h"
#include <utility>

using namespace std;

Map::Map() {

    for(int i = 0; i < width; i++) {
        vector<char> cell;
        for (int j = 0; j < height; j++){
            //TODO borders pravidlo
            if (i == 0 || i == width-1 || j == 0 || j == height-1) {
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


void Map::show_map() {

    for(int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++){
            std::cout << " " << map_grid[i][j];
        }
        std::cout << '\n';
    }
}

void Map::add_oil(vector<Coord> oil) {
    int size = oil.size();

    for(int i = 0; i < size; i++){
        int x = oil.at(i).first;
        int y = oil.at(i).second;
        map_grid[x][y] = 'X';
    }
}

