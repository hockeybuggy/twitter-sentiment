
library(ggplot2)

#data <- read.table("box.csv", header=TRUE, col.names=c("y"))
#data <- read.table("box.csv", col.names=c("X", "F"))
data <- read.csv("boxplot.csv", header=TRUE)

print(data)

chart_title <- "Maximum Entropy Classifier Performance"
xlab <- "Experiment"
ylab <- "F-score"
groups <- c("All", "Just Stopwords", "Just Uncommon", "Just Normalization", "Baseline")

cbPalette <- c("#999999", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7")
palette <- c("#999999", "#84B237", "#6E98FF", "#B24932", "#F0E442")

p <- ggplot(data, aes(x=factor(Label), y=F, fill=factor(Label))) + geom_boxplot()
p = p + scale_x_discrete(xlab, labels=groups)
p = p + scale_y_continuous(ylab, limits=c(0.35, 0.55))
p = p + ggtitle(chart_title)
p = p + scale_fill_manual(values=palette, guide=FALSE)
p = p + theme_minimal()

p # Draw that sucker
ggsave("boxplot.png")
