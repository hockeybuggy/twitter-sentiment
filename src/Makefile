
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

# Single run
single: single-maxent-111 single-maxent-110 single-maxent-101 single-maxent-100 single-maxent-011 single-maxent-010 single-maxent-001 single-maxent-000 single-bayes-111 single-bayes-110 single-bayes-101 single-bayes-100 single-bayes-011 single-bayes-010 single-bayes-001 single-bayes-000
	echo "Done"
#Run the test for the single 1 in the paper
# Not that of ABC A=Stopwords B=Uncommon words C=Normilize
single-maxent-111:
	python conductor.py 6500 --validation_metric fscore --labels pnn > m111-x.txt
single-maxent-110:
	python conductor.py 6500 --validation_metric fscore --labels pnn --no-normalize > m110-x.txt
single-maxent-101:
	python conductor.py 6500 --validation_metric fscore --labels pnn --no-uncommon-selection > m101-x.txt
single-maxent-100:
	python conductor.py 6500 --validation_metric fscore --labels pnn --no-uncommon-selection --no-normalize > m100-x.txt
single-maxent-011:
	python conductor.py 6500 --validation_metric fscore --labels pnn --no-stopword-removal > m011-x.txt
single-maxent-010:
	python conductor.py 6500 --validation_metric fscore --labels pnn --no-stopword-removal --no-normalize > m010-x.txt
single-maxent-001:
	python conductor.py 6500 --validation_metric fscore --labels pnn --no-stopword-removal --no-uncommon-selection > m001-x.txt
single-maxent-000:
	python conductor.py 6500 --validation_metric fscore --labels pnn --no-stopword-removal --no-uncommon-selection --no-normalize > m000-x.txt
single-bayes-111:
	python conductor.py 6500 --classifier_type bayes --labels pnn > b111-x.txt
single-bayes-110:
	python conductor.py 6500 --classifier_type bayes --labels pnn --no-normalize > b110-x.txt
single-bayes-101:
	python conductor.py 6500 --classifier_type bayes --labels pnn --no-uncommon-selection > b101-x.txt
single-bayes-100:
	python conductor.py 6500 --classifier_type bayes --labels pnn --no-uncommon-selection --no-normalize > b100-x.txt
single-bayes-011:
	python conductor.py 6500 --classifier_type bayes --labels pnn --no-stopword-removal > b011-x.txt
single-bayes-010:
	python conductor.py 6500 --classifier_type bayes --labels pnn --no-stopword-removal --no-normalize > b010-x.txt
single-bayes-001:
	python conductor.py 6500 --classifier_type bayes --labels pnn --no-stopword-removal --no-uncommon-selection > b001-x.txt
single-bayes-000:
	python conductor.py 6500 --classifier_type bayes --labels pnn --no-stopword-removal --no-uncommon-selection --no-normalize > b000-x.txt

## This section runs cross-validations
crossfolds: crossfolds-m crossfolds-b
crossfolds-m: crossfolds-m111 crossfolds-m100 crossfolds-m010 crossfolds-m001 crossfolds-m000
crossfolds-b: crossfolds-b111 crossfolds-b100 crossfolds-b010 crossfolds-b001 crossfolds-b000

crossfolds-m111:
	python crossval.py 6500 --validation_metric fscore --labels pnn > m111-cf.txt

crossfolds-m100:
	python crossval.py 6500 --validation_metric fscore --labels pnn  --no-uncommon-selection --no-normalize > m100-cf.txt

crossfolds-m010:
	python crossval.py 6500 --validation_metric fscore --labels pnn --no-normalize --no-stopword-removal > m010-cf.txt

crossfolds-m001:
	python crossval.py 6500 --validation_metric fscore --labels pnn --no-stopword-removal --no-uncommon-selection > m001-cf.txt

crossfolds-m000:
	python crossval.py 6500 --validation_metric fscore --labels pnn --no-stopword-removal --no-uncommon-selection --no-normalize > m000-cf.txt

crossfolds-b111:
	python crossval.py 6500 --classifier_type bayes --labels pnn > b111-cf.txt

crossfolds-b100:
	python crossval.py 6500 --classifier_type bayes --labels pnn  --no-uncommon-selection --no-normalize > b100-cf.txt

