import numpy

from nltk.classify.maxent import CutoffChecker, BinaryMaxentFeatureEncoding
from nltk.classify.maxent import calculate_nfmap, ConditionalExponentialClassifier
from nltk.classify.maxent import calculate_deltas, log_likelihood, accuracy
from nltk.classify.maxent import calculate_empirical_fcount

def train_maxent_classifier_with_validation(train_toks, prev_weights=None,
        trace=3, encoding=None, labels=None, **cutoffs):
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

