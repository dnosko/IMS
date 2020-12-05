#include <iostream>

#include "Map.h"
#include "Automata.h"

//TODO argumenty
// zobrazit simulaciu po Xtom dni

int main() {
    Map map;
    Automata automata(70, 70, 10, static_cast<Automata::WindDirection>(1));
    vector<std::pair<int,int>> vect{make_pair(60,60), make_pair(61,61),make_pair(61,62) };
    vector<pair<Coord, int>> oil = automata.init_oil(make_pair(60, 60), make_pair(70, 70));
    map.add_oil(oil);
    map.show_map();
    return 0;
}