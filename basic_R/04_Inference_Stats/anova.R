library(tidyverse)

anova_df <- function(fpath = "data.csv", col1, col2) {

    # --- 1. Read CSV file ---
    df <- read.csv(fpath)

    # --- 2. Select the two chosen columns ---
    X1 <- df[[col1]]
    X2 <- df[[col2]]

    # --- 3. Combine into long format ---
    long_df <- data.frame(
        value = c(X1, X2),
        feature = factor(rep(c(col1, col2), each = nrow(df)))
    )

    # --- 4. Run ANOVA ---
    anova_result <- aov(value ~ feature, data = long_df)

    # --- 5. Return summary ---
    return(summary(anova_result))
}

# Usage
anova_df("students.csv", "height", "weight")