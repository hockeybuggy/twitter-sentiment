#!/usr/bin/env python

import nltk

from nltk.featstruct import FeatStruct

class maxent_classifer:
    def __init__(self, train_set):
        self.classifier = nltk.MaxentClassifier.train(train_set)

    def test(self, test_set):
        print nltk.classify.accuracy(self.classifier, test_set)

    def inspect_errors(self, test_set):
        errors = []
        for item, label in test_set:
            result = self.classifier.classify(item) 
            if result != label:
                errors.append((label, result, item))
        for intended, result, error in errors:
            print intended, result, error
