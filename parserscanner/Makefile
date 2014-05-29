
#File       : Makefile
#Author     : Douglas Anderson
#Description: Makefile for semeval parser scanner

# --- Programs ---
CC = gcc
FLEX = flex
YACC = yacc

# --- Files ---
SPEC = semeval.lex
GRAMMER = semeval.y

# --- Miscellaneous ---
CFLAGS = -g -Wall
OBJS = y.tab.o lex.yy.o util.o main.o
LIBS = -ly -ll
EXE = parserscanner

# --- Targets ---
all: clean parserscanner

parserscanner: $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $(EXE) $(LIBS)

lex.yy.c: $(SPEC)
	$(FLEX) $(SPEC)

lex.yy.o: lex.yy.c y.tab.c y.tab.h
	$(CC) -o lex.yy.o -c lex.yy.c -g

y.tab.c: $(GRAMMER)
	$(YACC) -d $(GRAMMER)

y.tab.o: y.tab.c scan.h parse.h
	$(CC) -c y.tab.c -g

main.o: main.c globals.h scan.h parse.h util.h
	$(CC) $(CFLAGS) -c main.c

util.o: globals.h scan.h parse.h y.tab.h
	$(CC) $(CFLAGS) -c util.c

.PHONY: clean

clean:
	rm -f $(EXE) $(OBJS) lex.yy.c y.tab.h y.tab.c

