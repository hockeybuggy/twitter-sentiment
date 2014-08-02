
library(ggplot2)

xlab <- "Experiment"
ylab <- "F-score"
groups <- c("All", "Just Stopwords", "Just Uncommon", "Just Normalization", "Baseline")
palette <- c("#999999", "#84B237", "#6E98FF", "#B24932", "#F0E442")


## Maxent boxplot
data <- read.csv("maxent_boxplot.csv", header=TRUE)

chart_title <- "Maximum Entropy Classifier 5-fold Performance"

p <- ggplot(data, aes(x=factor(Label), y=F, fill=factor(Label))) + geom_boxplot()
p = p + scale_x_discrete(xlab, labels=groups)
p = p + scale_y_continuous(ylab, limits=c(0.35, 0.55))
p = p + ggtitle(chart_title)
p = p + scale_fill_manual(values=palette, guide=FALSE)
p = p + theme_minimal()

p # Draw that sucker
ggsave("maxent_boxplot.png")


## Naive Bayes boxplot
data <- read.csv("bayes_boxplot.csv", header=TRUE)

chart_title <- "Naive Bayes Classifier 5-fold Performance"

p <- ggplot(data, aes(x=factor(Label), y=F, fill=factor(Label))) + geom_boxplot()
p = p + scale_x_discrete(xlab, labels=groups)
p = p + scale_y_continuous(ylab, limits=c(0.35, 0.55))
p = p + ggtitle(chart_title)
p = p + scale_fill_manual(values=palette, guide=FALSE)
p = p + theme_minimal()

p # Draw that sucker
ggsave("bayes_boxplot.png")

