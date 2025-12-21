# ========================= Data Structures in R ========================
# Create variables
a <- c(1,2,3,4,5,6,7,8,9)
b <- list(x = LifeCycleSavings[,1], y = LifeCycleSavings[,2])

# Retrieve the types of `a` and `b`
typeof(a)                        # return "double"
typeof(b)                        # return "list"

# Retrieve the classes of `a` and `b`
class(a)                         # return "numeric"
class(b)                         # return "list"

# Retrieve the object type
typeof(quote(x * 10))            # return "language"

# Retrieve the class
class(quote(x * 10))             # return "call"    

# A formula
c <- y ~ x
d <- y ~ x + b
# Double check the class of `c`
class(c)                        # return "formula"
