#!/usr/bin/env python

import nltk

from nltk.featstruct import FeatStruct


def train(train_set, test_set=None):
    for i in train_set:
        print i
    classifier = nltk.MaxentClassifier.train(train_set)
    if test_set:
        print nltk.classify.accuracy(classifier, test_set)
