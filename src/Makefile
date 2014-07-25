
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

.PHONY: clean all test

clean:
	rm -f $(EXE) $(OBJS) lex.yy.c *.pyc

test: test-1

tiny:
	python conductor.py 10 --minlldelta 0.02

small:
	python conductor.py 250 --minlldelta 0.02

small-val: small-val-acc

small-val-acc:
	python conductor.py 250 --validationMetric accuracy

small-val-fsc:
	python conductor.py 250 --validationMetric fscore

small-bayes:
	python conductor.py 250 --classifier_type bayes

test-1:
	python conductor.py 6500 --numIterations 20

test-val-acc:
	python conductor.py 6500 --validationMetric accuracy

test-val-fsc:
	python conductor.py 6500 --validationMetric fscore

test-bayes:
	python conductor.py 6500 --classifier_type bayes

