CC = g++
CFLAGS  = -g -Wall

TARGET = ims

all:
	g++ main.cpp Args.cpp Args.h Map.cpp Map.h Automata.cpp Automata.h borders.cpp borders.h -o $(TARGET)

run:
	./$(TARGET) -N 10 -t 30 -r 5 -i 25 -j 20

clean:
	rm -f *.ll *.out *.s *.o $(TARGET)