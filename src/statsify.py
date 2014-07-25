#!/usr/bin/env python

# File       : statsify.py
# Author     : Douglas Anderson
# Description: Generates stats

import nltk

def __call__(feature_list, labels):
    # Count the document by label
    num_docs = len(feature_list)
    num_pos_docs = len([x for x in feature_list if x[1] == "positive"])
    if labels == "pnn":
        num_neu_docs = len([x for x in feature_list if x[1] == "neutral"])
    num_neg_docs = len([x for x in feature_list if x[1] == "negative"])

    print "Total number of documents:", num_docs
    print "% positive :", num_pos_docs / float(num_docs)
    if labels == "pnn":
        print "% neutral  :", num_neu_docs / float(num_docs)
    print "% negative :", num_neg_docs / float(num_docs)
    #print "Number of training documents:", len(train_set)
    #print "Number of test documents:", len(test_set)

    num_features = 0
    num_pos_features = 0
    num_neu_features = 0
    num_neg_features = 0
    for row in feature_list:
        num_features += len(row[0])
        if row[1] == "positive":
            num_pos_features += len(row[0])
        if labels == "pnn":
            if row[1] == "neutral":
                num_neu_features += len(row[0])
        if row[1] == "negative":
            num_neg_features += len(row[0])

    print "Features:"
    print "Avg features / doc :", num_features / float(num_docs)
    print "Avg positive / doc :", num_pos_features / float(num_pos_docs)
    if labels == "pnn":
        print "Avg neutral  / doc :", num_neu_features / float(num_neu_docs)
    print "Avg negative / doc :", num_neg_features / float(num_neg_docs)

def print_multi_confusion_matrix(cc):
    print "\n   \tpos\tneu\tneg"
    print "pos\t",cc["positive"]["positive"],"\t",cc["positive"]["neutral"],"\t",cc["positive"]["negative"]
    print "neu\t",cc["neutral"]["positive"],"\t",cc["neutral"]["neutral"],"\t",cc["neutral"]["negative"]
    print "neg\t",cc["negative"]["positive"],"\t",cc["negative"]["neutral"],"\t",cc["negative"]["negative"]

def print_bi_confusion_matrix(cc):
    print "\n   \tpos\tneg"
    print "pos\t",cc["positive"]["positive"],"\t",cc["positive"]["negative"]
    print "neg\t",cc["negative"]["positive"],"\t",cc["negative"]["negative"]

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
    return(label_stats)

def multi_label_classifier_test(classifier, test_set):
    cm_raw = {
            "positive": {"positive": 0, "neutral": 0, "negative": 0},
            "neutral":  {"positive": 0, "neutral": 0, "negative": 0},
            "negative": {"positive": 0, "neutral": 0, "negative": 0},
            }
    for item, intended_label in test_set:
        result = classifier.classify(item)
        cm_raw[result][intended_label] += 1

    print_multi_confusion_matrix(cm_raw)
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
    print "Accuracy    :\t", nltk.classify.accuracy(classifier, test_set)
    print "Avg Accuracy:\t", aa / 3.0
    print u"Precision\u03BC  :\t", tp_sum / float(tp_sum + fp_sum)
    print u"Recall\u03BC     :\t", tp_sum / float(tp_sum + fn_sum)
    print "Precision M :\t", running_precision / 3.0
    print "Recall M    :\t", running_recall / 3.0

def bi_label_classifier_test(classifier, test_set):
    cm_raw = {
            "positive": {"positive": 0, "negative": 0},
            "negative": {"positive": 0, "negative": 0},
            }
    for item, intended_label in test_set:
        result = classifier.classify(item)
        cm_raw[result][intended_label] += 1
    print_bi_confusion_matrix(cm_raw)

    try:
        precison = cm_raw["positive"]["positive"] / float(cm_raw["positive"]["positive"] + cm_raw["positive"]["negative"])
    except:
        precison = 0.0
    try:
        recall = cm_raw["positive"]["positive"] / float(cm_raw["positive"]["positive"] + cm_raw["negative"]["positive"])
    except:
        recall = 0.0
    try:
        fscore = 2 * ((precison * recall)/(precison + recall))
    except:
        fscore = 0.0

    print "Accuracy  :\t", nltk.classify.accuracy(classifier, test_set)
    print "Precision :\t", precison
    print "Recall    :\t", recall
    print "Fscore    :\t", fscore

def calculate_fscore(classifier, test_set):
    cm_raw = {
            "positive": {"positive": 0, "negative": 0},
            "negative": {"positive": 0, "negative": 0},
            }
    for item, intended_label in test_set:
        result = classifier.classify(item)
        cm_raw[result][intended_label] += 1
    try:
        precison = cm_raw["positive"]["positive"] / \
            float(cm_raw["positive"]["positive"] + cm_raw["positive"]["negative"])
    except:
        precison = 0.0
    try:
        recall = cm_raw["positive"]["positive"] / \
            float(cm_raw["positive"]["positive"] + cm_raw["negative"]["positive"])
    except:
        recall = 0.0
    try:
        fscore = 2 * ((precison * recall)/(precison + recall))
    except:
        fscore = 0.0
    return fscore

