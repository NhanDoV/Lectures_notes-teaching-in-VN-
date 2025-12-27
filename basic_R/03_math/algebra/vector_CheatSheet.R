#=================== Creating Vectors ====================
c(1, 3, 5)              # Create vector
1:7                     # Integer sequence
seq(2, 8, by = 2)       # Sequence with step
rep(c(2, 8), times = 4) # Repeat vector
rep(c(2, 8), each = 3)  # Repeat each element

#=================== Vector Functions ====================
sort(my_vector)         # Sort vector
rev(my_vector)          # Reverse order
table(my_vector)        # Count values
unique(my_vector)       # Unique values

#=================== Selecting Elements ====================
my_vector[6]            # 6th element
my_vector[-6]           # All except 6th
my_vector[2:6]          # Elements 2 to 6
my_vector[-(2:6)]       # Exclude 2 to 6
my_vector[c(2, 6)]      # Elements 2 and 6

#=================== Logical Subsetting ====================
my_vector[my_vector == 5]
my_vector[my_vector < 5]
my_vector[my_vector %in% c(2, 5, 8)]