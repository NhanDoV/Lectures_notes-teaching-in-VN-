# References: https://www.datacamp.com/cheat-sheet/getting-started-r

library(dplyr)

# ================================
# 1. Getting started
# ================================
# Create a data frame
df <- data.frame(
  x = 1:3,
  y = c("a", "b", "c"),
  z = 12:14
)

# This selects all columns of the third row
df[3, ]

# This selects the column y
df$y

# This selects all rows of the second column
df[, 2]

# This selects the third column of the second row
df[2, 3]

# ================================
# 2. Manipulating dataframe
# ================================

# --- bind_cols ---
df1 <- data.frame(id = 1:3)
df2 <- data.frame(score = c(80, 90, 85))

bind_cols(df1, df2)

# --- bind_rows ---
df1 <- data.frame(id = 1:2, score = c(70, 75))
df2 <- data.frame(id = 3:4, score = c(80, 85))

bind_rows(df1, df2)

# --- filter ---
df <- data.frame(
  x = 1:5,
  y = c("a", "b", "a", "b", "a")
)

filter(df, x == 2)

# --- distinct ---
df <- data.frame(
  z = c(1, 1, 2, 2, 3),
  x = c(10, 10, 20, 20, 30)
)

distinct(df, z)

# --- slice ---
df <- data.frame(
  x = 1:30,
  y = rnorm(30)
)

slice(df, 10:15)

# --- slice_max ---
df <- data.frame(
  name = c("A", "B", "C", "D"),
  z = c(10, 40, 20, 30)
)

slice_max(df, z, prop = 0.25)

# --- pull ---
df <- data.frame(
  x = 1:3,
  y = c("apple", "banana", "cherry")
)

pull(df, y)

# --- select ---
df <- data.frame(
  x = 1:3,
  y = c("a", "b", "c"),
  z = c(100, 200, 300)
)

select(df, x, y)

# --- relocate ---
df <- data.frame(
  x = 1:3,
  y = c("a", "b", "c"),
  z = c(100, 200, 300)
)

relocate(df, x, .after = last_col())

# --- rename ---
df <- data.frame(
  x = 1:3,
  z = c(20, 30, 40)
)

rename(df, age = z)

# --- arrange ---
df <- data.frame(
  x = c(5, 2, 8, 1),
  y = c("a", "b", "c", "d")
)

arrange(df, desc(x))

# --- summarise ---
df <- data.frame(
  x = c(10, 20, 30)
)

summarise(df, total = sum(x))

# --- group_by + summarise ---
df <- data.frame(
  z = c("A", "A", "B", "B"),
  x = c(10, 20, 30, 40)
)

df %>%
  group_by(z) %>%
  summarise(total = sum(x))