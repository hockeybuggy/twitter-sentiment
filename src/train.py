#!/usr/bin/env python

import nltk
import numpy
import statsify

from nltk.featstruct import FeatStruct
from nltk.classify.maxent import CutoffChecker, BinaryMaxentFeatureEncoding, calculate_empirical_fcount
from nltk.classify.maxent import calculate_nfmap, ConditionalExponentialClassifier, log_likelihood, accuracy
from nltk.classify.maxent import calculate_deltas

class classifier:
    def __init__(self, train_set):
        pass

    def test(self, test_set, labels):
        if labels == "pnn":
            statsify.multi_label_classifier_test(self.classifier, test_set)
        else:
            statsify.bi_label_classifier_test(self.classifier, test_set)

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
    def __init__(self, train_set, iterations=None, lldelta=None, ll=None):
        if lldelta:
            print "Cutoff after log likelyhood changes by less than", lldelta
            self.classifier = nltk.MaxentClassifier.train(train_set, min_lldelta=lldelta)
        elif ll:
            print "Cutoff after log likelyhood reaches", ll
            self.classifier = nltk.MaxentClassifier.train(train_set, min_ll=ll)
        else:
            if not iterations:
                iterations = 25
            print "Cutoff after {} iterations".format(iterations)
            self.classifier = nltk.MaxentClassifier.train(train_set, max_iter=iterations)

def train_maxent_classifier_with_iis_with_validation(train_toks, prev_weights=None, trace=3, encoding=None,
                                     labels=None, **cutoffs):
    """
    Derived from train_maxent_classifier_with_iis
    """
    cutoffs.setdefault('max_iter', 100)
    cutoffchecker = CutoffChecker(cutoffs)

    # Construct an encoding from the training data.
    if encoding is None:
        encoding = BinaryMaxentFeatureEncoding.train(train_toks, labels=labels)

    # Count how many times each feature occurs in the training data.
    empirical_ffreq = (calculate_empirical_fcount(train_toks, encoding) /
                       len(train_toks))

    # Find the nf map, and related variables nfarray and nfident.
    # nf is the sum of the features for a given labeled text.
    # nfmap compresses this sparse set of values to a dense list.
    # nfarray performs the reverse operation.  nfident is
    # nfarray multiplied by an identity matrix.
    nfmap = calculate_nfmap(train_toks, encoding)
    nfarray = numpy.array(sorted(nfmap, key=nfmap.__getitem__), 'd')
    nftranspose = numpy.reshape(nfarray, (len(nfarray), 1))

    # Check for any features that are not attested in train_toks.
    unattested = set(numpy.nonzero(empirical_ffreq==0)[0])

    # Build the classifier.  Start with weight=0 for each attested
    # feature, and weight=-infinity for each unattested feature.
    if prev_weights == None:
        weights = numpy.zeros(len(empirical_ffreq), 'd')
        for fid in unattested: weights[fid] = numpy.NINF
    else:
        weights = prev_weights
    classifier = ConditionalExponentialClassifier(encoding, weights)

    if trace > 0: print('  ==> Training (%d iterations)' % cutoffs['max_iter'])
    if trace > 2:
        print()
        print('      Iteration    Log Likelihood    Accuracy')
        print('      ---------------------------------------')

    # Old log-likelihood and accuracy; used to check if the change
    # in log-likelihood or accuracy is sufficient to indicate convergence.
    ll_old = None
    acc_old = None

    # Train the classifier.
    try:
        while True:
            if trace > 2:
                ll = cutoffchecker.ll or log_likelihood(classifier, train_toks)
                acc = cutoffchecker.acc or accuracy(classifier, train_toks)
                iternum = cutoffchecker.iter
                print('     %9d    %14.5f    %9.3f' % (iternum, ll, acc))

            # Calculate the deltas for this iteration, using Newton's method.
            deltas = calculate_deltas(
                train_toks, classifier, unattested, empirical_ffreq,
                nfmap, nfarray, nftranspose, encoding)

            # Use the deltas to update our weights.
            weights = classifier.weights()
            weights += deltas
            classifier.set_weights(weights)

            # Check the log-likelihood & accuracy cutoffs.
            if cutoffchecker.check(classifier, train_toks):
                break

    except KeyboardInterrupt:
        print('      Training stopped: keyboard interrupt')
    except:
        raise

    if trace > 2:
        ll = log_likelihood(classifier, train_toks)
        acc = accuracy(classifier, train_toks)
        print('         Final    %14.5f    %9.3f' % (ll, acc))
    # Return the classifier.
    return classifier

class multi_label_classifier_with_validation(classifier):
    def __init__(self, train_set, validation_set, accuracy_delta_cutoff):
        print "Cutoff after validation set reaches {}% accuracy".format(accuracy_delta_cutoff)
        self.classifier = nltk.MaxentClassifier.train(train_set, trace=1, max_iter=5)
        iter_count = 0
        prev_accuracy = 0.0
        accuracy = nltk.classify.accuracy(self.classifier, validation_set)
        print "Iteration {} Accuracy  :\t{}".format(iter_count, accuracy)
        #while accuracy < accuracy_cutoff and iter_count > 20:
        while (accuracy - prev_accuracy) > accuracy_delta_cutoff:
            iter_count += 1
            prev_weights = self.classifier.weights()
            self.classifier = train_maxent_classifier_with_iis_with_validation(train_set, trace=1, prev_weights=prev_weights, max_iter=1)
            prev_accuracy = accuracy
            accuracy = nltk.classify.accuracy(self.classifier, validation_set)
            print "Iteration {} Accuracy  :\t{}".format(iter_count, accuracy)
            print "Accuracy delta  :\t{}".format(accuracy - prev_accuracy)

    #def train_with_validation(train_toks, max_iter=5):


class multi_label_naive_bayes_classifier(classifier):
    def __init__(self, train_set):
        self.classifier = nltk.NaiveBayesClassifier.train(train_set)

