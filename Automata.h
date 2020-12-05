//
// Created by dasa on 5. 12. 2020.
//

#ifndef IMS_C___AUTOMATA_H
#define IMS_C___AUTOMATA_H

#include <vector>

using namespace std;
using Coord = pair<int, int>;

class Automata {
public:

    enum WindDirection{
        North,
        West,
        East,
        South,
        NoWind
    };

    vector<pair<Coord ,int>> oil_grid;
    WindDirection wind_direction = NoWind;
    Automata(int rows, int columns, int max_mass, WindDirection wind);
    Automata();
    vector<pair<Coord, int>> init_oil(Coord c1, Coord c2);


private:
    int rows = 10;
    int cols = 10;
    int max_oil = 10;
    //constants
    float m = 0.098;  // spreading in the four adjacent cells
    float d = 0.0176; // spreading constant for diagonal cells
    vector<Coord> neighborhood;

    void get_neighbors(Coord cell); // returns moore neighborhood
    void next_generation();
    int rules(int actual_cell_mass);
    int wind(int actual_cell_mass);
    int cells_sum(unsigned from, unsigned to, int actual_cell_mass); // type = 'A'=adjustent cells or 'D'=diagonal
};


#endif //IMS_C___AUTOMATA_H
