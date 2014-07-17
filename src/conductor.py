#!/usr/bin/env python

# File       : conductor.py
# Author     : Douglas Anderson
# Description: Driver for my parser implementation

import os, sys
import argparse
import math

import tokenize
import normalize
import labelselect
import statsify
import wordselection
import dictizer
from Token import Token
from train import multi_label_classifier, multi_label_naive_bayes_classifier

def parse_args():
    parser = argparse.ArgumentParser(description="Scan a tweet to determine it's tokens")
    parser.add_argument("--file", type=str, help="The file name containing the text to be scanned")
    parser.add_argument("items", type=int, help="The number of items to use")
    parser.add_argument("--minlldelta", type=float, help="This parameter changes the cutoff of training for max ent ")
    parser.add_argument("--minll", type=float, help="This parameter changes the cutoff for training for max ent ")
    parser.add_argument("--classifier_type", default="max_ent", help="Select classifer should be: max_ent, naive_bayes")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    print "Opening dataset..."
    tokens = tokenize.open_tweets_file("../data/b.tsv", 0, args.items)

    print "Selecting labels..."
    tokens = labelselect.__call__(tokens) # Select only the labels


    print "Normalizing dataset..."
    tokens = normalize.__call__(tokens) # Normalize the tokens
    #for token in tokens:
        #print token.__unicode__()

    print "Transforming dataset..."
    feature_list = dictizer.__call__(tokens)

    print "Selecting features from the dataset..."
    feature_list = wordselection.__call__(feature_list)

    split_point = int(math.ceil(len(feature_list) * 0.8))
    train_set = feature_list[:split_point]
    test_set = feature_list[split_point:]

    # Write the features out to a file
    with open("filtered_docs.txt", "w") as w:
        for row in feature_list:
            w.write(str(row[0]) + "\n")

    # Count the document by label
    num_docs = len(feature_list)
    num_pos_docs = len([x for x in feature_list if x[1] == "positive"])
    num_neu_docs = len([x for x in feature_list if x[1] == "neutral"])
    num_neg_docs = len([x for x in feature_list if x[1] == "negative"])

    print "Total number of documents:", num_docs
    print "% positive :", num_pos_docs / float(num_docs)
    print "% neutral  :", num_neu_docs / float(num_docs)
    print "% negative :", num_neg_docs / float(num_docs)
    print "Number of training documents:", len(train_set)
    print "Number of test documents:", len(test_set)

    num_features = 0
    num_pos_features = 0
    num_neu_features = 0
    num_neg_features = 0
    for row in feature_list:
        num_features += len(row[0])
        if row[1] == "positive":
            num_pos_features += len(row[0])
        if row[1] == "neutral":
            num_neu_features += len(row[0])
        if row[1] == "negative":
            num_neg_features += len(row[0])

    print "Features:"
    print "Avg features / doc :", num_features / float(num_docs)
    print "Avg positive / doc :", num_pos_features / float(num_pos_docs)
    print "Avg neutral  / doc :", num_neu_features / float(num_neu_docs)
    print "Avg negative / doc :", num_neg_features / float(num_neg_docs)

    if args.classifier_type == "max_ent":
        if args.minlldelta:
            classifier = multi_label_classifier(train_set, lldelta=args.minlldelta)
        elif args.minll:
            classifier = multi_label_classifier(train_set, ll=args.minll)
        else:
            classifier = multi_label_classifier(train_set)
    else:
        classifier = multi_label_naive_bayes_classifier(train_set)

    #classifier.show_informitive_features()
    print "\nTesting"
    classifier.test(test_set)
    #classifier.inspect_errors(test_set)

