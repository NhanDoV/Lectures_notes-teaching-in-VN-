###############################################################
# R DISTRIBUTION FUNCTIONS WITH EXAMPLES
###############################################################

# 1. NORMAL DISTRIBUTION
x <- 0.5
mean <- 0
sd <- 1
dnorm(x, mean, sd)
pnorm(x, mean, sd)
qnorm(0.95, mean, sd)
rnorm(5, mean, sd)

# 2. BINOMIAL DISTRIBUTION
x <- 3
size <- 10
prob <- 0.5
dbinom(x, size, prob)
pbinom(x, size, prob)
qbinom(0.75, size, prob)
rbinom(5, size, prob)

# 3. POISSON DISTRIBUTION
x <- 2
lambda <- 3
dpois(x, lambda)
ppois(x, lambda)
qpois(0.8, lambda)
rpois(5, lambda)

# 4. EXPONENTIAL DISTRIBUTION
x <- 1
rate <- 2
dexp(x, rate)
pexp(x, rate)
qexp(0.9, rate)
rexp(5, rate)

# 5. UNIFORM DISTRIBUTION
x <- 0.4
min <- 0
max <- 1
dunif(x, min, max)
punif(x, min, max)
qunif(0.7, min, max)
runif(5, min, max)

# 6. GAMMA DISTRIBUTION
x <- 2
shape <- 2
rate <- 1
dgamma(x, shape, rate)
pgamma(x, shape, rate)
qgamma(0.8, shape, rate)
rgamma(5, shape, rate)

# 7. BETA DISTRIBUTION
x <- 0.3
shape1 <- 2
shape2 <- 5
dbeta(x, shape1, shape2)
pbeta(x, shape1, shape2)
qbeta(0.9, shape1, shape2)
rbeta(5, shape1, shape2)

# 8. CHI-SQUARE DISTRIBUTION
x <- 3
df <- 4
dchisq(x, df)
pchisq(x, df)
qchisq(0.95, df)
rchisq(5, df)

# 9. STUDENT t DISTRIBUTION
x <- 1
df <- 10
dt(x, df)
pt(x, df)
qt(0.975, df)
rt(5, df)

# 10. F DISTRIBUTION
x <- 2
df1 <- 5
df2 <- 10
df(x, df1, df2)
pf(x, df1, df2)
qf(0.9, df1, df2)
rf(5, df1, df2)

# 11. GEOMETRIC DISTRIBUTION
x <- 2
prob <- 0.3
dgeom(x, prob)
pgeom(x, prob)
qgeom(0.8, prob)
rgeom(5, prob)

# 12. HYPERGEOMETRIC DISTRIBUTION
x <- 3
m <- 10
n <- 5
k <- 4
dhyper(x, m, n, k)
phyper(x, m, n, k)
qhyper(0.7, m, n, k)
rhyper(5, m, n, k)

# 13. NEGATIVE BINOMIAL DISTRIBUTION
x <- 3
size <- 5
prob <- 0.4
dnbinom(x, size, prob)
pnbinom(x, size, prob)
qnbinom(0.85, size, prob)
rnbinom(5, size, prob)

# 14. LOG-NORMAL DISTRIBUTION
x <- 1
meanlog <- 0
sdlog <- 0.5
dlnorm(x, meanlog, sdlog)
plnorm(x, meanlog, sdlog)
qlnorm(0.9, meanlog, sdlog)
rlnorm(5, meanlog, sdlog)

# 15. WEIBULL DISTRIBUTION
x <- 1
shape <- 2
scale <- 1
dweibull(x, shape, scale)
pweibull(x, shape, scale)
qweibull(0.8, shape, scale)
rweibull(5, shape, scale)

# 16. CAUCHY DISTRIBUTION
x <- 0.5
location <- 0
scale <- 1
dcauchy(x, location, scale)
pcauchy(x, location, scale)
qcauchy(0.9, location, scale)
rcauchy(5, location, scale)

# 17. MULTINOMIAL DISTRIBUTION
size <- 5
prob <- c(0.2, 0.3, 0.5)
rmultinom(1, size, prob)
rmultinom(5, size, prob)