library(ggplot2)
library(reshape2)
library(scales)
#library(devtools)

#devtools::install_github('cttobin/ggthemr')

history.data <- read.csv(file = "history.csv", sep = ";")
history.data <- head(history.data, 30)

data <- melt(history.data, id="Iteration")
p <- ggplot(data=data, aes(x=Iteration, y=value, colour=variable)) 
p <- p + labs(colour = "Users")
p <- p + geom_line() 
p <- p + geom_point()
p <- p + scale_x_continuous(breaks = pretty_breaks())
p <- p + labs(title="PageRank growth over time", x = "Iteration", y = "PageRank")
p <- p + theme_light()

p
