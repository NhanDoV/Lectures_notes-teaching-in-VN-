# Mixture PDF: 0.3*N(0,1) + 0.7*N(5,2)
target_pdf <- function(x) {
  0.3*dnorm(x,0,1) + 0.7*dnorm(x,5,2)
}

mcmc_sampler <- function(n_samples, initial_x, proposal_sd) {
  x <- numeric(n_samples)
  x[1] <- initial_x
  for (i in 2:n_samples) {
    current_x <- x[i-1]
    proposed_x <- current_x + rnorm(1, 0, proposal_sd)
    R <- target_pdf(proposed_x) / target_pdf(current_x)
    if (runif(1) < R) x[i] <- proposed_x else x[i] <- current_x
  }
  return(x)
}

set.seed(123)
samples <- mcmc_sampler(50000, 0, 1)
effective_samples <- samples[-(1:5000)]
cat("Estimated mean of mixture:", mean(effective_samples), "\n")