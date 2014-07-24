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
import split_dataset
from Token import Token
from train import multi_label_classifier, multi_label_naive_bayes_classifier

def parse_args():
    classifier_types = ["max_ent", "bayes"]
    labels = ["pn", "pnn"]
    parser = argparse.ArgumentParser(description="Scan a tweet to determine it's tokens")
    parser.add_argument("--file", type=str,
            help="The file name containing the text to be scanned")
    parser.add_argument("items", type=int, help="The number of items to use")
    parser.add_argument("--minlldelta", type=float,
            help="This parameter changes the cutoff of training for max ent ")
    parser.add_argument("--minll", type=float,
            help="This parameter changes the cutoff for training for max ent ")
    parser.add_argument("--classifier_type", default="max_ent",
            help="Select classifer should be:" + " ".join(classifier_types))
    parser.add_argument("--labels", default="pn",
            help="Which labels should be:" + " ".join(labels))
    args = parser.parse_args()
    if args.classifier_type not in classifier_types:
        raise Exception("Classifier type must be one of: " + " ".join(classifier_types))
    if args.labels not in labels:
        raise Exception("Labels must be one of: " + " ".join(labels))
    return args

if __name__ == "__main__":
    args = parse_args()
    print "Opening dataset..."
    tokens = tokenize.open_tweets_file("../data/b.2.tsv", 0, args.items)

    print "Selecting labels..."
    tokens = labelselect.__call__(tokens, args.labels) # Select only the labels

    print "Normalizing dataset..."
    tokens = normalize.__call__(tokens) # Normalize the tokens

    print "Transforming dataset..."
    feature_list = dictizer.__call__(tokens)

    print "Selecting features from the dataset..."
    feature_list = wordselection.__call__(feature_list)

    print "Splitting the dataset..."
    train_set, test_set = split_dataset.__call__(feature_list, 0.2)

    # Write the features out to a file
    with open("filtered_docs.txt", "w") as w:
        for row in feature_list:
            w.write(str(row[0]) + "\n")

    print "Generating feature set statistics..."
    statsify.__call__(feature_list, args.labels)

    if args.classifier_type == "max_ent":
        if args.minlldelta:
            classifier = multi_label_classifier(train_set, lldelta=args.minlldelta)
        elif args.minll:
            classifier = multi_label_classifier(train_set, ll=args.minll)
        else:
            classifier = multi_label_classifier(train_set)
    else:
        classifier = multi_label_naive_bayes_classifier(train_set)

    print "\nTesting"
    classifier.test(test_set, args.labels)
    #classifier.show_informitive_features()
    #classifier.inspect_errors(test_set)

