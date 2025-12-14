valid_triangle <- function(a, b, c) {
  if ((a > 0) && (b > 0) && (c > 0) && 
      (a + b > c) && (a + c > b) && (b + c > a)) {
    return(TRUE)
  } else {
    return(FALSE)
  }
}

is_Equilateral <- function(a, b, c) {
    if (valid_triangle(a, b, c) == TRUE) {
        print("Triangle is valid")
        if ((a == b) && (b == c)) {
            print("and it is Equilateral")
        } else {
            print("but not Equilateral")
        }
    } else {
        print("Triangle is not valid")
    }
}

is_Isosceles <- function(a, b, c) {
    if (valid_triangle(a, b, c) == TRUE) {
        print("Triangle is valid")
        if ((a == b) || (b == c) || (a == c)) {
            print("and it is Isosceles")
        } else {
            print("but not Isosceles")
        }
    } else {
        print("Triangle is not valid")
    }
}

# Right triangle: a² + b² = c² (with c being the largest side)
is_RightTriangle <- function(a, b, c) {
    if (valid_triangle(a, b, c) == TRUE) {
        print("Triangle is valid")
        
        # Find the largest side (assumed to be hypotenuse)
        sides <- c(a, b, c)
        hypotenuse <- max(sides)
        
        # Check Pythagorean theorem
        if (hypotenuse == c) {
            if (round(a^2 + b^2, 6) == round(c^2, 6)) {  # round to avoid floating-point errors
                print("and it is Right Triangle")
                return(TRUE)
            }
        } else if (hypotenuse == b) {
            if (round(a^2 + c^2, 6) == round(b^2, 6)) {
                print("and it is Right Triangle")
                return(TRUE)
            }
        } else if (hypotenuse == a) {
            if (round(b^2 + c^2, 6) == round(a^2, 6)) {
                print("and it is Right Triangle")
                return(TRUE)
            }
        }
        print("but not Right Triangle")
        return(FALSE)
    } else {
        print("Triangle is not valid")
        return(FALSE)
    }
}

# Scalene: a triangle with no equal sides
is_Scalene <- function(a, b, c) {
    if (valid_triangle(a, b, c) == TRUE) {
        print("Triangle is valid")
        if ((a != b) && (b != c) && (a != c)) {
            print("and it is Scalene")
            return(TRUE)
        } else {
            print("but not Scalene")
            return(FALSE)
        }
    } else {
        print("Triangle is not valid")
        return(FALSE)
    }
}

# Combined function to check all triangle types
triangle_type <- function(a, b, c) {
    cat("Analyzing triangle with sides:", a, b, c, "\n")
    cat("----------------------------------------\n")
    
    if (!valid_triangle(a, b, c)) {
        cat("Triangle is NOT VALID\n")
        return("Invalid")
    }
    
    cat("Triangle is VALID\n")
    
    # Check Equilateral (highest priority)
    if (a == b && b == c) {
        cat("Type: EQUILATERAL\n")
        return("Equilateral")
    }
    
    # Check Right Triangle
    sides <- c(a, b, c)
    hypotenuse <- max(sides)
    is_right <- FALSE
    if (hypotenuse == c && round(a^2 + b^2, 6) == round(c^2, 6)) {
        is_right <- TRUE
    } else if (hypotenuse == b && round(a^2 + c^2, 6) == round(b^2, 6)) {
        is_right <- TRUE
    } else if (hypotenuse == a && round(b^2 + c^2, 6) == round(a^2, 6)) {
        is_right <- TRUE
    }
    
    # Check Isosceles
    is_isosceles <- (a == b) || (b == c) || (a == c)
    
    # Scalene: neither isosceles nor right
    is_scalene <- !is_isosceles && !is_right
    
    if (is_right) {
        cat("Type: RIGHT TRIANGLE\n")
        return("Right Triangle")
    } else if (is_isosceles) {
        cat("Type: ISOSCELES\n")
        return("Isosceles")
    } else if (is_scalene) {
        cat("Type: SCALENE\n")
        return("Scalene")
    }
}

# Test cases
triangle_type(2, 2, 2)        # Equilateral
triangle_type(5, 5, 6)        # Isosceles  
triangle_type(3, 4, 5)        # Right Triangle
triangle_type(2, 3, 4)        # Scalene
triangle_type(1, 1, 3)        # Invalid