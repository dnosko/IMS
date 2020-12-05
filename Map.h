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
    Map();
    void show_map();
    void add_oil(vector<Coord> oil); // adds oil to map

private:
    void init_map();
    int height = 70;
    int width = 70;
    vector<vector<char> > map_grid;
};


#endif //IMS_C___MAP_H
