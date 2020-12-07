CC = g++
CFLAGS  = -g -Wall

TARGET = ims

all:
	g++ main.cpp Map.cpp Map.h Automata.cpp Automata.h borders.cpp borders.h Args.cpp Args.h -o $(TARGET)

clean:
	rm -f *.ll *.out *.s *.o $(TARGET)