//
// Created by dasa on 5. 12. 2020.
//
using namespace std;
#include <iostream>
#include <vector>

#ifndef IMS_C___MAP_H
#define IMS_C___MAP_H

using namespace std;
using Coord = pair<int, int>;

class Map {
public:
    Map(int x, int y);
    Map();
    void show_map();
    void add_oil(vector<vector<int>> oil, int max_mass); // adds oil to map

private:
    void init_map();
    int width;
    int height;
    vector<vector<char>> map_grid;
};


#endif //IMS_C___MAP_H
