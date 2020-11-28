//
// Created by awesome on 28.11.20.
//

#ifndef IMS_PROJ_CELLULARAUTOMATA_H
#define IMS_PROJ_CELLULARAUTOMATA_H

#include "unordered_map"
#include "vector"

class CellularAutomata {
public:
    enum states {
        S_EMPTY,
        S_OIL,
        S_SOURCE,
        S_BORDER
    };

    /**
     * Creates automata
     * @param width number of cells in x-direction
     * @param height number of cells in y-direction
     */
    CellularAutomata(unsigned long width, unsigned long height);

    /**
     * Sets border cells to grid
     */
    void set_borders();

    /**
     * Sets location of source and its size
     */
    void set_source();

    /**
     * Run simulation. Function is a generator returning data for each step.
     * If steps are not enabled, it returns final result only
     * @param duration number of days
     * @param steps size of step in hours
     */
    void run(unsigned int duration, unsigned int step_size = 0);

private:
    std::unordered_map<int, std::unordered_map<int, states>> grid;
};


#endif //IMS_PROJ_CELLULARAUTOMATA_H
