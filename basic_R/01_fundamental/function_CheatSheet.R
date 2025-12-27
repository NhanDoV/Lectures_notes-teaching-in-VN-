#=================== Accessing Help ====================
?max          # Help for max function
?tidyverse    # Help for tidyverse package
??"max"       # Search documentation related to "max"

#=================== Object Inspection ====================
str(my_df)    # Structure of object
class(my_df)  # Class of object

#=================== Packages ====================
install.packages("tidyverse")  # Install package
library(tidyverse)             # Load package

#=================== Working Directory ====================
getwd()                         # Get current working directory
setwd("C://file/path")          # Set working directory

#=================== Math Functions ====================
log(x)        # Logarithm
exp(x)        # Exponential
max(x)        # Maximum
min(x)        # Minimum
mean(x)       # Mean
sum(x)        # Sum
median(x)     # Median
quantile(x)   # Quantiles
round(x, 2)   # Round decimals
rank(x)       # Rank values
signif(x, 3)  # Significant figures
var(x)        # Variance
sd(x)         # Standard deviation
cor(x, y)     # Correlation