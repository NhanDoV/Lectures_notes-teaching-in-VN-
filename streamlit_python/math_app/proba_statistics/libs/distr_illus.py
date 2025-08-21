import streamlit as st 
import numpy as np
import matplotlib.pyplot as plt 

def bernoulli_show(p):
    from scipy.stats import bernoulli 
    x = np.array([0, 1]) 
    pmf = bernoulli.pmf(x, p) 
    cdf = bernoulli.cdf(x, p) 
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(3.5, 6))

    ax1.bar(x, pmf, color='blue', alpha=0.7)
    ax1.set_title(f'pmf B(1, p = {p})')
    ax1.set_xlabel('$x$')
    ax1.set_xticks(x)

    ax2.bar(x, cdf, color='orange', alpha=0.7)
    ax2.set_title(f'cdf B(1, p = {p})')
    ax2.set_xlabel('$x$')
    ax2.set_xticks(x)
    plt.tight_layout()
    st.pyplot(fig)
    
def binomial_show(n, p):
    from scipy.stats import binom
    x = np.arange(0, n + 1)
    pmf = binom.pmf(x, n, p)
    cdf = binom.cdf(x, n, p)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 7))

    ax1.bar(x, pmf, color='green', alpha=0.7)
    ax1.set_title(f'PMF of Binomial(n = {n}, p = {p})')
    ax1.set_xlabel('$x$')
    ax1.set_ylabel('Probability')
    ax1.set_xticks(x)

    ax2.bar(x, cdf, color='purple', alpha=0.7)
    ax2.set_title(f'CDF of Binomial(n = {n}, p = {p})')
    ax2.set_xlabel('$x$')
    ax2.set_ylabel('Cumulative Probability')
    ax2.set_xticks(x)

    plt.tight_layout()
    st.pyplot(fig) 

def poisson_show(lambd):
    
    from scipy.stats import poisson
    x = np.arange(0, int(lambd + 4 * np.sqrt(lambd)) + 1) 
    pmf = poisson.pmf(x, mu=lambd)
    cdf = poisson.cdf(x, mu=lambd)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 7))

    ax1.bar(x, pmf, color='orange', alpha=0.7)
    ax1.set_title(f'PMF of Poisson($\lambda$ = {lambd})')
    ax1.set_xlabel('$x$')
    ax1.set_ylabel('Probability')
    ax1.set_xticks(x)

    ax2.bar(x, cdf, color='blue', alpha=0.7)
    ax2.set_title(f'CDF of Poisson($\lambda$ = {lambd})')
    ax2.set_xlabel('$x$')
    ax2.set_ylabel('Cumulative Probability')
    ax2.set_xticks(x)

    plt.tight_layout()
    st.pyplot(fig)
    
def geometry_show(p):

    from scipy.stats import geom

    x = np.arange(1, min(30, geom.ppf(0.99, p).astype(int)) + 1)
    pmf = geom.pmf(x, p)
    cdf = geom.cdf(x, p)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 7))

    ax1.bar(x, pmf, color='teal', alpha=0.7)
    ax1.set_title(f'PMF of Geometric(p = {p})')
    ax1.set_xlabel('$x$')
    ax1.set_xticks(x)

    ax2.bar(x, cdf, color='indigo', alpha=0.7)
    ax2.set_title(f'CDF of Geometric(p = {p})')
    ax2.set_xlabel('$x$')
    ax2.set_xticks(x)

    plt.tight_layout()
    st.pyplot(fig)
 
def hypergeometry_show(N, K, n):
    """
        N : population size
        K: number of sucess in population
        n: number of draws
    """ 
    from scipy.stats import hypergeom
    
    # x ranges from max(0, n + K - N) to min(n, K)
    x_min = max(0, n + K - N)
    x_max = min(n, K)
    x = np.arange(x_min, x_max + 1)

    rv = hypergeom(N, K, n)
    pmf = rv.pmf(x)
    cdf = rv.cdf(x)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 7))

    ax1.bar(x, pmf, color='crimson', alpha=0.7)
    ax1.set_title(f'PMF of Hypergeometric(N = {N}, K = {K}, n = {n})')
    ax1.set_xlabel('$x$')
    ax1.set_xticks(x)

    ax2.bar(x, cdf, color='navy', alpha=0.7)
    ax2.set_title(f'CDF of Hypergeometric(N = {N}, K = {K}, n = {n})')
    ax2.set_xlabel('$x$')
    ax2.set_xticks(x)

    plt.tight_layout()
    st.pyplot(fig)
    
