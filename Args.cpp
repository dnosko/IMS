//
// Created by dasa on 6. 12. 2020.
//

#include <getopt.h>
#include <iostream>
#include "Args.h"

Args::Args() {
    args.Nth_gen = 0;
    args.CA_x = 100;
    args.CA_y = 100;
    args.oil_mass = 790;
    args.oil_x1 = 10;
    args.oil_y1 = 10;
    args.oil_x2 = 20;
    args.oil_y2 = 15;
    args.land_x = 20;
    args.land_y = 10,
    args.land_r = 5,
    args.wind = 4;
}

Arguments Args::parseArgs(int argc, char **argv) {

    int c;
    while ((c = getopt (argc, argv, "N:x:y:o:k:l:m:n:i:j:r:w:h")) != -1) {
        switch(c){
            case 'N':
                args.Nth_gen = atoi(optarg);
                break;
            case 'x':
                args.CA_x = atoi(optarg);
                break;
            case 'y':
                args.CA_y = atoi(optarg);
                break;
            case 'o':
                args.oil_mass = atoi(optarg);
                break;
            case 'k':
                args.oil_x1 = atoi(optarg);
                break;
            case 'l':
                args.oil_y1 = atoi(optarg);
                break;
            case 'm':
                args.oil_x2 = atoi(optarg);
                break;
            case 'n':
                args.oil_y2 = atoi(optarg);
                break;
            case 'i':
                args.land_x = atoi(optarg);
                break;
            case 'j':
                args.land_y = atoi(optarg);
                break;
            case 'r':
                args.land_r = atoi(optarg);
                break;
            case 'w':
                args.wind = atoi(optarg);
                break;
            case 'h':
                help();
                exit(0);
            default:
                std::cout << "Invalid arguments!\n";
                help();
                exit(0);
        }
    }
    return args;
}

void Args::help() {

    std::cout << "./ims [-h] [-Nxyoklmnijr <int>] [-w] \n\n"
              << "\t-h\t Prints help/usage\n\n"
              << "\t-N\t Generate Nth generation\n"
              << "\t-x\t Map width \n"
              << "\t-y\t Map height \n"
              << "\t-o\t Oil spill in kgs \n"
              << "\t-k\t Oil x1 \n"
              << "\t-l\t Oil y1 \n"
              << "\t-m\t Oil x2 \n"
              << "\t-n\t Oil y2 \n"
              << "\t-i\t Island x coordinate \n"
              << "\t-j\t Island y coordinate \n"
              << "\t-r\t Island radius \n\n"
              << "\t-w\t Wind direction:\n"
              << "\t\t\tNorth = 0\n"
                 "\t\t\tWest = 1 \n"
                 "\t\t\tEast = 2\n"
                 "\t\t\tSouth = 3\n"
                 "\t\t\tNoWind = 4\n" <<

                 "" << std::endl;

}
