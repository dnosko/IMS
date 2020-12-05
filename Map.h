//
// Created by dasa on 5. 12. 2020.
//

#include <iostream>

#ifndef IMS_C___MAP_H
#define IMS_C___MAP_H


class Map {
public:
    Map();
    void show_map();
    char* generate_land();
private:
    int height = 70;
    int width = 70;
};


#endif //IMS_C___MAP_H