def Nega_binom_show(r, p):
    """
        r : number of successes until the experiment is stopped
        p : probability in each experiment
    """
    from scipy.stats import nbinom
    # Generate a reasonable x range
    x = np.arange(0, 10 * r + 1)  # up to 10*r failures

    rv = nbinom(r, p)  # Note: scipy uses number of failures until r-th success
    pmf = rv.pmf(x)
    cdf = rv.cdf(x)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 7))

    ax1.bar(x, pmf, color='darkorange', alpha=0.7)
    ax1.set_title(f'PMF of Negative Binomial(r = {r}, p = {p})')
    ax1.set_xlabel('$x$ (failures until {r}-th success)')
    ax1.set_xticks(x[::max(1, len(x)//10)])

    ax2.bar(x, cdf, color='green', alpha=0.7)
    ax2.set_title(f'CDF of Negative Binomial(r = {r}, p = {p})')
    ax2.set_xlabel('$x$')
    ax2.set_xticks(x[::max(1, len(x)//10)])

    plt.tight_layout()
    st.pyplot(fig)    
    
def Nega_HyperGeo_show(N, K, r):
    """
        N: total number of elements
        K: total number of 'success' elements
        r:  number of failures when experiment is stopped
    """
    from scipy.special import comb
    # The number of possible successes before r failures
    max_successes = K
    x = np.arange(0, max_successes + 1)

    def pmf(x_val):
        with np.errstate(divide='ignore', invalid='ignore'):
            top = comb(x_val + r - 1, x_val) * comb(N - K - r + 1, r)
            bottom = comb(N, r + x_val)
            return np.where(bottom == 0, 0, top / bottom)

    pmf_vals = pmf(x)
    cdf_vals = np.cumsum(pmf_vals)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 7))

    ax1.bar(x, pmf_vals, color='purple', alpha=0.7)
    ax1.set_title(f'PMF of Negative Hypergeometric(N = {N}, K = {K}, r = {r})')
    ax1.set_xlabel('$x$ (successes before {r}-th failure)')
    ax1.set_xticks(x)

    ax2.bar(x, cdf_vals, color='teal', alpha=0.7)
    ax2.set_title(f'CDF of Negative Hypergeometric(N = {N}, K = {K}, r = {r})')
    ax2.set_xlabel('$x$')
    ax2.set_xticks(x)

    plt.tight_layout()
    st.pyplot(fig)
    
def unif_descrete_show(N, a, b):
    """
        N: number of random points
        a, b: respectively the lower-bound / upper-bound of these random points        
    """
    from scipy.stats import randint

    # Sample N points from the discrete uniform distribution
    samples = randint.rvs(a, b + 1, size=N)
    
    # Define x range
    x = np.arange(a, b + 1)
    
    # Theoretical PMF and CDF
    pmf = np.full_like(x, 1 / (b - a + 1), dtype=np.float64)
    cdf = np.cumsum(pmf)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 7))

    # PMF: Show histogram of the actual samples vs theoretical
    counts, bins = np.histogram(samples, bins=np.arange(a, b + 2) - 0.5, density=True)
    ax1.bar(x, counts, width=0.9, alpha=0.6, label='Sampled', color='orange')
    ax1.plot(x, pmf, 'ro-', label='Theoretical', markersize=5)
    ax1.set_title(f'PMF of Discrete Uniform({a}, {b}) with N={N}')
    ax1.set_xlabel('$x$')
    ax1.set_xticks(x)
    ax1.legend()

    # CDF: Show theoretical only
    ax2.step(x, cdf, where='mid', color='green')
    ax2.set_title(f'CDF of Discrete Uniform({a}, {b})')
    ax2.set_xlabel('$x$')
    ax2.set_xticks(x)

    plt.tight_layout()
    st.pyplot(fig)
    
def unif_cts_show(a, b):
    """
        a, b: lower-bounds and upper-bound of uniformly distribution in continuous-case
    """
    from scipy.stats import uniform

    x = np.linspace(a - (b - a) * 0.1, b + (b - a) * 0.1, 500)
    rv = uniform(loc=a, scale=b - a)

    pdf = rv.pdf(x)
    cdf = rv.cdf(x)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 7))

    ax1.plot(x, pdf, 'b-', lw=2)
    ax1.fill_between(x, pdf, alpha=0.3, color='skyblue')
    ax1.set_title(f'PDF of Continuous Uniform({a}, {b})')
    ax1.set_xlabel('$x$')

    ax2.plot(x, cdf, 'g-', lw=2)
    ax2.set_title(f'CDF of Continuous Uniform({a}, {b})')
    ax2.set_xlabel('$x$')

    plt.tight_layout()
    st.pyplot(fig)
    
