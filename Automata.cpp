//
// Created by dasa on 5. 12. 2020.
//

#include <iostream>
#include <cmath>
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

void Automata::get_neighbors(Coord cell) {
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

    neighborhood = neighbors;
}

void Automata::next_generation() {

    vector<pair<Coord ,int>> tmp_grid = oil_grid;


}

int Automata::rules(int actual_cell_mass) {
    int new_mass = wind(actual_cell_mass);
    if (new_mass > max_oil)
        new_mass = max_oil;
    return new_mass;
}

int Automata::wind(int actual_cell_mass) {

    int adj_cells, diag_cells;
    float result;

    adj_cells = cells_sum(0,4,actual_cell_mass);
    diag_cells = cells_sum(4,8,actual_cell_mass);
    result = actual_cell_mass + m * adj_cells + d * m * diag_cells;

    return round(result);
}

int Automata::cells_sum(unsigned from, unsigned to, int actual_cell_mass) {

    int cells_sum = 0;
    int x,y;
    int cell_mass;

    for(unsigned i = from; i < to; i++) {
        x = neighborhood.at(i).first;
        y = neighborhood.at(i).second;
        if (x == -1 || x > rows || y == -1 || y > cols) {
            cells_sum = 0;
        }
        else {
            cell_mass = oil_grid.at(i).second;
            cells_sum  += cell_mass - actual_cell_mass;
        }
    }

    return cells_sum;
}
