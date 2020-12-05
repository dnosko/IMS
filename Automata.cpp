//
// Created by dasa on 5. 12. 2020.
//

#include <iostream>
#include "Automata.h"

Automata::Automata(int rows, int columns, int max_mass, WindDirection wind) {
    rows = rows;
    cols = columns;
    max_oil = max_mass;
    wind_direction = wind;
}

vector<pair<Coord, int>> Automata::init_oil(Coord c1, Coord c2) {

    pair<Coord ,int> cell;
    Coord coords;

    for(int x = c1.first; x < c2.first; x++){
        for(int y = c1.second; y < c2.second; y++){
            coords = make_pair(x,y);
            cell = make_pair(coords,max_oil);
            oil_grid.push_back(cell);
        }
    }

    return oil_grid;
}

Automata::Automata() {

}

vector<Coord> Automata::get_neighbors(Coord cell) {
    int x = cell.first;
    int y = cell.second;

    vector<Coord> neighbors;

    neighbors.push_back(make_pair(x-1,y)); // top
    neighbors.push_back(make_pair(x,y-1)); // left
    neighbors.push_back(make_pair(x,y+1)); // right
    neighbors.push_back(make_pair(x+1,y)); // bottom
    neighbors.push_back(make_pair(x-1,y-1)); // top left
    neighbors.push_back(make_pair(x-1,y+1)); // top right
    neighbors.push_back(make_pair(x+1,y-1)); // bottom left
    neighbors.push_back(make_pair(x+1,y+1)); // bottom right

    return neighbors;
}

void Automata::next_generation() {

    vector<pair<Coord ,int>> tmp_grid = oil_grid;

   
}

int Automata::rules(vector<Coord> neighborhood, int actual_cell_mass) {
    int new_mass = wind(neighborhood, actual_cell_mass);
    if (new_mass > max_oil)
        new_mass = max_oil;
    return new_mass;
}

int Automata::wind(vector<Coord> neighborhood, int actual_cell_mass) {

    int adj_cells, diag_cells;
    int x,y;
    int position;

    for(int i = 0; i < 4; i++) {
        x = neighborhood.at(i).first;
        y = neighborhood.at(i).second;
        if (x == -1 || x > rows || y == -1 || y > cols) {
            adj_cells = 0;
        }
        else {
            adj_cells  += 1;
        }
    }



    return 0;
}
