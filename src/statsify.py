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

def print_multi_confusion_matrix(cm):
    pos = "positive"
    neu = "neutral"
    neg = "negative"
    print "\n   \tpos\tneu\tneg"
    print "pos\t",cm[pos][pos],"\t",cm[pos][neu],"\t",cm[pos][neg]
    print "neu\t",cm[neu][pos],"\t",cm[neu][neu],"\t",cm[neu][neg]
    print "neg\t",cm[neg][pos],"\t",cm[neg][neu],"\t",cm[neg][neg]

def print_bi_confusion_matrix(cm):
    print "\n   \tpos\tneg"
    print "pos\t",cm["positive"]["positive"],"\t",cm["positive"]["negative"]
    print "neg\t",cm["negative"]["positive"],"\t",cm["negative"]["negative"]


def calculate_metrics(classifier, test_set, trace=True):
    cm = {
            "positive": {"positive": 0, "neutral": 0, "negative": 0},
            "neutral":  {"positive": 0, "neutral": 0, "negative": 0},
            "negative": {"positive": 0, "neutral": 0, "negative": 0},
            }
    stats = {
            "accuracy": 0.0,
            "posP": 0.0,
            "posR": 0.0,
            "negP": 0.0,
            "negR": 0.0,
            "Fpos": 0.0,
            "Fneg": 0.0,
            "F": 0.0
            }

    # Test how the classifier does
    for item, intended_label in test_set:
        result = classifier.classify(item)
        cm[result][intended_label] += 1

    if trace:
        print_multi_confusion_matrix(cm)

    stats["accuracy"] = nltk.classify.accuracy(classifier, test_set)

    # The following strings help make the precision and recall calculations shorter
    pos = "positive"
    neu = "neutral"
    neg = "negative"
    # Calculate Precision and Recall
    try:
        stats["posP"] = cm[pos][pos] / float(cm[pos][pos] + cm[pos][neu] + cm[pos][neg])
    except ZeroDivisionError:
        pass
    try:
        stats["posR"] = cm[pos][pos] / float(cm[pos][pos] + cm[neu][pos] + cm[neg][pos])
    except ZeroDivisionError:
        pass
    try:
        stats["negP"] = cm[neg][neg] / float(cm[neg][pos] + cm[neg][neu] + cm[neg][neg])
    except ZeroDivisionError:
        pass
    try:
        stats["negR"] = cm[neg][neg] / float(cm[pos][neg] + cm[neg][neg] + cm[neg][neg])
    except ZeroDivisionError:
        pass

    # Calculate Fpositive and Fnegative
    try:
        stats["Fpos"] = 2 * ((stats["posP"] * stats["posR"])/(stats["posP"] + stats["posR"]))
    except ZeroDivisionError:
        pass
    try:
        stats["Fneg"] = 2 * ((stats["negP"] * stats["negR"])/(stats["negP"] + stats["negR"]))
    except ZeroDivisionError:
        pass
    # Average the two F scores
    stats["F"] = (stats["Fpos"] + stats["Fneg"]) / 2.0

    if trace:
        print "Accuracy:\t", stats["accuracy"]
        print "Pos P   :\t", stats["posP"]
        print "Pos R   :\t", stats["posR"]
        print "Neg P   :\t", stats["negP"]
        print "Neg R   :\t", stats["negP"]
        print "F pos   :\t", stats["Fpos"]
        print "F neg   :\t", stats["Fneg"]
        print "Fscore  :\t", stats["F"]
    #return stats["F"]
    return stats

def calculate_fscore(classifier, test_set):
    x = calculate_metrics(classifier, test_set, trace=False)["F"]
    print "x:", x
    return x