def normal_show(muy, sigma):
    """
        muy, sigma: mean and standard-deviation in the normal distribution
    """
    from scipy.stats import norm

    x = np.linspace(muy - 4 * sigma, muy + 4 * sigma, 500)
    rv = norm(loc=muy, scale=sigma)

    pdf = rv.pdf(x)
    cdf = rv.cdf(x)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 7))

    ax1.plot(x, pdf, 'darkred', lw=2)
    ax1.fill_between(x, pdf, alpha=0.3, color='salmon')
    ax1.set_title(f'PDF of Normal(μ = {muy}, σ = {sigma})')
    ax1.set_xlabel('$x$')

    ax2.plot(x, cdf, 'darkgreen', lw=2)
    ax2.set_title(f'CDF of Normal(μ = {muy}, σ = {sigma})')
    ax2.set_xlabel('$x$')

    plt.tight_layout()
    st.pyplot(fig)
    
def expon_show(lambd):
    """
        lambd: lambda > 0 of the exponential distr
    """
    from scipy.stats import expon
    
    scale = 1 / lambd  # scipy uses scale = 1/lambda
    x = np.linspace(0, 10 * scale, 500)
    rv = expon(scale=scale)

    pdf = rv.pdf(x)
    cdf = rv.cdf(x)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 7))

    ax1.plot(x, pdf, 'darkblue', lw=2)
    ax1.fill_between(x, pdf, alpha=0.3, color='skyblue')
    ax1.set_title(f'PDF of Exponential(λ = {lambd})')
    ax1.set_xlabel('$x$')

    ax2.plot(x, cdf, 'darkorange', lw=2)
    ax2.set_title(f'CDF of Exponential(λ = {lambd})')
    ax2.set_xlabel('$x$')

    plt.tight_layout()
    st.pyplot(fig)
    
def cauchy_show(muy, sig):
    """
        muy: location of Cauchy distribution
        sig: scale 
    """
    from scipy.stats import cauchy
    
    x = np.linspace(muy - 10 * sig, muy + 10 * sig, 500)
    rv = cauchy(loc=muy, scale=sig)

    pdf = rv.pdf(x)
    cdf = rv.cdf(x)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 7))

    ax1.plot(x, pdf, 'purple', lw=2)
    ax1.fill_between(x, pdf, alpha=0.3, color='violet')
    ax1.set_title(f'PDF of Cauchy(μ = {muy}, σ = {sig})')
    ax1.set_xlabel('$x$')

    ax2.plot(x, cdf, 'darkgreen', lw=2)
    ax2.set_title(f'CDF of Cauchy(μ = {muy}, σ = {sig})')
    ax2.set_xlabel('$x$')

    plt.tight_layout()
    st.pyplot(fig)
    
