
library(ggplot2)

data <- read.table("features.tsv", col.names=c("y", "x"), sep="\t")

chart_title <- "Histogram of Term Occurrences"
xlab <- "Term Rank"
ylab <- "Document Frequency"

ggplot(data, aes(x)) + geom_histogram(binwidth=0.2) + scale_x_log10(breaks=c(1,2,5,10,100,1000)) + ggtitle(chart_title) + xlab(xlab) + ylab(ylab) + theme_minimal()

