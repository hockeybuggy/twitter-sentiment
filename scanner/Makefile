
# File        : Makefile
# Author      : Douglas Anderson
# Description : Makefile for semantic eval scanner

# --- Programs ---
CC = gcc
FLEX = flex

# --- Files ---
SPEC = semeval.lex

# --- Miscellaneous ---
CFLAGS = -g -Wall
OBJS = lex.yy.o util.o main.o
LIBS = -ll
EXE = scanner

# --- Targets ---
all: clean scanner

py: clean module

scanner: $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $(EXE) $(LIBS)

lex.yy.c: $(SPEC)
	$(FLEX) $(SPEC)

lex.yy.o: lex.yy.c
	$(CC) -o lex.yy.o -c lex.yy.c -g

main.o: main.c globals.h scan.h util.h
	$(CC) $(CFLAGS) -c main.c

util.o: globals.h scan.h
	$(CC) $(CFLAGS) -c util.c

module: globals.h scan.h
	$(CC) -shared -I/usr/include/python2.7/ -lpython2.7 -Wall -fPIC -o scanner_module.so scanner_module.c

.PHONY: clean all py

clean:
	rm -f $(EXE) $(OBJS) lex.yy.c

