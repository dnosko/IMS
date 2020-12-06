#include <iostream>

#include "Map.h"
#include "Automata.h"
#include "borders.h"
#include "Args.h"

//TODO argumenty
// zobrazit simulaciu po Xtom dni

int main(int argc, char* argv[]) {

    Args args;
    Arguments arguments = args.parseArgs(argc, argv);

    Map map(arguments.CA_x, arguments.CA_y);
    Automata automata(arguments.CA_x, arguments.CA_y, arguments.oil_mass,
                      static_cast<Automata::WindDirection>(arguments.wind));

    automata.init_oil(make_pair(arguments.oil_x1, arguments.oil_y1), make_pair(arguments.oil_x2, arguments.oil_y2));

    // get borders
    auto island = get_island(arguments.land_x, arguments.land_y, arguments.land_r);
    automata.init_borders(island);

    vector<vector<int>> oil;
    oil = automata.get_N_generation(arguments.Nth_gen);
    map.add_oil(oil, arguments.oil_mass);
    map.show_map();
    std::cout << "Generation " << arguments.Nth_gen;
    return 0;
}