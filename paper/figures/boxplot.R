
library(ggplot2)

#data <- read.table("box.csv", header=TRUE, col.names=c("y"))
#data <- read.table("box.csv", col.names=c("X", "F"))
data <- read.csv("boxplot.csv", header=TRUE)

print(data)

chart_title <- "Classifier Performance"
xlab <- "Experiment"
ylab <- "F-score"

p <- ggplot(data, aes(x=factor(Label), y=F)) + geom_boxplot()
p = p + scale_x_discrete("Labels", labels=c("A", "B"))
p = p + ylim(c(0.25,0.75))
p = p + ggtitle(chart_title)
p = p + xlab(xlab)
p = p + ylab(ylab)
p = p + theme_minimal()
p # Draw that sucker
