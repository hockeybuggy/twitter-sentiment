#!/usr/bin/env python

import nltk

from finisher import binarize_labels
from nltk.featstruct import FeatStruct

class multi_label_classifier:
    def __init__(self, train_set):
        self.classifier = nltk.MaxentClassifier.train(train_set)

    def test(self, test_set):
        print nltk.classify.accuracy(self.classifier, test_set)
        self.classifier.show_most_informative_features()

    def inspect_errors(self, test_set):
        errors = []
        for item, label in test_set:
            result = self.classifier.classify(item) 
            if result != label:
                errors.append((label, result, item))
        for intended, result, error in errors:
            print intended, result, error

class binary_classifier:
    def __init__(self, train_set):
        pos_train_set = binarize_labels(train_set, "positive")
        neg_train_set = binarize_labels(train_set, "negative")
        print pos_train_set
        self.pos_classifier = nltk.MaxentClassifier.train(pos_train_set)
        self.neg_classifier = nltk.MaxentClassifier.train(neg_train_set)


    def test(self, test_set):
        pos_test_set = binarize_labels(test_set, "positive")
        neg_test_set = binarize_labels(test_set, "negative")
        print "Pos:\t", nltk.classify.accuracy(self.pos_classifier, pos_test_set)
        print "Neg:\t", nltk.classify.accuracy(self.neg_classifier, neg_test_set)
        #print test_set
        correct_count = 0

        for item, intended_label in test_set:
            pos_result = self.pos_classifier.classify(item)
            neg_result = self.neg_classifier.classify(item)
            #print pos_result
            #print neg_result
            choice = self.select_choice(pos_result, neg_result)
            #print "Intended:\t", intended_label, "\tChoice:\t", choice
            if choice == intended_label:
                #print "correct"
                correct_count += 1
            elif choice == "neutral":
                if intended_label != "positive" and intended_label != "negative":
                    #print "close enough"
                    correct_count += 1


        accuracy = float(correct_count) / float(len(test_set))
        print "Overall:\t", accuracy

    def select_choice(self, pos_str, neg_str):
        pos_result = True if pos_str == "true" else False
        neg_result = True if neg_str == "true" else False
        #print pos_result
        #print neg_result
        if pos_result == True:
            return "positive"
        else:
            if neg_result == True:
                return "negative"
            else:
                return "neutral"

    def inspect_errors(self, test_set):
        pass

