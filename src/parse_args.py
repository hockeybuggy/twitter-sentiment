#!/usr/bin/env python

# File       : parse_args.py
# Author     : Douglas Anderson
# Description: Command line options for argument parseing

import argparse

def parse_args():
    classifier_types = ["max_ent", "bayes"]
    valid_fold_numbers = [5, 10]
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
    parser.add_argument("--validation_metric", default="none",
            help="This changes the metric for validation set evaluation")
    parser.add_argument("--df-cutoff", type=int, default=1,
            help="This parameter changes the document frequency cutoff")
    parser.add_argument("--num-folds", type=int, default=5,
            help="This parameter changes number of folds for cross-validation")

    parser.add_argument("--no-uncommon-selection", dest="uncommon_selection",
            action="store_false", help="This toggles whither word selection is on off")
    parser.add_argument("--no-stopword-removal", dest="stopword_removal",
            action="store_false", help="This toggles whither stopword removal is on off")

    parser.add_argument("--no-normalize", dest="normalize",
            action="store_false", help="This toggles whither anything is normalized")
    parser.add_argument("--no-normalize-words", dest="normalize_words",
            action="store_false", help="This toggles whither words are normalized")
    parser.add_argument("--no-normalize-punct", dest="normalize_punct",
            action="store_false", help="This toggles whither words are normalized")
    parser.add_argument("--no-normalize-emoticons", dest="normalize_emoticons",
            action="store_false", help="This toggles whither words are normalized")
    parser.add_argument("--no-normalize-users", dest="normalize_users",
            action="store_false", help="This toggles whither users are normalized")
    parser.add_argument("--no-normalize-hashtags", dest="normalize_hashtags",
            action="store_false", help="This toggles whither hashtags are normalized")
    parser.add_argument("--no-normalize-nums", dest="normalize_nums",
            action="store_false", help="This toggles whither nums are normalized")
    parser.add_argument("--no-normalize-urls", dest="normalize_urls",
            action="store_false", help="This toggles whither urls are normalized")

    parser.add_argument("--classifier_type", default="max_ent",
            help="Select classifier should be:" + " ".join(classifier_types))
    parser.add_argument("--labels", default="pn",
            help="Which labels should be:" + " ".join(labels))
    args = parser.parse_args()
    if args.classifier_type not in classifier_types:
        raise Exception("Classifier type must be one of: " + " ".join(classifier_types))
    if args.labels not in labels:
        raise Exception("Labels must be one of: " + " ".join(labels))
    if args.validation_metric not in val_metrics:
        raise Exception("Validation metrics must be one of: " + " ".join(val_metrics))
    if args.num_folds not in valid_fold_numbers :
        raise Exception("Validation metrics must be one of: " + " ".join(val_metrics))
    return args

