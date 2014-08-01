#!/usr/bin/env python

# File       : conductor.py
# Author     : Douglas Anderson
# Description: Simple driver for sentiment analysis implementation

import os, sys

import tokenize
import normalize
import labelselect
import statsify
import wordselection
import dictizer
import split_dataset
from Token import Token
from parse_args import parse_args
from train import maxent_classifier
from train import maxent_classifier_with_validation
from train import naive_bayes_classifier


if __name__ == "__main__":
    args = parse_args()
    print "Opening dataset..."
    tokens = tokenize.open_tweets_file("../data/b.2.tsv", 0, args.items)

    print "Selecting labels..."
    tokens = labelselect.__call__(tokens, args.labels) # Select only the labels

    print "Normalizing dataset..."
    #tokens = normalize.__call__(tokens) # Normalize the tokens
    if args.normalize and args.normalize_words:
        normalize.normalize_words(tokens)
    if args.normalize and args.normalize_punct:
        normalize.normalize_punct(tokens)
    if args.normalize and args.normalize_emoticons:
        normalize.normalize_emoticons(tokens)
    if args.normalize and args.normalize_users:
        normalize.normalize_users(tokens)
    if args.normalize and args.normalize_hashtags:
        normalize.normalize_hashtags(tokens)
    if args.normalize and args.normalize_nums:
        normalize.normalize_nums(tokens)
    if args.normalize and args.normalize_urls:
        normalize.normalize_urls(tokens)

    print "Transforming dataset..."
    feature_list = dictizer.__call__(tokens)

    docfreq = wordselection.calculate_docfreq(feature_list)

    if args.stopword_removal:
        print "Removing stopwords from the dataset..."
        feature_list = wordselection.remove_stopwords(feature_list)

    if args.uncommon_selection:
        print "Removing uncommon words from the dataset..."
        feature_list = wordselection.remove_uncommon(feature_list, docfreq, args.df_cutoff)

    wordselection.print_reatined_features(docfreq, args.df_cutoff)

    # Write the features out to a file
    with open("filtered_docs.txt", "w") as w:
        for row in feature_list:
            w.write(str(row[0]) + "\n")

    print "Generating feature set statistics..."
    statsify.__call__(feature_list, args.labels)

    print "Splitting the dataset..."
    if args.validation_metric == "none":
        train_set, _, test_set = split_dataset.__call__(feature_list, 0.2)
    else:
        train_set, validation_set, test_set = split_dataset.__call__(feature_list, 0.2, validation_size=0.2)

    if args.classifier_type == "max_ent":
        if args.minlldelta:
            classifier = maxent_classifier(train_set, lldelta=args.minlldelta)
        elif args.minll:
            classifier = maxent_classifier(train_set, ll=args.minll)
        elif args.validation_metric != "none":
            classifier = maxent_classifier_with_validation(train_set, validation_set,
                    args.validation_metric, 3)
        elif args.numIterations:
            classifier = maxent_classifier(train_set, iterations=args.numIterations)
        else:
            print "Error no cut off set"
            sys.exit(0)
    else:
        classifier = naive_bayes_classifier(train_set)

    print "\nTesting"
    classifier.test(test_set, args.labels)

    classifier.show_informitive_features(30)
    #classifier.inspect_errors(test_set)

