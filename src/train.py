#!/usr/bin/env python

import nltk

from finisher import binarize_labels
from nltk.featstruct import FeatStruct

class classifier:
    def __init__(self, train_set):
        pass

    def test(self, test_set):
        cc = {
                "positive": {"positive": 0, "neutral": 0, "negative": 0},
                "neutral":  {"positive": 0, "neutral": 0, "negative": 0},
                "negative": {"positive": 0, "neutral": 0, "negative": 0},
                }
        for item, intended_label in test_set:
            result = self.classifier.classify(item)
            cc[result][intended_label] += 1

        # This ulgy blob prints a confusion matrix
        print "\n   \tpos\tneu\tneg"
        print "pos\t", cc["positive"]["positive"], "\t",cc["positive"]["neutral"], "\t", cc["positive"]["negative"]
        print "neu\t", cc["neutral"]["positive"], "\t", cc["neutral"]["neutral"], "\t", cc["neutral"]["negative"]
        print "neg\t", cc["negative"]["positive"], "\t", cc["negative"]["neutral"], "\t", cc["negative"]["negative"]

        print "Accuracy:", nltk.classify.accuracy(self.classifier, test_set)
        print "Accuracy:", (cc["positive"]["positive"] + cc["neutral"]["neutral"] + cc["negative"]["negative"]) / float(len(test_set))

        #for label in cc.keys():
            #print label

        print "Avg Accuracy:", (cc["positive"]["positive"] + cc["neutral"]["neutral"] + cc["negative"]["negative"]) / float(len(test_set))


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
    def __init__(self, train_set):
        self.classifier = nltk.MaxentClassifier.train(train_set, min_lldelta=0.01)

class multi_label_naive_bayes_classifier(classifier):
    def __init__(self, train_set):
        self.classifier = nltk.NaiveBayesClassifier.train(train_set)


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
        if pos_result == True:
            return "positive"
        else:
            if neg_result == True:
                return "negative"
            else:
                return "neutral"

    def inspect_errors(self, test_set):
        pass

