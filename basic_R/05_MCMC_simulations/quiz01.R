target_pdf <- function(x) {
  return(dnorm(x, mean = 10, sd = 2))
}

mcmc_sampler <- function(n_samples, initial_x, proposal_sd) {
  x <- numeric(n_samples)
  x[1] <- initial_x
  for (i in 2:n_samples) {
    current_x <- x[i-1]
    proposed_x <- current_x + rnorm(1, mean = 0, sd = proposal_sd)
    R <- target_pdf(proposed_x) / target_pdf(current_x)
    if (runif(1) < R) x[i] <- proposed_x else x[i] <- current_x
  }
  return(x)
}

set.seed(123)
samples <- mcmc_sampler(50000, 5, 1)
effective_samples <- samples[-(1:5000)]
cat("Estimated mean:", mean(effective_samples), "\n")
