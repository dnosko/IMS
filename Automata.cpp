//
// Created by dasa on 5. 12. 2020.
//

#include <iostream>
#include "Automata.h"

Automata::Automata(int rows, int columns, int max_mass) {
    x = rows;
    y = columns;
    max_oil = max_mass;
}

vector<Coord> Automata::init_oil(Coord c1, Coord c2) {

    vector<Coord> oil;
    Coord oil_cell;

    for(int x = c1.first; x < c2.first; x++){
        for(int y = c1.second; y < c2.second; y++){
            oil_cell = make_pair(x,y);
            oil.push_back(oil_cell);
        }
    }

    return oil;
}

Automata::Automata() {

}
