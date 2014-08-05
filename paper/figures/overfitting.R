
library(ggplot2)

xlab <- "Number of Iterations"
ylab <- "F-score"


## Maxent boxplot
data <- read.csv("overfitting.csv", header=TRUE)

chart_title <- "Maximum Entropy Classifier Performance"

p <- ggplot(data, aes(x=NumIter, y=F)) + geom_point()
p = p + geom_smooth(method="loess")
p = p + scale_x_continuous(xlab)
p = p + scale_y_continuous(ylab, limits=c(0.35, 0.55))
p = p + ggtitle(chart_title)
#p = p + scale_fill_manual(values=palette, guide=FALSE)
p = p + theme_minimal()

p # Draw that sucker
ggsave("overfitting.png")

