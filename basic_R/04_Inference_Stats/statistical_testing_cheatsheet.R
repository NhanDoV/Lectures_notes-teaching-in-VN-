###############################
# 1. MEAN TESTS
###############################

# 1-Sample t-test (mean vs μ0)
# t.test(x, mu = μ0)
# Example:
x <- c(1, 2, 3, 5, 9)
t.test(x, mu = 5)

# 2-Sample t-test (independent)
# Welch test is default unless var.equal=TRUE
x <- c(1, 3, 5)
y <- c(2, 4, 6, 8)
t.test(x, y, var.equal = FALSE)

# Paired t-test
x <- c(1, 2, 9, 5, -2, -3)
y <- c(2, 4, 9, 8, 8, 1)
t.test(x, y, paired = TRUE)

# Mean difference (paired data), one sample
t.test(x - y)

###############################
# 2. VARIANCE TESTS
###############################

# 1-Sample Variance Test (χ²)
# (no base R function)

# 2-Sample Variance Test (F-test)
var.test(x, y)
# Tests H0: σ1² = σ2²


###############################
# 3. PROPORTION TESTS
###############################

# 1-Sample proportion test
prop.test(x, n, p = p0)

# 2-Sample proportion test
prop.test(c(x1, x2), c(n1, n2))


###############################
# 4. INDEPENDENCE / ASSOCIATION TESTS
###############################

# Chi-square test for independence
chisq.test(table)

# Fisher exact test (small sample size)
fisher.test(table)

# Correlation significance
cor.test(x, y, method = "pearson")
cor.test(x, y, method = "spearman")
cor.test(x, y, method = "kendall")


###############################
# 5. DISTRIBUTION TESTS
###############################

# Shapiro–Wilk test (normality)
shapiro.test(x)

# Kolmogorov–Smirnov test
ks.test(x, y)        # sample vs sample
ks.test(x, "pnorm")  # sample vs normal distribution


###############################
# 6. ANOVA TESTS
###############################

# One-way ANOVA
aov(y ~ group, data = df)
summary(aov(y ~ group, data = df))

# Nonparametric ANOVA (Kruskal–Wallis)
kruskal.test(y ~ group, data = df)


###############################
# 7. REGRESSION TESTS
###############################

# Simple linear regression
model <- lm(y ~ x)
summary(model)

# Multiple regression
model <- lm(y ~ x1 + x2 + x3)
summary(model)