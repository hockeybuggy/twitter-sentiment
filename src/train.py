#!/usr/bin/env python

import nltk
import statsify

from nltk.featstruct import FeatStruct

class classifier:
    def __init__(self, train_set):
        pass

    def test(self, test_set, labels):
        if labels == "pnn":
            statsify.multi_label_classifier_test(self.classifier, test_set)
        else:
            statsify.bi_label_classifier_test(self.classifier, test_set)

    def show_informitive_features(self):
        self.classifier.show_most_informative_features(20)

    def inspect_errors(self, test_set):
        errors = []
        for item, label in test_set:
            result = self.classifier.classify(item)
            if result != label:
                errors.append((label, result, item))
        for intended, result, error in errors:
            print "Should have been:", intended, "Was:", result, error


class multi_label_classifier(classifier):
    def __init__(self, train_set, lldelta=None, ll=None):
        if lldelta:
            print "Cutoff after log likelyhood changes by less than", lldelta
            self.classifier = nltk.MaxentClassifier.train(train_set, min_lldelta=lldelta)
        elif ll:
            print "Cutoff after log likelyhood reaches", ll
            self.classifier = nltk.MaxentClassifier.train(train_set, min_ll=ll)
        else:
            print "Cutoff after 50 iterations"
            self.classifier = nltk.MaxentClassifier.train(train_set, max_iter=50)

class multi_label_naive_bayes_classifier(classifier):
    def __init__(self, train_set):
        self.classifier = nltk.NaiveBayesClassifier.train(train_set)

