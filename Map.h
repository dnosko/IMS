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
    int oil_count = 0;

    Map(int x, int y);
    void show_map();
    void show_orientation();
    void add_oil(vector<vector<double>> oil, int max_mass); // adds oil to map

private:
    int width;
    int height;
    vector<vector<char>> map_grid;
    void init_map();
};


#endif //IMS_C___MAP_H
