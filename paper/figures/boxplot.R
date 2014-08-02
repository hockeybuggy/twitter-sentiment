
library(ggplot2)

#data <- read.table("box.csv", header=TRUE, col.names=c("y"))
#data <- read.table("box.csv", col.names=c("X", "F"))
data <- read.csv("boxplot.csv", header=TRUE)

print(data)

chart_title <- "Maximum Entropy Classifier Performance"
xlab <- "Experiment"
ylab <- "F-score"
groups <- c("All", "Just Stopwords", "Just Uncommon", "Just Normalization", "Baseline")

p <- ggplot(data, aes(x=factor(Label), y=F)) + geom_boxplot()
p = p + scale_x_discrete(xlab, labels=groups)
p = p + scale_y_continuous(ylab, limits=c(0.30, 0.60))
p = p + ggtitle(chart_title)
p = p + theme_minimal()
p # Draw that sucker
