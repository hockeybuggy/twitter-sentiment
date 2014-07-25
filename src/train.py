#!/usr/bin/env python

import nltk
import statsify

from nltk.featstruct import FeatStruct
from maxent_classifier_with_validation import train_maxent_classifier_with_validation

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


class maxent_classifier(classifier):
    def __init__(self, train_set, iterations=None, lldelta=None, ll=None):
        if lldelta:
            print "Cutoff after log likelyhood changes by less than", lldelta
            self.classifier = nltk.MaxentClassifier.train(train_set, min_lldelta=lldelta)
        elif ll:
            print "Cutoff after log likelyhood reaches", ll
            self.classifier = nltk.MaxentClassifier.train(train_set, min_ll=ll)
        else:
            if not iterations:
                iterations = 25
            print "Cutoff after {} iterations".format(iterations)
            self.classifier = nltk.MaxentClassifier.train(train_set, max_iter=iterations)


class maxent_classifier_with_validation(classifier):
    def __init__(self, train_set, validation_set, metric_type):
        self.classifier = nltk.MaxentClassifier.train(train_set, trace=1, max_iter=5)
        iter_count = 0
        if metric_type == "accuracy":
            metric = nltk.classify.accuracy(self.classifier, validation_set)
        else:
            metric = statsify.calculate_fscore(self.classifier, validation_set)
        prev_metric = 0.0
        print "Iteration {} {}  :\t{}".format(iter_count, metric_type, metric)
        while (metric - prev_metric) > 0.0:
            iter_count += 1
            prev_weights = self.classifier.weights()
            self.classifier = train_maxent_classifier_with_validation(train_set,
                    trace=1, prev_weights=prev_weights, max_iter=1)
            prev_metric = metric
            if metric_type == "accuracy":
                metric = nltk.classify.accuracy(self.classifier, validation_set)
            else:
                metric = statsify.calculate_fscore(self.classifier, validation_set)
            print "Iteration {} {}  :\t{}".format(iter_count, metric_type, metric)
            print "{} delta  :\t{}".format(metric_type, metric - prev_metric)
        print "Restoring iteration {} weights".format(iter_count-1)
        self.classifier.set_weights(prev_weights)


class naive_bayes_classifier(classifier):
    def __init__(self, train_set):
        self.classifier = nltk.NaiveBayesClassifier.train(train_set)

