#include <iostream>

#include "Map.h"
#include "Automata.h"

//TODO argumenty
// zobrazit simulaciu po Xtom dni

int main() {
    int x = 20;
    int y = 70;
    Map map(x, y);
    Automata automata(x, y, 790, static_cast<Automata::WindDirection>(1));
    automata.init_oil(make_pair(10, 60), make_pair(15, 65));
    vector<vector<int>> oil;
    oil = automata.get_N_generation(100);
    int max_mass = 790;
    map.add_oil(oil, max_mass);
    map.show_map();
    return 0;
}