#include <iostream>

#include "Map.h"

int main() {
    Map map;
    vector<std::pair<int,int>> vect{make_pair(60,60), make_pair(61,61),make_pair(61,62) };
    map.add_oil(vect);
    map.show_map();
    return 0;
}