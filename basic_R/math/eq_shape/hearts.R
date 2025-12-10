heart_eq1 <- function(n_pat = 101, epsilon = 1e-6) {
  t <- seq(-1, 1, length.out = n_pat)
  x <- sin(t) * cos(t) * log(abs(t) + epsilon)
  y <- sqrt(abs(t)) * cos(t)
  
  plot(x, y, type = "l", asp = 1, main = "Heart Curve Type 1",
       xlab = "", ylab = "", col = "red")
}

heart_eq2 <- function(n_pat = 500) {
  x <- seq(-1.25, 1.25, length.out = n_pat)
  y <- seq(-1.1, 1.25, length.out = n_pat)
  X <- rep(x, each = length(y))
  Y <- rep(y, times = length(x))
  F <- (X^2 + Y^2 - 1)^3 - (X^2) * (Y^3)
  
  zero_idx <- which(abs(F) < 1e-3)
  plot(X[zero_idx], Y[zero_idx], pch = 20, cex = 0.5, col = "red", 
       asp = 1, main = "Heart Curve Type 2", xlab = "", ylab = "")
}

heart_eq3 <- function(n_pat = 500) {
  x <- seq(-1.1, 1.1, length.out = n_pat)
  y <- seq(-0.8, 1.1, length.out = n_pat)
  X <- rep(x, each = length(y))
  Y <- rep(y, times = length(x))
  cbrt_x2 <- sign(X) * abs(X)^(2/3)
  F <- X^2 + 2*(0.6 * cbrt_x2 - Y)^2 - 1
  
  zero_idx <- which(abs(F) < 1e-3)
  plot(X[zero_idx], Y[zero_idx], pch = 20, cex = 0.5, col = "#9400D3", 
       asp = 1, main = "Heart Curve Type 3", xlab = "", ylab = "")
}

heart_eq4 <- function(n_pat = 500) {
  t <- seq(0, 60, length.out = n_pat)
  poly_term <- -t^2 + 40*t + 1200
  x1 <- -0.01 * poly_term * sin(pi * t / 180)
  y1 <- 0.01 * poly_term * cos(pi * t / 180)
  x2 <- 0.01 * poly_term * sin(pi * t / 180)
  y2 <- y1
  
  plot(c(x1, x2), c(y1, y2), type = "l", asp = 1, col = "#BA55D3",
       main = "Heart Curve Type 4", xlab = "", ylab = "")
}

heart_eq5 <- function(n_pat = 500) {
  t1 <- seq(-pi, -pi/2, length.out = n_pat)
  t2 <- seq(pi/2, pi, length.out = n_pat)
  r1 <- (sin(t1))^7 * exp(2 * abs(t1))
  r2 <- (sin(t2))^7 * exp(2 * abs(t2))
  
  x1 <- r1 * cos(t1); y1 <- r1 * sin(t1)
  x2 <- r2 * cos(t2); y2 <- r2 * sin(t2)
  
  plot(c(x1, x2), c(y1, y2), type = "l", asp = 1, col = "magenta",
       main = "Heart Curve Type 5", xlab = "", ylab = "")
}

heart_eq6 <- function(n_deg = 3, n_pat = 500) {
  r <- (n_deg + 5) / 3
  x <- seq(-r*0.8, r*0.8, length.out = n_pat)
  y <- seq(-r*0.8, r, length.out = n_pat)
  X <- rep(x, each = length(y))
  Y <- rep(y, times = length(x))
  F <- X^2 + (Y - abs(X)^(1/2))^2 - n_deg
  
  zero_idx <- which(abs(F) < 1e-3)
  plot(X[zero_idx], Y[zero_idx], pch = 20, cex = 0.5, col = "purple", 
       asp = 1, main = paste("Heart Curve Type 6: n_deg =", n_deg), 
       xlab = "", ylab = "")
}

# Test it:
plot_all_hearts_grid <- function() {
  # Set up 3x2 grid layout (3 columns, 2 rows)
  par(mfrow = c(2, 3), mar = c(2, 2, 3, 1), oma = c(1, 1, 2, 1))
  
  # Plot each heart curve
  heart_eq1()
  heart_eq2()
  heart_eq3()
  heart_eq4()
  heart_eq5()
  heart_eq6()
  
  # Add overall title
  title("Six Heart Curves Comparison", outer = TRUE, line = 0)
  
  # Reset layout
  par(mfrow = c(1, 1))
}

# Usage
plot_all_hearts_grid()