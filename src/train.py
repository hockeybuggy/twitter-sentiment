#!/usr/bin/env python

import nltk

from finisher import binarize_labels
from nltk.featstruct import FeatStruct

def print_raw_confusion_matrix(cc):
    print "\n   \tpos\tneu\tneg"
    print "pos\t",cc["positive"]["positive"],"\t",cc["positive"]["neutral"],"\t",cc["positive"]["negative"]
    print "neu\t",cc["neutral"]["positive"],"\t",cc["neutral"]["neutral"],"\t",cc["neutral"]["negative"]
    print "neg\t",cc["negative"]["positive"],"\t",cc["negative"]["neutral"],"\t",cc["negative"]["negative"]

def calculate_confusion_matrix(cc):
    label_stats = {
            "positive": {"tp": 0, "tn": 0, "fp": 0, "fn": 0},
            "neutral":  {"tp": 0, "tn": 0, "fp": 0, "fn": 0},
            "negative": {"tp": 0, "tn": 0, "fp": 0, "fn": 0},
            }
    for label in cc.keys():
        for other_label in cc.keys():
            if label == other_label:
                label_stats[label]["tp"] += cc[label][label]
            else:
                label_stats[label]["tn"] += cc[other_label][label]
                label_stats[label]["fp"] += cc[label][other_label]
                for other_other_label in cc.keys():
                    if label != other_other_label:
                        label_stats[label]["fn"] += cc[other_other_label][other_label]

        #print label, "tp:\t", label_stats[label]["tp"]
        #print label, "tn:\t", label_stats[label]["tn"]
        #print label, "fp:\t", label_stats[label]["fp"]
        #print label, "fn:\t", label_stats[label]["fn"]
    return(label_stats)


class classifier:
    def __init__(self, train_set):
        pass

    def test(self, test_set):
        cm_raw = {
                "positive": {"positive": 0, "neutral": 0, "negative": 0},
                "neutral":  {"positive": 0, "neutral": 0, "negative": 0},
                "negative": {"positive": 0, "neutral": 0, "negative": 0},
                }
        for item, intended_label in test_set:
            result = self.classifier.classify(item)
            cm_raw[result][intended_label] += 1

        print_raw_confusion_matrix(cm_raw)
        # cm stands for confusion matrix
        cm = calculate_confusion_matrix(cm_raw)

        aa = 0.0
        tp_sum = 0.0
        fp_sum = 0.0
        fn_sum = 0.0
        running_recall = 0.0
        running_precision = 0.0

        for l in cm_raw.keys():
            aa += float(cm[l]["tp"]+cm[l]["tn"])/float(cm[l]["tp"]+cm[l]["tn"]+cm[l]["fp"]+cm[l]["fn"])
            tp_sum += cm[l]["tp"]
            fp_sum += cm[l]["fp"]
            fn_sum += cm[l]["fn"]
            running_recall += cm[l]["tp"] / float(cm[l]["tp"] + cm[l]["fp"])
            running_precision += cm[l]["tp"] / float(cm[l]["tp"] + cm[l]["fn"])

        print
        print "Accuracy    :\t", nltk.classify.accuracy(self.classifier, test_set)
        print "Avg Accuracy:\t", aa / 3.0
        print u"Precision\u03BC  :\t", tp_sum / float(tp_sum + fp_sum)
        print u"Recall\u03BC     :\t", tp_sum / float(tp_sum + fn_sum)
        print "Precision M :\t", running_precision / 3.0
        print "Recall M    :\t", running_recall / 3.0


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

