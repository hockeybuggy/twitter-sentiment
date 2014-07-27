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
from train import maxent_classifier
from train import maxent_classifier_with_validation
from train import naive_bayes_classifier

def parse_args():
    classifier_types = ["max_ent", "bayes"]
    labels = ["pn", "pnn"]
    val_metrics = ["none", "accuracy", "fscore"]
    parser = argparse.ArgumentParser(description="Scan a tweet to determine it's tokens")
    parser.add_argument("--file", type=str,
            help="The file name containing the text to be scanned")
    parser.add_argument("items", type=int, help="The number of items to use")
    parser.add_argument("--minlldelta", type=float,
            help="This parameter changes the cutoff of training for max ent ")
    parser.add_argument("--minll", type=float,
            help="This parameter changes the cutoff for training for max ent ")
    parser.add_argument("--numIterations", type=int,
            help="This parameter changes the cutoff for training for max ent ")
    parser.add_argument("--validationMetric", default="none",
            help="This changes the metric for validation set evaluation")
    parser.add_argument("--no-uncommon-selection", dest="uncommon_selection",
            action="store_false", help="This toggles whither word selection is on off")
    parser.add_argument("--no-stopword-removal", dest="stopword_removal",
            action="store_false", help="This toggles whither stopword removal is on off")
    parser.add_argument("--classifier_type", default="max_ent",
            help="Select classifier should be:" + " ".join(classifier_types))
    parser.add_argument("--labels", default="pn",
            help="Which labels should be:" + " ".join(labels))
    args = parser.parse_args()
    if args.classifier_type not in classifier_types:
        raise Exception("Classifier type must be one of: " + " ".join(classifier_types))
    if args.labels not in labels:
        raise Exception("Labels must be one of: " + " ".join(labels))
    if args.validationMetric not in val_metrics:
        raise Exception("Validation metrics must be one of: " + " ".join(val_metrics))
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

    if args.stopword_removal:
        print "Removing stopwords from the dataset..."
        feature_list = wordselection.remove_uncommon(feature_list)

    if args.uncommon_selection:
        print "Removing uncommon words from the dataset..."
        feature_list = wordselection.remove_stopwords(feature_list)

    # Write the features out to a file
    with open("filtered_docs.txt", "w") as w:
        for row in feature_list:
            w.write(str(row[0]) + "\n")

    print "Generating feature set statistics..."
    statsify.__call__(feature_list, args.labels)

    print "Splitting the dataset..."
    if args.validationMetric == "none":
        train_set, _, test_set = split_dataset.__call__(feature_list, 0.2)
    else:
        train_set, validation_set, test_set = split_dataset.__call__(feature_list, 0.2, validation_size=0.2)

    if args.classifier_type == "max_ent":
        if args.minlldelta:
            classifier = maxent_classifier(train_set, lldelta=args.minlldelta)
        elif args.minll:
            classifier = maxent_classifier(train_set, ll=args.minll)
        elif args.validationMetric != "none":
            classifier = maxent_classifier_with_validation(train_set, validation_set,
                    args.validationMetric, 3)
        elif args.numIterations:
            classifier = maxent_classifier(train_set, iterations=args.numIterations)
        else:
            print "Error no cut off set"
            sys.exit(0)
    else:
        classifier = naive_bayes_classifier(train_set)

    print "\nTesting"
    classifier.test(test_set, args.labels)

    #classifier.show_informitive_features(30)
    #classifier.inspect_errors(test_set)

