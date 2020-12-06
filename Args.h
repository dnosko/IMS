//
// Created by dasa on 6. 12. 2020.
//

#ifndef IMS_C___ARGS_H
#define IMS_C___ARGS_H

struct Arguments{
public:
    int Nth_gen,
        CA_x,
        CA_y,
        oil_mass,
        oil_x1,
        oil_y1,
        oil_x2,
        oil_y2,
        land_x,
        land_y,
        land_r,
        temp,
        wind;
};

class Args {
public:
    Args();

    Arguments parseArgs(int argc, char *argv[]);

    /* prints --help to output*/
    void help();

private:
    Arguments args;

};


#endif //IMS_C___ARGS_H
