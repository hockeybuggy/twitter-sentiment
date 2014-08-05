
all: feature_hist boxplot overfitting

feature_hist: features.tsv
	R < feature_hist.R --no-save

boxplot: maxent_boxplot.csv bayes_boxplot.csv
	R < boxplot.R --no-save

overfitting: overfitting.csv
	R < overfitting.R --no-save

