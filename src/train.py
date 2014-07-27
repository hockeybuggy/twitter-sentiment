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

    def show_informitive_features(self, numFeatures):
        self.classifier.show_most_informative_features(numFeatures)

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
    def __init__(self, train_set, validation_set, metric_type, smoothing):
        self.classifier = nltk.MaxentClassifier.train(train_set, trace=1, max_iter=5)
        iter_count = 0
        rounds_without_improvment = 0
        if metric_type == "accuracy":
            metric = nltk.classify.accuracy(self.classifier, validation_set)
        else:
            metric = statsify.calculate_fscore(self.classifier, validation_set)
        best_iteration = 0
        best_metric = metric
        best_weights = self.classifier.weights()
        print "Iteration {} {}  :\t{}".format(iter_count, metric_type, metric)
        #while (metric - prev_metric) >= 0.0:
        while rounds_without_improvment < smoothing:
            iter_count += 1
            self.classifier = train_maxent_classifier_with_validation(train_set,
                    trace=1, prev_weights=self.classifier.weights(), max_iter=1)
            if metric_type == "accuracy":
                metric = nltk.classify.accuracy(self.classifier, validation_set)
            else:
                metric = statsify.calculate_fscore(self.classifier, validation_set)
            print "Iteration {} {}  :\t{}".format(iter_count, metric_type, metric)
            print "{} delta  :\t{}".format(metric_type, metric - best_metric)
            if(metric - best_metric) <= 0.0:
                rounds_without_improvment += 1
            else:
                rounds_without_improvment = 0
                best_iteration = iter_count
                best_metric = metric
                best_weights = self.classifier.weights()

        print "Restoring iteration {} weights".format(best_iteration)
        self.classifier.set_weights(best_weights)


class naive_bayes_classifier(classifier):
    def __init__(self, train_set):
        self.classifier = nltk.NaiveBayesClassifier.train(train_set)

