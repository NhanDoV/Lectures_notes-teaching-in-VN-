# =======================================================================================================
#          					Mathematical functions
# =======================================================================================================
x <- c(1.1, -2.3, -4.5, 5.2, -1.6)
y <- c(2.4,-44, -2.2)

# Rounded value of x
round(x)

# Rounded absolute value of x
round(abs(x))

# Sum of Rounded absolute value of x
sum(round(abs(x)))

# Average of the rounded absolute values of x and y
mean(c(
  sum(round(abs(x))),
  sum(round(abs(y)))
  ))

# =======================================================================================================
seq(8, 2, by=-2) # a sequence from 8 till 2 (inclusive) with a decrement step of 2

rep(seq(8, 2, by=-2), times=2) # repeat it 2 times

# list with a boolean value, a string, and a sorted integer vector.
list_define <- list(log = TRUE,                              # boolean.val (log is a logical operator)
                    ch = "Con_di_me_thang_loz_Tô_Lâm",       # string
                    int_vec = sort(rep(seq(8, 2, by = -2),   # sorted-integer
                                       times = 2)))          # which duplicated 2 times
list_define

is.list(list_define) #returns TRUE if the argument passed is a list.

is.list(c(1,2,3)) #returns FALSE since you passed a vector.

vec_to_list <- as.list(c(1,2,3))
is.list(vec_to_list) #verify it with is.list()

list_to_vec <- unlist(vec_to_list) # a list can be unrolled into a vector
is.vector(list_to_vec)

# reverse or change the order of a list
str(rev(list_define))