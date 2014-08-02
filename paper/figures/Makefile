
all: feature_hist boxplot

feature_hist: features.tsv
	R < feature_hist.R --no-save

boxplot: features.tsv
	R < boxplot.R --no-save

