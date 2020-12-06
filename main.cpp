#include <iostream>

#include "Map.h"
#include "Automata.h"
#include "borders.h"
#include "Args.h"

//TODO argumenty
// zobrazit simulaciu po Xtom dni

int main(int argc, char* argv[]) {

    map<Automata::WindDirection ,std::string> m;
    m[Automata::North] = "^ North";
    m[Automata::West] = "< West";
    m[Automata::East] = "> East";
    m[Automata::South] = "v South";
    m[Automata::NoWind] = "No wind";

    Args args;
    Arguments arguments = args.parseArgs(argc, argv);

    Map map(arguments.CA_x, arguments.CA_y);
    Automata automata(arguments.CA_x, arguments.CA_y, arguments.oil_mass,
                      static_cast<Automata::WindDirection>(arguments.wind));

    /* swap if needed */
    if (arguments.oil_x1 > arguments.oil_x2) {
        swap(arguments.oil_x1,arguments.oil_x2);
    }

    if (arguments.oil_y1 > arguments.oil_y2) {
        swap(arguments.oil_y1,arguments.oil_y2);
    }

    int oil_width = arguments.oil_x2 - arguments.oil_x1;
    int oil_height = arguments.oil_y2 - arguments.oil_y1;

    if (oil_width > arguments.CA_x || oil_height > arguments.CA_y){
        std::cout << "Oil must be inside CA/Map";
        return 1;
    }
    automata.init_oil(make_pair(arguments.oil_x1, arguments.oil_y1), make_pair(arguments.oil_x2, arguments.oil_y2));

    // get borders
    auto island = get_island(arguments.land_x, arguments.land_y, arguments.land_r);

    if (arguments.land_r != 0 && (arguments.land_r >= arguments.CA_x || arguments.land_r >= arguments.CA_y)) {
        std::cout << "Land radius can't be bigger than size of CA/Map.";
        return 1;
    }

    automata.init_borders(island);

    vector<vector<int>> oil;
    oil = automata.get_N_generation(arguments.Nth_gen);
    map.add_oil(oil, arguments.oil_mass);

    // output
    map.show_map();

    int time = arguments.Nth_gen;
    std::cout << "Time elapsed: " << time/24 <<" days "<< time % 24 << " h" << "\n";
    std::cout << "Wind direction: " << m[static_cast<Automata::WindDirection>(arguments.wind)] << "\n";
    std::cout << "Oil at the start in: " << automata.oil_cell_count << " cells \n";
    std::cout << "Oil at the end in: " << map.oil_count_end << " cells \n";
    return 0;
}


