#=================== Arithmetic Operators ====================
a + b     # Sum
a - b     # Subtraction
a * b     # Multiplication
a / b     # Division
a ^ b     # Exponentiation
a %% b    # Remainder
a %/% b   # Integer division

#=================== Relational Operators ====================
a == b    # Equal
a != b    # Not equal
a > b     # Greater than
a < b     # Less than
a >= b    # Greater than or equal
a <= b    # Less than or equal

#=================== Logical Operators ====================
!a        # NOT
a & b     # Element-wise AND
a && b    # AND (first element only)
a | b     # Element-wise OR
a || b    # OR (first element only)

#=================== Assignment Operators ====================
x <- 1    # Assign 1 to x
x = 1     # Assign 1 to x (alternative)

#=================== Other Operators ====================
x %in% c(1, 2, 3)   # Check membership
df$column           # Access column in object
x %>% mean()        # Pipe operator (magrittr)