CC = gcc
CFLAGS  = -g -Wall

TARGET = ims

all:
	gcc helloword.c -o $(TARGET)

clean:
	rm -f *.ll *.out *.s *.o $(TARGET)