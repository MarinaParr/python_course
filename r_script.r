setwd("~/PycharmProjects/untitled")
#files <- (Sys.glob("*_rev_tab_hb_trace.dat"))
#lapply(files, plotting())
#plotting <- function(file):
file <- "42_outer__rev_tab_hb_trace.dat"
  data <- read.table(file)
  rnames <- data[,1]
  data <- data.matrix(data[-1])
  cnames <- seq(0,ncol(data)*20,20)
  "nba_heatmap.png" <- heatmap(data, Rowv=NA, Colv=NA, scale="column", margins=c(5,10), 
                       labRow = rnames, labCol = cnames, 
                       xlab = "Time, ns", ylab = "Names of interations")
  dev.copy(png,"nba_heatmap.png")
  dev.off()