def student_show(deg):
    """
        deg: degrees of Freedoms in the centralized Student distribution
    """
    from scipy.stats import t
    
    x = np.linspace(-10, 10, 500)
    rv = t(df=deg)

    pdf = rv.pdf(x)
    cdf = rv.cdf(x)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 7))

    ax1.plot(x, pdf, 'blue', lw=2)
    ax1.fill_between(x, pdf, alpha=0.3, color='lightblue')
    ax1.set_title(f'PDF of Student\'s t (df = {deg})')
    ax1.set_xlabel('$x$')

    ax2.plot(x, cdf, 'darkorange', lw=2)
    ax2.set_title(f'CDF of Student\'s t (df = {deg})')
    ax2.set_xlabel('$x$')

    plt.tight_layout()
    st.pyplot(fig)    
    
def chisq_show(deg):
    """
        deg: degrees of freedom for Chi-squared distribution
    """
    from scipy.stats import chi2
    
    x = np.linspace(0, deg + 10, 500)
    rv = chi2(df=deg)

    pdf = rv.pdf(x)
    cdf = rv.cdf(x)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 7))

    ax1.plot(x, pdf, 'crimson', lw=2)
    ax1.fill_between(x, pdf, alpha=0.3, color='salmon')
    ax1.set_title(f'PDF of Chi-squared (df = {deg})')
    ax1.set_xlabel('$x$')

    ax2.plot(x, cdf, 'darkgreen', lw=2)
    ax2.set_title(f'CDF of Chi-squared (df = {deg})')
    ax2.set_xlabel('$x$')

    plt.tight_layout()
    st.pyplot(fig)    
    
def fisher_show(deg_num, deg_dem):
    """
        deg_num: degrees of freedom of numerator (d1)
        deg_dem: degrees of freedom of denominator (d2)
    """
    from scipy.stats import f

    x = np.linspace(0.01, 5, 500)
    rv = f(dfn=deg_num, dfd=deg_dem)  # F-distribution from scipy

    pdf = rv.pdf(x)
    cdf = rv.cdf(x)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 7))

    ax1.plot(x, pdf, 'blue', lw=2)
    ax1.fill_between(x, pdf, alpha=0.3, color='lightblue')
    ax1.set_title(f'PDF of F-distribution (d1 = {deg_num}, d2 = {deg_dem})')
    ax1.set_xlabel('$x$')

    ax2.plot(x, cdf, 'green', lw=2)
    ax2.set_title(f'CDF of F-distribution (d1 = {deg_num}, d2 = {deg_dem})')
    ax2.set_xlabel('$x$')

    plt.tight_layout()
    st.pyplot(fig)
    
def beta_show(alpha, beta):
    """
        alpha: shape `higher alpha lean towards 1`
        beta: shape `higher beta lean towards 0`
    """
    from scipy.stats import beta as beta_dist
    
    x = np.linspace(0.01, 0.99, 500)
    rv = beta_dist(a=alpha, b=beta)

    pdf = rv.pdf(x)
    cdf = rv.cdf(x)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 7))

    ax1.plot(x, pdf, 'blue', lw=2)
    ax1.fill_between(x, pdf, alpha=0.3, color='lightblue')
    ax1.set_title(f'PDF of Beta distribution (α = {alpha}, β = {beta})')
    ax1.set_xlabel('$x$')

    ax2.plot(x, cdf, 'green', lw=2)
    ax2.set_title(f'CDF of Beta distribution (α = {alpha}, β = {beta})')
    ax2.set_xlabel('$x$')

    plt.tight_layout()
    st.pyplot(fig)
        
def gamma_show(alpha, theta):
    """ 
        alpha : shape
        theta : scale
    """
    from scipy.stats import gamma as gamma_dist
    
    x = np.linspace(0.01, 5 * alpha * theta, 500)
    rv = gamma_dist(a=alpha, scale=theta)

    pdf = rv.pdf(x)
    cdf = rv.cdf(x)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 7))

    ax1.plot(x, pdf, 'blue', lw=2)
    ax1.fill_between(x, pdf, alpha=0.3, color='lightblue')
    ax1.set_title(f'PDF of Gamma distribution (α = {alpha}, θ = {theta})')
    ax1.set_xlabel('$x$')

    ax2.plot(x, cdf, 'green', lw=2)
    ax2.set_title(f'CDF of Gamma distribution (α = {alpha}, θ = {theta})')
    ax2.set_xlabel('$x$')

    plt.tight_layout()
    st.pyplot(fig)    
    