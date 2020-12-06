#include <iostream>

#include "Map.h"
#include "Automata.h"
#include "borders.h"

//TODO argumenty
// zobrazit simulaciu po Xtom dni

int main() {
    int x = 40;
    int y = 40;
    Map map(x, y);
    Automata automata(x, y, 790, static_cast<Automata::WindDirection>(4));

    automata.init_oil(make_pair(18, 22), make_pair(18, 22));
    auto island = get_island(15, 20, 5);
    automata.init_borders(island);

    vector<vector<int>> oil;
    oil = automata.get_N_generation(1);
    int max_mass = 790;
    map.add_oil(oil, max_mass);
    map.show_map();
    return 0;
}