cmake_minimum_required(VERSION 3.15)
project(ims_c__)

set(CMAKE_CXX_STANDARD 14)

add_executable(ims_c__ main.cpp Map.cpp Map.h Automata.cpp Automata.h borders.cpp borders.h Args.cpp Args.h)