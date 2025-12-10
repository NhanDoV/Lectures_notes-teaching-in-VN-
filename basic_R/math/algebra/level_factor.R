# Write a R program to find the levels of factor of a given vector.

find_factor_levels <- function(v) {
    # Print original vector
    print("Original vector:")
    print(v)

    # Print levels
    print("Levels of factor of the said vector:")
    print(levels(factor(v)))
}

# ---- TEST ----
# Create a vector 'v' with values including some repeated numbers and NA values
v <- c(1, 2, 3, 3, 4, NA, 3, 2, 4, 5, NA, 5)
find_factor_levels(v)