//
// Created by dasa on 5. 12. 2020.
//

#include <iostream>
#include <cmath>
#include "Automata.h"

#define SKIP -2

Automata::Automata() {
    rows = 70;
    cols = 70;
    max_oil = 790;
    wind_direction = NoWind;
}

Automata::Automata(int x, int y, int max_mass, WindDirection wind) {
    rows = y;
    cols = x;
    max_oil = max_mass;
    wind_direction = wind;
}

void Automata::init_oil(Coord c1, Coord c2) {

    for (int y = 0; y < rows; y++) {
        vector<int> cell;
        for (int x = 0; x < cols; x++) {
            if (x >= c1.first && x <= c2.first &&
                y >= c1.second && y <= c2.second) {
                cell.push_back(max_oil);
            } else
                cell.push_back(0);
        }
        oil_grid.push_back(cell);
    }
}

void Automata::init_borders(std::vector<Coord> c) {
    for (auto &p : c) {
        oil_grid[p.first][p.second] = -1;
    }
}

vector<Coord> Automata::get_neighbors(Coord cell) {
    /*****************************************
     *     neighboorhood order
     *       NW N WE    4 0 5
     *       W  X E   = 1 X 2
     *       SW S SE    6 3 7
    ******************************************/

    int x = cell.first;
    int y = cell.second;

    vector<Coord> neighbors;
    neighbors.push_back(make_pair(x - 1, y)); // top
    neighbors.push_back(make_pair(x, y - 1)); // left
    neighbors.push_back(make_pair(x, y + 1)); // right
    neighbors.push_back(make_pair(x + 1, y)); // bottom
    neighbors.push_back(make_pair(x - 1, y - 1)); // top left
    neighbors.push_back(make_pair(x - 1, y + 1)); // top right
    neighbors.push_back(make_pair(x + 1, y - 1)); // bottom left
    neighbors.push_back(make_pair(x + 1, y + 1)); // bottom right

    return skip_neighbors(neighbors);
}

vector<Coord> Automata::skip_neighbors(vector<Coord> neighbors) {
    // set values to skip if wind is set
    switch (wind_direction) {
        case North:
            neighbors.at(0).first = SKIP;
            neighbors.at(4).first = SKIP;
            neighbors.at(5).first = SKIP;
            break;
        case West:
            neighbors.at(1).first = SKIP;
            neighbors.at(4).first = SKIP;
            neighbors.at(6).first = SKIP;
            break;
        case East:
            neighbors.at(2).first = SKIP;
            neighbors.at(5).first = SKIP;
            neighbors.at(7).first = SKIP;
            break;
        case South:
            neighbors.at(3).first = SKIP;
            neighbors.at(6).first = SKIP;
            neighbors.at(7).first = SKIP;
            break;
        case NoWind:
            break;
    }

    return neighbors;
}

void Automata::next_generation() {

    vector<vector<int>> tmp_grid = oil_grid;

    for (int i = 0; i < rows - 1; i++) {
        for (int j = 0; j < cols - 1; j++) {
            // if cell is border skip
            if (tmp_grid[i][j] == -1)
                continue;
            // get next gen value of cell
            neighborhood = get_neighbors(make_pair(i, j));
            tmp_grid[i][j] = rules(tmp_grid[i][j]);
        }
    }

    oil_grid = tmp_grid;
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

    adj_cells = cells_sum(0, 4, actual_cell_mass);
    diag_cells = cells_sum(4, 8, actual_cell_mass);
    result = actual_cell_mass + m * adj_cells + d * m * diag_cells;

    return round(result);
}

int Automata::cells_sum(unsigned from, unsigned to, int actual_cell_mass) {

    int cells_sum = 0;
    int x, y;
    int cell_mass;

    for (unsigned i = from; i < to; i++) {
        x = neighborhood.at(i).first;
        // SKIP if wind direction is set
        if (neighborhood.at(i).first == SKIP)
            continue;
        y = neighborhood.at(i).second;
        // out of borders
        if (x == -1 || x > rows || y == -1 || y > cols) {
            cells_sum = 0;
        } else { // get next gen cell value
            cell_mass = oil_grid[x][y];
            cells_sum += cell_mass - actual_cell_mass;
        }
    }

    return cells_sum;
}

vector<vector<int>> Automata::get_N_generation(int N) {

    for (int i = 0; i < N; i++) {
        next_generation();
    }

    return oil_grid;
}

