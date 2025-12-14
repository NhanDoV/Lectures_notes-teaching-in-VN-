# Target PDF: exponential with rate 1
target_pdf <- function(x) {
  if (x < 0) return(0) # support x >= 0
  return(dexp(x, rate = 1))
}

# Function to compute expected value h(X) = X^2
mcmc_sampler <- function(n_samples, initial_x, proposal_sd) {
  x <- numeric(n_samples)
  x[1] <- initial_x
  for (i in 2:n_samples) {
    current_x <- x[i-1]
    proposed_x <- abs(current_x + rnorm(1, 0, proposal_sd)) # reflect negative proposals
    R <- target_pdf(proposed_x) / target_pdf(current_x)
    if (runif(1) < R) x[i] <- proposed_x else x[i] <- current_x
  }
  return(x)
}

set.seed(123)
samples <- mcmc_sampler(50000, 1, 1)
effective_samples <- samples[-(1:5000)]
integral_estimate <- mean(effective_samples^2) # E[X^2]
cat("Estimated E[X^2]:", integral_estimate, "\n")
cat("True E[X^2]:", 2, "\n") # Exponential(1) variance + mean^2