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
    Automata(int rows, int columns, int max_mass);
    Automata();
    vector<Coord> init_oil(Coord c1, Coord c2);

private:
    int x = 10;
    int y = 10;
    int max_oil = 10;
    //constants
    float m = 0.098;  // spreading in the four adjacent cells
    float d = 0.0176; // spreading constant for diagonal cells

};


#endif //IMS_C___AUTOMATA_H
