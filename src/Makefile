
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

# --- Testing targets ---
test:
	echo "Not yet implemented" #TODO implement

# --- small dataset ---
tiny:
	python conductor.py 10 --minlldelta 0.02

# --- Small dataset - Only positive and negitive labels ---

small-pn: small-baseline-pn small-no-uncommon-selection-pn small-no-stopword-removal-pn small-val-acc-pn small-val-fsc-pn small-bayes-pn

small-lldelta-pn:
	python conductor.py 250 --minlldelta 0.02

small-baseline-pn:
	python conductor.py 250 --validation_metric accuracy --no-uncommon-selection --no-stopword-removal --no-normalize-words --no-normalize-punct --no-normalize-emoticons --no-normalize-users --no-normalize-hashtags --no-normalize-nums --no-normalize-urls

small-no-uncommon-selection-pn:
	python conductor.py 250 --validation_metric accuracy --no-uncommon-selection

small-no-stopword-removal-pn:
	python conductor.py 250 --validation_metric accuracy --no-stopword-removal

small-val-acc-pn:
	python conductor.py 250 --validation_metric accuracy

small-val-fsc-pn:
	python conductor.py 250 --validation_metric fscore

small-bayes-pn:
	python conductor.py 250 --classifier_type bayes

small-bayes-baseline-pn:
	python conductor.py 250 --classifier_type bayes --no-uncommon-selection --no-stopword-removal --no-normalize-words --no-normalize-punct --no-normalize-emoticons --no-normalize-users --no-normalize-hashtags --no-normalize-nums --no-normalize-urls

# --- Small dataset - Positive, neutral, and negative labels ---

small-pnn: small-baseline-pnn small-no-uncommon-selection-pnn small-no-stopword-removal-pnn small-val-acc-pnn small-val-fsc-pnn small-bayes-pnn

small-baseline-pnn:
	python conductor.py 250 --validation_metric fscore --no-uncommon-selection --no-stopword-removal --no-normalize-words --no-normalize-punct --no-normalize-emoticons --no-normalize-users --no-normalize-hashtags --no-normalize-nums --no-normalize-urls --labels pnn

small-no-uncommon-selection-pnn:
	python conductor.py 250 --validation_metric fscore --no-uncommon-selection --labels pnn

small-no-stopword-removal-pnn:
	python conductor.py 250 --validation_metric fscore --no-stopword-removal --labels pnn

small-val-acc-pnn:
	python conductor.py 250 --validation_metric fscore --labels pnn

small-val-fsc-pnn:
	python conductor.py 250 --validation_metric fscore --labels pnn

small-bayes-pnn:
	python conductor.py 250 --classifier_type bayes --labels pnn

small-bayes-baseline-pnn:
	python conductor.py 250 --classifier_type bayes --no-uncommon-selection --no-stopword-removal --no-normalize-words --no-normalize-punct --no-normalize-emoticons --no-normalize-users --no-normalize-hashtags --no-normalize-nums --no-normalize-urls --labels pnn

# --- Full dataset - Only positive, negative labels ---

test-pn: test-baseline-pn test-no-uncommon-selection-pn test-no-stopword-removal-pn test-val-acc-pn test-val-fsc-pn test-bayes-pn

test-20iter-pn:
	python conductor.py 6500 --numIterations 20

test-baseline-pn:
	python conductor.py 6500 --validation_metric accuracy --no-uncommon-selection --no-stopword-removal --no-normalize-words --no-normalize-punct --no-normalize-emoticons --no-normalize-users --no-normalize-hashtags --no-normalize-nums --no-normalize-urls

test-no-uncommon_selection-pn:
	python conductor.py 6500 --validation_metric accuracy --no-uncommon-selection

test-no-stopword-removal-pn:
	python conductor.py 6500 --validation_metric accuracy --no-stopword-removal

test-val-acc-pn:
	python conductor.py 6500 --validation_metric accuracy

