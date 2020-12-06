CC = g++
CFLAGS  = -g -Wall

TARGET = ims

all:
	g++ main.cpp Args.cpp Args.h Map.cpp Map.h Automata.cpp Automata.h borders.cpp borders.h -o $(TARGET)

run:
    ./$(TARGET)

clean:
	rm -f *.ll *.out *.s *.o $(TARGET)