crossfolds-b010:
	python crossval.py 6500 --classifier_type bayes --labels pnn --no-normalize --no-stopword-removal > b010-cf.txt

crossfolds-b001:
	python crossval.py 6500 --classifier_type bayes --labels pnn --no-stopword-removal --no-uncommon-selection > b001-cf.txt

crossfolds-b000:
	python crossval.py 6500 --classifier_type bayes --labels pnn --no-stopword-removal --no-uncommon-selection --no-normalize > b000-cf.txt

crossfolds10: crossfolds10-m crossfolds10-b
crossfolds10-m: crossfolds10-m111 crossfolds10-m100 crossfolds10-m010 crossfolds10-m001 crossfolds10-m000
crossfolds10-b: crossfolds10-b111 crossfolds10-b100 crossfolds10-b010 crossfolds10-b001 crossfolds10-b000

crossfolds10-m111:
	python crossval.py 6500 --validation_metric fscore --labels pnn --num-folds 10 > m111-cf-10.txt

crossfolds10-m100:
	python crossval.py 6500 --validation_metric fscore --labels pnn  --no-uncommon-selection --no-normalize --num-folds 10 > m100-cf-10.txt

crossfolds10-m010:
	python crossval.py 6500 --validation_metric fscore --labels pnn --no-normalize --no-stopword-removal --num-folds 10 > m010-cf-10.txt

crossfolds10-m001:
	python crossval.py 6500 --validation_metric fscore --labels pnn --no-stopword-removal --no-uncommon-selection --num-folds 10 > m001-cf-10.txt

crossfolds10-m000:
	python crossval.py 6500 --validation_metric fscore --labels pnn --no-stopword-removal --no-uncommon-selection --no-normalize --num-folds 10 > m000-cf-10.txt

crossfolds10-b111:
	python crossval.py 6500 --classifier_type bayes --labels pnn --num-folds 10 > b111-cf-10.txt

crossfolds10-b100:
	python crossval.py 6500 --classifier_type bayes --labels pnn  --no-uncommon-selection --no-normalize --num-folds 10 > b100-cf-10.txt

crossfolds10-b010:
	python crossval.py 6500 --classifier_type bayes --labels pnn --no-normalize --no-stopword-removal --num-folds 10 > b010-cf-10.txt

crossfolds10-b001:
	python crossval.py 6500 --classifier_type bayes --labels pnn --no-stopword-removal --no-uncommon-selection --num-folds 10 > b001-cf-10.txt

crossfolds10-b000:
	python crossval.py 6500 --classifier_type bayes --labels pnn --no-stopword-removal --no-uncommon-selection --no-normalize --num-folds 10 > b000-cf-10.txt

## Num Iterations experiment
iterations: iterations-5 iterations-10 iterations-15 iterations-20 iterations-25 iterations-30 iterations-35 iterations-40 iterations-45 iterations-50 iterations-55

iterations-5:
	python crossval.py 6500 --numIterations 5  --labels pnn --num-folds 5 > ni-5.txt
iterations-10:
	python crossval.py 6500 --numIterations 10 --labels pnn --num-folds 5 > ni-10.txt
iterations-15:
	python crossval.py 6500 --numIterations 15 --labels pnn --num-folds 5 > ni-15.txt
iterations-20:
	python crossval.py 6500 --numIterations 20 --labels pnn --num-folds 5 > ni-20.txt
iterations-25:
	python crossval.py 6500 --numIterations 25 --labels pnn --num-folds 5 > ni-25.txt
iterations-30:
	python crossval.py 6500 --numIterations 30 --labels pnn --num-folds 5 > ni-30.txt
iterations-35:
	python crossval.py 6500 --numIterations 35 --labels pnn --num-folds 5 > ni-35.txt
iterations-40:
	python crossval.py 6500 --numIterations 40 --labels pnn --num-folds 5 > ni-40.txt
iterations-45:
	python crossval.py 6500 --numIterations 45 --labels pnn --num-folds 5 > ni-45.txt
iterations-50:
	python crossval.py 6500 --numIterations 50 --labels pnn --num-folds 5 > ni-50.txt
iterations-55:
	python crossval.py 6500 --numIterations 55 --labels pnn --num-folds 5 > ni-55.txt