test-val-fsc-pn:
	python conductor.py 6500 --validation_metric fscore

test-bayes-pn:
	python conductor.py 6500 --classifier_type bayes

test-bayes-baseline-pn:
	python conductor.py 6500 --classifier_type bayes --no-uncommon-selection --no-stopword-removal --no-normalize-words --no-normalize-punct --no-normalize-emoticons --no-normalize-users --no-normalize-hashtags --no-normalize-nums --no-normalize-urls

# --- Full dataset - Positive, neutral, and negative labels ---

test-pnn: test-baseline-pnn test-no-uncommon-selection-pnn test-no-stopword-removal-pnn test-val-acc-pnn test-val-fsc-pnn test-bayes-pnn

test-20iter-pnn:
	python conductor.py 6500 --numIterations 20 --labels pnn

test-baseline-pnn:
	python conductor.py 6500 --validation_metric accuracy --no-uncommon-selection --no-stopword-removal --no-normalize-words --no-normalize-punct --no-normalize-emoticons --no-normalize-users --no-normalize-hashtags --no-normalize-nums --no-normalize-urls --labels pnn

test-no-uncommon_selection-pnn:
	python conductor.py 6500 --validation_metric accuracy --no-uncommon-selection --labels pnn

test-no-stopword-removal-pnn:
	python conductor.py 6500 --validation_metric accuracy --no-stopword-removal --labels pnn

test-val-acc-pnn:
	python conductor.py 6500 --validation_metric accuracy --labels pnn

test-val-fsc-pnn:
	python conductor.py 6500 --validation_metric fscore --labels pnn

test-bayes-pnn:
	python conductor.py 6500 --classifier_type bayes --labels pnn

test-bayes-baseline-pnn:
	python conductor.py 6500 --classifier_type bayes --no-uncommon-selection --no-stopword-removal --no-normalize --labels pnn

#Run the test for the table 1 in the paper
# Not that of ABC A=Stopwords B=Uncommon words C=Normilize

table-maxent-111:
	python conductor.py 6500 --validation_metric fscore --labels pnn
table-maxent-110:
	python conductor.py 6500 --validation_metric fscore --labels pnn --no-normalize
table-maxent-101:
	python conductor.py 6500 --validation_metric fscore --labels pnn --no-uncommon-selection
table-maxent-100:
	python conductor.py 6500 --validation_metric fscore --labels pnn --no-uncommon-selection --no-normalize
table-maxent-011:
	python conductor.py 6500 --validation_metric fscore --labels pnn --no-stopword-removal
table-maxent-010:
	python conductor.py 6500 --validation_metric fscore --labels pnn --no-stopword-removal --no-normalize
table-maxent-001:
	python conductor.py 6500 --validation_metric fscore --labels pnn --no-stopword-removal --no-uncommon-selection
table-maxent-000:
	python conductor.py 6500 --validation_metric fscore --labels pnn --no-stopword-removal --no-uncommon-selection --no-normalize
table-bayes-111:
	python conductor.py 6500 --classifier_type bayes --labels pnn
table-bayes-110:
	python conductor.py 6500 --classifier_type bayes --labels pnn --no-normalize
table-bayes-101:
	python conductor.py 6500 --classifier_type bayes --labels pnn --no-uncommon-selection
table-bayes-100:
	python conductor.py 6500 --classifier_type bayes --labels pnn --no-uncommon-selection --no-normalize
table-bayes-011:
	python conductor.py 6500 --classifier_type bayes --labels pnn --no-stopword-removal
table-bayes-010:
	python conductor.py 6500 --classifier_type bayes --labels pnn --no-stopword-removal --no-normalize
table-bayes-001:
	python conductor.py 6500 --classifier_type bayes --labels pnn --no-stopword-removal --no-uncommon-selection
table-bayes-000:
	python conductor.py 6500 --classifier_type bayes --labels pnn --no-stopword-removal --no-uncommon-selection --no-normalize

