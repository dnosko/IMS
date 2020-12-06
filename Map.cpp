//
// Created by dasa on 5. 12. 2020.
//

#include "Map.h"

using namespace std;


Map::Map(int x, int y) {

    if ( x < 0 || x > 100 || y < 0  || y > 100){
        cout << "X and Y must be in <0-100> interval.";
        exit(1);
    }
    width = x;
    height = y;
    init_map();
}


void Map::show_map() {

    for(int y = 0; y < height; y++) {
        for (int j = 0; j < width; j++){
            cout << " " << map_grid[y][j];
        }
        cout << '\n';
    }
}

void Map::show_orientation() {

    cout << "\n Map orientation: ";
    cout << "\t " << "N" << "\n";
    cout << "\t               W " << "X" << " E" << "\n";
    cout << "\t                 " << "S" << "\n\n";
}

void Map::add_oil(vector<vector<double>> oil, int max_mass) {

    int half_mass = max_mass / 2;

    int x_size = oil.size();
    int y_size = oil.front().size();

    for(int x = 0; x < x_size; x++){
        for (int y = 0; y < y_size; y++) {
            double cell = oil[x][y];
        // oil cant be out of map
        if(x < height && y < width) {
            // oil cant be on borders
            if (map_grid[x][y] != '-') {
                if (cell > half_mass ) {
                    map_grid[x][y] = 'X'; //lots of oil
                    oil_count++;
                }
                else if(cell > 1 && cell <= half_mass ){
                    map_grid[x][y] = 'x'; //some oil
                    oil_count++;
                }
                else if (cell > -1)
                    map_grid[x][y] = ' '; // water
                else
                    map_grid[x][y] = '~'; // land
            }
        }
    }
    }
}

void Map::init_map() {

    for(int y = 0; y < height; y++) {
        vector<char> cell;
        for (int x = 0; x < width; x++){
            if (y == 0 || y == height -1 || x == 0 || x == width -1) {
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



