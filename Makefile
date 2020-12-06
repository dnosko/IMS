CC = gcc
CFLAGS  = -g -Wall

TARGET = ims

all:
	gcc main.cpp Map.cpp Map.h Automata.cpp Automata.h borders.cpp borders.h -o $(TARGET)

clean:
	rm -f *.ll *.out *.s *.o $(TARGET)