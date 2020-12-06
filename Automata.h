//
// Created by dasa on 5. 12. 2020.
//

#ifndef IMS_C___AUTOMATA_H
#define IMS_C___AUTOMATA_H

#include <vector>
#include <map>
#include <iostream>
#include <iterator>

#define ENUM_LEN 4

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

    vector<vector<double>> oil_grid;
    WindDirection wind_direction;


    Automata(int x, int y, int max_mass, WindDirection wind);
    void init_oil(Coord c1, Coord c2);
    void init_borders(std::vector<Coord>);
    vector<vector<double>> get_N_generation(int N);


private:
    int rows;
    int cols;
    int max_oil;

    //constants
    float m = 0.098;  // spreading in the four adjacent cells
    float d = 0.0176; // spreading constant for diagonal cells
    vector<Coord> neighborhood;


    vector<Coord> get_neighbors(Coord cell); // returns moore neighborhood
    vector<Coord> skip_neighbors(vector<Coord> neighbors);
    void next_generation();
    double rules(double actual_cell_mass);
    double wind(double actual_cell_mass);
    int cells_sum(unsigned from, unsigned to, int actual_cell_mass); // type = 'A'=adjustent cells or 'D'=diagonal
};


#endif //IMS_C___AUTOMATA_H
