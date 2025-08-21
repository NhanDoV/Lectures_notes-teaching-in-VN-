import streamlit as st

def render_latex_table(df, distr_1, distr_2):
    markdown_table = "| Features - Variables | " + distr_1 + " | " + distr_2 + " |\n"
    markdown_table += "|:--------|:-------------|:-------------|\n"
    for _, row in df.iterrows():
        markdown_table += f"| {row['Feature']} | {row[distr_1]} | {row[distr_2]} |\n"
    
    return markdown_table

distribution_ls = [
    "Bernoulli", "Binomial", "Poisson", "Geometry", "HyperGeometry", "Negative Binomial", "Negative HyperGeometry",
    "Uniform (descrete type)", "Uniform (continuous type)", "Normal", "Exponential", "Student", "Chi-squared",
    "Fisher", "Beta", "Gamma", "Cauchy" 
]

notation_map = {
    "Bernoulli": r"$\mathcal{B}(1, p)$",
    "Binomial": r"$\mathcal{B}(n, p)$",
    "Poisson": r"$\mathcal{P}(\lambda)$",
    "Geometry": r"Geo$(p)$",
    "HyperGeometry": r"HyperGeo$(N, K, n)$", 
    "Negative Binomial": r"NB$(r, p)$", 
    "Negative HyperGeometry": r"NHG$(N, K, r)$",
    "Uniform (descrete type)": r"$\mathcal{U}\lbrace a_1, \ldots, a_k \rbrace$", 
    "Uniform (continuous type)": r"$\mathcal{U}(a, b)$",
    "Normal": r"$\mathcal{N}(\mu, \sigma^2)$", 
    "Exponential": r"$\mathcal{E}( \lambda )$", 
    "Student": r"$\mathcal{St}(d)$", 
    "Chi-squared": r"$\chi^2(d)$",
    "Fisher": r"$\mathcal{F}(d_1, d_2)$", 
    "Beta": r"Beta$(\alpha, \beta)$",
    "Gamma": r"Gamma$(\alpha, \lambda)$", 
    "Cauchy": r"Cauchy$(\mu, \sigma)$"
}

description_map = {
    "Bernoulli": "Observe a single binary trial where the outcome is either a success or a failure. <br> Example: <li> Tossing a coin once (Heads or Tails), <li> testing if a product is defective (Yes or No).",
    "Binomial": "Observe multiple independent binary trials (repeated Bernoulli experiments). <br> Counts how many times success occurs out of a fixed number of trials. <br> Example: <li> Tossing a coin 10 times and counting how many heads appear, <li> testing 20 items for defects.",
    "Poisson": "Models the number of events happening in a fixed interval of time or space when events occur independently at a constant rate. <br> Example: <li>Number of emails received per hour</li> <li>Number of cars passing through a toll booth in 10 minutes</li>",
    "Geometry": "Counts the number of trials needed to get the first success in a series of independent Bernoulli trials. <br> Example: <li>Flipping a coin until the first heads appears</li>",
    "HyperGeometry": "<li> For $x$ successes (random draws for which the object drawn has a specified feature) in $n$ draws, `without replacement`, from a finite population of size $N$ that contains exactly $K$ objects <br> with that feature, wherein each draw is either a success or a failure. <br> <li> In contrast, the binomial distribution describes the probability of $x$ successes in $n$ draws `with replacement` <br> Example: We have 5 red apples and 45 green apples, ($N=50$), draw 10 apples without replacement ($n=10$), What is the probability that exactly 4 of the 10 are red $(K = 5, x = 4)$", 
    "Negative Binomial": "Number of successes $r$ until the experiment is stopped with many failures $x$ with probability in each experiment $p$. <br> Example: Pat Collis is required to sell candy bars to raise money for the 6th grade field trip. Pat is (somewhat harshly) not supposed to return home until $r=5$ candy bars have been sold. So the child goes door to door, selling candy bars. At each house, there is a 0.6 probability of selling one candy bar and a $p=0.4$ probability of selling nothing.", 
    "Negative HyperGeometry": "Drawing elements `without replacement` from a population of size $N$, which has $K$ sucesses an we will stop the experiment until exactly $r$ `failures` are observed. <br> Example: Given 10 cards ($N=10$ and $K=4$ red cards); we will stop after seeing $r=3$ black cards then $X \sim$ NHG$(10, 4, 3)$",
    "Uniform (descrete type)": "Each outcome in a finite set has equal probability. <br> Example: <li>Rolling a fair die (1 to 6)</li>", 
    "Uniform (continuous type)": "Every value in a continuous interval has equal probability density. <br> Example: <li>Picking a random number between 0 and 1</li>", 
    "Normal": "A continuous distribution shaped like a bell curve, centered around the mean. Common in natural data. <br> Example: <li>Heights of people</li> <li>Exam scores</li>", 
    "Exponential": "Models the time between events in a Poisson process. Memoryless property. <br> Example: <li>Time between incoming phone calls</li>", 
    "Student": "A distribution used instead of Normal when sample size is small and variance is unknown. <br> Example: <li>Estimating a population mean with small samples</li>", 
    "Chi-squared": "Used in hypothesis testing and confidence interval estimation for variance. <br> Example: <li>Goodness-of-fit tests</li>",
    "Fisher": "Used in comparing two sample variances (ANOVA). <br> Example: <li>Testing if two groups have the same variance</li>", 
    "Beta": "Continuous distribution on [0,1], useful for modeling probabilities. <br> Example: <li>Modeling success rate in Bayesian inference</li>", 
    "Gamma": "Generalization of exponential distribution. Models waiting time for multiple events. <br> Example: <li>Total time until 3 customers arrive</li>",
    "Cauchy": "Has heavy tails and undefined mean/variance. Often used to demonstrate issues with estimation. <br> Example: <li>Ratio of two standard normal variables</li>"
}

domain_mapping = {
    "Bernoulli": r"$\lbrace 0, 1 \rbrace$",
    "Binomial": r"$\lbrace 0, 1, \ldots, n \rbrace$",
    "Poisson": r"$\lbrace 0, 1, \ldots, \infty \rbrace$",
    "Geometry": r"$\lbrace 0, 1, \ldots, \infty \rbrace$",
    "HyperGeometry": r"$\lbrace \max\lbrace 0, n+K-N \rbrace, \min \lbrace n, K \rbrace \rbrace$", 
    "Negative Binomial": r"$ \lbrace 0,1,\ldots \rbrace $", 
    "Negative HyperGeometry": r"$ \lbrace 0, \ldots, K \rbrace $",
    "Uniform (descrete type)": r"$\lbrace a_1, \ldots, a_k \rbrace$", 
    "Uniform (continuous type)": r"$(a, b)$", 
    "Normal": r"$\mathbb{R}$", 
    "Exponential": r"$\mathbb{R}_{+}$", 
    "Student": r"$\mathbb{R}$", 
    "Chi-squared": r"$\mathbb{R}_{++}$",
    "Fisher": r"$\mathbb{R}_{++}$", 
    "Beta": r"$[0, 1]$", 
    "Gamma": r"$\mathbb{R}_{+}$", 
    "Cauchy": r"$\mathbb{R}$"
}

params_mapping = {
    "Bernoulli": r"$p \in [0, 1]$",
    "Binomial": r"$p \in [0, 1] \quad n \in \mathbb{N}$",
    "Poisson": r"$\lambda \in (0, \infty)$",
    "Geometry": r"$p \in [0, 1)$",
    "HyperGeometry": r"$N \in \overline{0,1, \ldots} \quad K,n \in \overline{0,1, \ldots, N}$", 
    "Negative Binomial": r"<li> $r > 0$, by moment-method $r = \frac{\mathbb{E}X^2}{ \text{Var} X - \mathbb{E}X }$ <br> <li> $p \in [0, 1]$ likewise $p = \frac{\mathbb{E}X}{ \text{Var} X }$", 
    "Negative HyperGeometry": r"$N \in \lbrace 0,1,\ldots \rbrace \quad K \in \lbrace 0,1, \ldots, N \rbrace \quad r \in \lbrace 0,1, \ldots, N-K \rbrace $",
    "Uniform (descrete type)": r"$a_1, \ldots, a_k \in \mathbb{R}$ and $a_1 < a_2 \leq \ldots \leq a_k$", 
    "Uniform (continuous type)": r"$-\infty < a < b < \infty$", 
    "Normal": r"$\mu \in \mathbb{R} \quad \sigma^2 > 0$", 
    "Exponential": r"$\lambda > 0$", 
    "Student": r"$d > 0$ is `degrees of freedom`, almost always a positive integer", 
    "Chi-squared":  r"$d > 0$ is `degrees of freedom`, almost always a positive integer <br> whereas $\chi_d^2 = \displaystyle \sum_{i=1}^d \mathcal{N}^2 $",
    "Fisher":  r"$d_1, d_2 > 0$ are `degrees of freedom`, almost always a positive integer <br> whereas $\mathcal{F}(d_1, d_2) = \dfrac{\chi^2_{d_1} / d_1}{ \chi^2_{d_2} / d_2 } $",
    "Beta": r"<li> $\alpha > 0$: shape; by moment method: $ \left( \frac{\mathbb{E}X \left( 1 - \mathbb{E} X \right)}{ \text{Var} X } - 1 \right) \mathbb{E} X $ <br> <li> $\beta > 0$: shape; likewise: $ \left( \frac{\mathbb{E}X \left( 1 - \mathbb{E} X \right)}{ \text{Var} X } - 1 \right) (1 - \mathbb{E} X) $ ", 
    "Gamma": r"<li> $\alpha > 0$: shape ( by method of moment: $\frac{\mathbb{E}X^2}{ \text{Var} X }$ )<br> <li> $\lambda > 0$: scale (likewise,: $\frac{\mathbb{E}X}{ \text{Var} X }$ )", 
    "Cauchy":  r"$\mu \in \mathbb{R} \quad \sigma > 0$" 
}

pdf_pmf_mapping = {
    "Bernoulli": r"$p^x (1-p)^{1-x}$",
    "Binomial": r"$\displaystyle \binom{n}{x} p^x (1-p)^{n-x}$",
    "Poisson": r"$\dfrac{e^{-\lambda} \lambda^x }{x!}$",
    "Geometry": r"$p(1-p)^x$ if $x \in \lbrace 0,1, \ldots \rbrace$ <br> or <br> $p(1-p)^{x-1}$ if $x \in \lbrace 1,2, \ldots \rbrace$",
    "HyperGeometry": r"$ \dfrac{ \binom{K}{x} \binom{N - K}{K - x} }{\binom{N}{n}} $", 
    "Negative Binomial": r"$\displaystyle \binom{r+x-1}{x} p^r (1-p)^x $", 
    "Negative HyperGeometry": r"$ \dfrac{\displaystyle \binom{r+x-1}{x} \binom{N-r-x}{K-x} }{ \displaystyle \binom{N}{K} } $",
    "Uniform (descrete type)": r"$\frac{1}{k}$", 
    "Uniform (continuous type)": r"$\dfrac{1}{b - a}$", 
    "Normal": r"$ \dfrac{1}{\sigma \sqrt{2\pi}} \exp \left( \frac{ (x - \mu)^2 }{2\sigma^2} \right) $", 
    "Exponential": r"$\lambda e^{-\lambda x}$", 
    "Student": r"$ \dfrac{\Gamma\left( \frac{d+1}{2} \right) }{ \sqrt{\pi d} \Gamma \left( \frac{d}{2} \right) } \left( 1 + \frac{x^2}{d} \right)^{-\frac{(d+1)}{2}} $", 
    "Chi-squared": r"$\dfrac{1}{2^{d/2} \cdot \Gamma \left( d/2 \right) } x^{d/2 - 1} e^{-x / 2} $",
    "Fisher": r"$ \dfrac{1}{x B\left( \frac{d_1}{2}, \frac{d_2}{2} \right)} \sqrt{ \dfrac{ (d_1 x)^{d_1} d_2^{d_2} }{(d_1 x + d_2)^{d_1 + d_2} } } $", 
    "Beta": r"$\qquad \qquad \dfrac{x^{\alpha - 1} (1 - x)^{\beta - 1} }{ B(\alpha, \beta) } $ <br> <br> where $B(a, b) := \frac{\Gamma(a) \Gamma(b)}{\Gamma(a+b)} $ is `Beta function` <br> and $\Gamma(\dot)$ is the `Gamma function` [see Gamma distribution]", 
    "Gamma": r"$ \dfrac{\lambda^{\alpha}}{\Gamma (\alpha)} x^{\alpha - 1} x^{-\lambda x} $ where <br> $\qquad \quad \displaystyle \Gamma(s, x) = \int_x^{\infty} t^{s-1} e^{-t} dt $ is the `upper incomplete gamma function` <br> in some version we can see the scale $r = \lambda^{-1} \in (0, 1]$ instead", 
    "Cauchy": r"$ \dfrac{1}{\pi \sigma \left[ 1 + \left( \frac{x - \mu}{\sigma} \right)^2 \right] } $"    
}

cdf_mapping = {
    "Bernoulli": r"$\left\lbrace \begin{array}{ccc} 0 && x < 0 \\ 1-p && x \in [0, 1] \\ 1 && x > 1 \end{array} \right.$",
    "Binomial": r"$\left\lbrace \begin{array}{ccl} 0 && x < 0 \\ \displaystyle \sum_{k=0}^x C_k^n p^k (1-p)^{n-k} && x \in [0, n) \\ 1 && x \geq n \end{array} \right.$",
    "Poisson":  r"$ \displaystyle \sum_{k=0}^x \dfrac{e^{-\lambda} \lambda^k }{k!} * \mathcal{I}_{\left( x \geq 0 \right)} $",
    "Geometry": r"$\left( 1 - (1 - p)^{1 + \text{floor} (x) } \right) * \mathcal{I}_{ \lbrace x \geq 0 \rbrace }$ if minimum in domain = 0 <br> <br> $\left( 1 - (1 - p)^{ \text{floor} (x) } \right) * \mathcal{I}_{ \lbrace x \geq 1 \rbrace }$ if minimum in domain = 1",
    "HyperGeometry": r"$ \displaystyle \sum_{k=0}^x \dfrac{\binom{K}{k} \binom{N-K}{n-k} }{ \binom{N}{n} } $", 
    "Negative Binomial": r"$ \displaystyle \sum_{k=0}^x \binom{r+k-1}{k} p^r (1-p)^k $", 
    "Negative HyperGeometry": r"$\displaystyle \sum_{k=0}^x \dfrac{ \binom{r+k-1}{k} \binom{N-r-k}{K-k} }{ \binom{N}{K} } $",
    "Uniform (descrete type)": r"$ \displaystyle \sum_{j=0}^m \frac{a_j}{k} * \mathcal{I}_{ \lbrace a_{1} < x \leq a_m  \rbrace } $", 
    "Uniform (continuous type)": r"$ \dfrac{x - a}{b - a} * \mathcal{I}_{ \lbrace x > a \rbrace } $", 
    "Normal": r"$ \dfrac{1}{2} \left[ 1 + \text{erf} \left( \frac{ x - \mu }{\sigma \sqrt{2} } \right) \right] $ where $ \text{erf}(x) = \displaystyle \frac{2}{\sqrt{\pi}} \int_0^x e^{-t^2}dt $", 
    "Exponential": r"$1 - e^{-\lambda x}$", 
    "Student": r"$ \frac{1}{2} + x \, \Gamma\left( \frac{d + 1}{2} \right) \cdot \frac{ {}_2F_1\left( \frac{1}{2}, \frac{d + 1}{2}; \frac{3}{2}; -\frac{x^2}{d} \right) }{ \sqrt{\pi d} \, \Gamma\left( \frac{d}{2} \right) } $ <br> where ${}_2F_1$ is a `hypergeometric function`", 
    "Chi-squared": r"$\dfrac{1}{\Gamma(d / 2)} \cdot \gamma \left( \frac{x}{2}, \frac{d}{2} \right)$ where $\Gamma, \gamma$ are `upper and lower incomplete Gamma` functions [see Gamma distribution]",
    "Fisher": r"$ I_{\frac{d_1 x}{ d_1 x + d_2 }} \left( \frac{d_1}{2}, \frac{d_2}{2} \right)$ where $I_x(a, b) = \dfrac{B(x, a, b)}{B(a, b)}$ <br> is the `regularized incomplete beta function` <br> $B(a,b)$ is `Beta function` [see Beta distribution] and <br> $B(x,a,b) = \displaystyle \int_0^x t^{a-1} (1-t)^{b-1} dt$ is `regularized incomplete beta function`", 
    "Beta": r"$ \dfrac{ \displaystyle \int_0^x t^{\alpha - 1} (1 - t)^{\beta - 1} dt }{B(\alpha, \beta)} $", 
    "Gamma": r"$\dfrac{\gamma (\alpha, \lambda x)}{ \Gamma (\alpha) }$  where <br> $\qquad \gamma(s, x) = \displaystyle \int_0^x t^{s-1} e^{-t} dt $ is the `lower incomplete gamma function`.", 
    "Cauchy": r"$ \qquad \dfrac{1}{\pi} \arctan \left( \dfrac{x - \mu}{\sigma} \right) + \dfrac{1}{2} $"    
}

expec_mapping = {
    "Bernoulli": r"$p$",
    "Binomial": r"$np$",
    "Poisson": r"$\lambda$",
    "Geometry": r"$ \dfrac{1 - p}{p} $",
    "HyperGeometry": r"$\dfrac{nK}{N}$", 
    "Negative Binomial": r"$\dfrac{r(1-p)}{p}$", 
    "Negative HyperGeometry": r"$\dfrac{Kr}{N - K + 1}$",
    "Uniform (descrete type)": r"$ k^{-1} \sum_{j=1}^k a_j $", 
    "Uniform (continuous type)": r"$\dfrac{a+b}{2}$", 
    "Normal": r"$\mu$", 
    "Exponential": r"$ \lambda^{-1} $", 
    "Student": r"$0$ if $d > 1, \quad$ otherwise `undefined`", 
    "Chi-squared": r"$d$",
    "Fisher": r"$\dfrac{d_2}{d_2 - 2}$ for $d_2 > 2$", 
    "Beta": r"$\begin{array}{lcl} \mathbb{E} X &=& \dfrac{\alpha}{\alpha + \beta} \\ \mathbb{E} \ln X &=& \psi(\alpha) -\psi(\alpha + \beta) \\ \mathbb{E} X \ln X &=& \dfrac{\alpha}{\alpha + \beta} \left[ \psi(\alpha+1) - \psi(1+\alpha+\beta) \right] \end{array}$ <br> where $\psi$ is the `digamma function`", 
    "Gamma": r"$\dfrac{\alpha}{\lambda}$", 
    "Cauchy": "undefined [see the proofs in the next page]"    
}

mode_mapping = {
    "Bernoulli": r"$ \left\lbrace \begin{array}{ccc} 0 && p < 0.5 \\ \lbrace 0, 1 \rbrace && p = 0.5\\ 1 && p > 0.5 \end{array} \right. $",
    "Binomial": r"$ \lbrace \text{ floor} [p(n+1)] ; \text{ ceil} [p(n+1)] - 1 \rbrace $",
    "Poisson": r"$ \lbrace \text{ceil}(\lambda) - 1, \text{floor}(\lambda) \rbrace$",
    "Geometry": r"$0$ the minimum value from the support-domain <br> $1$ if you consider your domain is $\lbrace 1, 2, \ldots, \rbrace $",
    "HyperGeometry": r"$ \left\lbrace \text{ceil} \left( \dfrac{(n+1)(K+1)}{N+2} \right) - 1; \text{floor} \left( \dfrac{(n+1)(K+1)}{N+2} \right) \right\rbrace $", 
    "Negative Binomial": r"floor$\left( \dfrac{(r - 1)(1 - p)}{p} \right) * \mathcal{I}_{ \lbrace r > 1 \rbrace } $", 
    "Negative HyperGeometry": "not defined in general case",
    "Uniform (descrete type)": "any value since uniformly", 
    "Uniform (continuous type)": r"$\dfrac{a+b}{2}$", 
    "Normal": r"$\mu$", 
    "Exponential": r"$ 0 $", 
    "Student": r"$ 0 $", 
    "Chi-squared": r"$ \max \lbrace d-2, 0 \rbrace $",
    "Fisher": r"$ \dfrac{d_2 (d_1 - 2)}{d_1 (d_2 + 2)}$ for $d_1 > 2$", 
    "Beta": r"$\dfrac{\alpha - 1}{\alpha + \beta - 2}$ only if $\alpha, \beta > 1$; otherwise `no mode`", 
    "Gamma": r"$ \dfrac{\alpha - 1}{\lambda} * \mathcal{I}_{ \lbrace \alpha \geq 1 \rbrace } $", 
    "Cauchy": r"$\mu$"    
}

median_mapping = {
    "Bernoulli": r"$ \left\lbrace \begin{array}{ccc} 0 && p < 0.5 \\ [0, 1] && p = 0.5\\ 1 && p > 0.5 \end{array} \right. $",
    "Binomial": r"$ \left\lbrace \begin{array}{ccr} \text{ floor} [np] \\ \text{ ceil} [np] \end{array} \right. $",
    "Poisson": r"$\approx \text{ceil} \left( \lambda + \frac{1}{3} - \frac{1}{50 \lambda} \right)$",
    "Geometry": r"ceil$\left( \dfrac{-1}{ \log_2 (1 - p)} \right) - 1$ <br> and not unique if $ \dfrac{-1}{ \log_2 (1 - p)}$ is an integer)",
    "HyperGeometry": "does not have a closed-form formula in general", 
    "Negative Binomial": " not defined in general case", 
    "Negative HyperGeometry": "not defined in general case",
    "Uniform (descrete type)": "not defined in general case", 
    "Uniform (continuous type)": "any value since uniformly", 
    "Normal": r"$\mu$", 
    "Exponential": r"$ \dfrac{\ln 2}{\lambda} $", 
    "Student": r"$ 0 $", 
    "Chi-squared": r"$ \left( 1 - \dfrac{2}{9d} \right)^3 $",
    "Fisher": "undefined ", 
    "Beta": r"$\approx \dfrac{\alpha - \frac{1}{3}}{ \alpha + \beta - \frac{2}{3} }$ for $\alpha, \beta > 1$", 
    "Gamma": "Simple closed form does not exist", 
    "Cauchy": r"$\mu$"    
}

variance_mapping = {
    "Bernoulli": r"$ p(1-p) $",
    "Binomial": r"$np(1-p)$",
    "Poisson": r"$\lambda$",
    "Geometry": r"$\dfrac{1 - p}{p^2}$",
    "HyperGeometry": r"$ \dfrac{nK(N-K)(N-n)}{N^2(N-1)} $", 
    "Negative Binomial": r"$\dfrac{r(1-p)}{p^2}$", 
    "Negative HyperGeometry": r"$ \dfrac{Kr(N + 1)}{(N - K + 1)(N - K + 2)} \left( 1 - \dfrac{r}{N-K+1} \right) $",
    "Uniform (descrete type)": r"$\displaystyle \left( k^{-1} \sum_{i=1}^k a_i^2 \right) - \left( k^{-1} \sum_{i=1}^k a_i \right)^2 $", 
    "Uniform (continuous type)": r"$\dfrac{(b-a)^2}{12}$", 
    "Normal": r"$\sigma^2$", 
    "Exponential": r"$ \lambda^{-2} $", 
    "Student": r"<li> $\dfrac{d}{d-2}$ if $d > 2$ <br> <li> $\infty$ if $1 < d \leq 2$", 
    "Chi-squared": r"$2d$",
    "Fisher": r"$ \dfrac{2d_2^2 (d_1 + d_2 - 2)}{d_1 (d_2 - 4) (d_2 - 2)^2} $ for $d_2 > 4$", 
    "Beta": r"$ \dfrac{\alpha \beta}{ (\alpha + \beta)^2 (\alpha + \beta + 1) } $", 
    "Gamma": r"$\dfrac{\alpha}{\lambda^2}$", 
    "Cauchy": "undefined since expectation undefined"
}

skewness_mapping = { 
    "Bernoulli": r"$ \dfrac{1 - 2p}{\sqrt{p(1 - p)} } $",    
    "Binomial": r"$ \dfrac{1 - 2p}{\sqrt{n p(1 - p)} } $",
    "Poisson": r"$\lambda^{-1/2}$",
    "Geometry": r"$\dfrac{2 - p}{\sqrt{1 - p}}$",
    "HyperGeometry": r"$\dfrac{(N - 2K)(N - 1)^{1/2}(N - 2n)}{[nK(N - K)(N - n)]^{1/2}(N - 2)} $", 
    "Negative Binomial": r"$\dfrac{2-p}{ \sqrt{r(1-p)} }$", 
    "Negative HyperGeometry": "not defined in general case",
    "Uniform (descrete type)": "not defined in general case", 
    "Uniform (continuous type)": r"$0$", 
    "Normal": r"$0$", 
    "Exponential": "2", 
    "Student": r"$0$ if $d > 3, \quad$ otherwise `undefined`", 
    "Chi-squared": r"$ \sqrt{8 / d} $",
    "Fisher": r"$ \dfrac{(2d_1 + d_2 - 2)\sqrt{8(d_2 - 4)} }{(d_2 - 6) \sqrt{d_1 (d_1 + d_2 - 2)} } $ for $d_2 > 6$", 
    "Beta": r"$\dfrac{2(\beta - \alpha) \sqrt{\alpha + \beta + 1}}{(\alpha + \beta + 2) \sqrt{\alpha \beta}}$", 
    "Gamma": r"$\dfrac{2}{\sqrt{\alpha}}$", 
    "Cauchy": "undefined"    
}

kurtosis_mapping = {
    "Bernoulli": r"$ \dfrac{1 - 6p(1-p)}{p(1-p)} $",
    "Binomial": r"$ \dfrac{1 - 6p(1 - p)}{n p (1-p)} $",
    "Poisson": r"$\lambda^{-1}$",
    "Geometry": r"$6 + \dfrac{p^2}{1 - p}$",
    "HyperGeometry": r"$\dfrac{\Bigg[ (N - 1)N^2(N + 1) - 6K(N - K)(N - n) - 6n(N - n) + 6nK(N - K)(N - n)(5N - 6) \Bigg]}{nK(N - K)(N - n)(N - 2)(N - 3)}$",
    "Negative Binomial": r"$ \dfrac{6}{r} + \dfrac{p^2}{r(1-p)} $", 
    "Negative HyperGeometry": "not defined in general case",
    "Uniform (descrete type)": "not defined in general case", 
    "Uniform (continuous type)": r"$\dfrac{9}{5}$", 
    "Normal": r"$0$", 
    "Exponential": "6", 
    "Student": r"<li> $\dfrac{6}{d-4}$ if $d > 4$ <br> <li> $\infty$ if $2 < d \leq 4$", 
    "Chi-squared": r"$\dfrac{12}{d}$",
    "Fisher": r"$ \frac{6(d_1 + d_2 - 2)(d_2 - 2)^2}{d_1(d_2 - 4)(d_2 - 6)} $", 
    "Beta": r"$\dfrac{6\left[(\alpha - \beta)^2 (\alpha + \beta + 1) - \alpha \beta (\alpha + \beta + 2)\right]}{\alpha \beta (\alpha + \beta + 2)(\alpha + \beta + 3)}$", 
    "Gamma": r"$\dfrac{6}{\alpha}$", 
    "Cauchy": "undefined"    
} 

charfunc_mapping = {
    "Bernoulli": r"$(1-p) + pe^{it}$ ",
    "Binomial": r"$ \left( (1-p) + pe^{it} \right)^n $",
    "Poisson": r"$\exp \left( \lambda \left( e^{it} - 1 \right) \right)$",
    "Geometry": r"$\dfrac{p}{1 - (1-p)e^{it}}$ if domain := $\lbrace 0,1,\ldots \rbrace$ <br> <br> $\dfrac{pe^{it} }{1 - (1-p)e^{it}}$ if domain := $\lbrace 1,2,\ldots \rbrace$",
    "HyperGeometry": r"$\frac{{N - K \choose n}}{{N \choose n}} \cdot {}_2F_1(-n, -K; N - K - n + 1; e^{it}) $", 
    "Negative Binomial": r"$\left( \frac{p}{1 - (1 - p)e^{it}} \right)^r \quad \text{with } t \in \mathbb{R} $", 
    "Negative HyperGeometry": "not defined in general case",
    "Uniform (descrete type)": r"$ \displaystyle k^{-1} \sum_{i=0}^k e^{it x_k} $", 
    "Uniform (continuous type)": r"<li> $\dfrac{e^{itb} - e^{ita}}{it(b - a)}$ if $t \neq 0$ <br> <li> $1$ if $t = 0$", 
    "Normal": r"$ \exp \left( i \mu t - \frac{\sigma^2 t^2}{2} \right) $", 
    "Exponential": r"$ \dfrac{\lambda}{\lambda - it} $", 
    "Student": r"$ \dfrac{(\sqrt{d} \cdot \vert t \vert )^{d/2} \cdot K_{d/2}(\sqrt{d}, \vert t \vert )}{\Gamma(d/2)\cdot 2^{d/2 - 1}} $ for $d > 0$ <br> where $K_d$ is the `modified Bessel function` of the second kind", 
    "Chi-squared": r"$ \left( 1 - 2it \right)^{d/2} $",
    "Fisher": "No closed-form", 
    "Beta": r"$ \displaystyle 1 + \sum_{k=1}^{\infty} \left( \prod_{r=0}^{k-1} \frac{\alpha + r}{\alpha + \beta + r} \right) \frac{(it)^k}{k!} $", 
    "Gamma": r"$ \left( 1 - \dfrac{it}{\lambda} \right)^{-\alpha} $", 
    "Cauchy": r"$\exp \left( \mu i t  - \sigma \vert t \vert \right)$"    
}

moment_gen_func_map = {
    "Bernoulli": r"$(1-p) + pe^{t}$ ",
    "Binomial": r"$ \left( (1-p) + pe^{t} \right)^n $",
    "Poisson": r"$\exp \left( \lambda \left( e^{t} - 1 \right) \right)$",
    "Geometry":r"$\dfrac{p}{1 - (1-p)e^{t}}$ if domain := $\lbrace 0,1,\ldots \rbrace$ <br> <br> $\dfrac{pe^{t} }{1 - (1-p)e^{t}}$ if domain := $\lbrace 1,2,\ldots \rbrace$",
    "HyperGeometry": r"$\dfrac{{N - K \choose n}}{{N \choose n}} \cdot {}_2F_1(-n, -K; N - K - n + 1; e^t) $ where ${}_2F_1 $ is the `generalized hypergeometric function`", 
    "Negative Binomial": r"$\left( \dfrac{p}{1 - (1 - p)e^t} \right)^r \quad \text{for } t < -\log(1 - p) $", 
    "Negative HyperGeometry": "not defined in general case",
    "Uniform (descrete type)":  r"$ \displaystyle k^{-1} \sum_{i=0}^k e^{t x_k} $", 
    "Uniform (continuous type)":  r"<li> $\dfrac{e^{tb} - e^{ta}}{t(b - a)}$ if $t \neq 0$ <br> <li> $1$ if $t = 0$", 
    "Normal": r"$ \exp \left( \mu t - \frac{\sigma^2 t^2}{2} \right) $", 
    "Exponential":  r"$ \dfrac{\lambda}{\lambda - t} $ for $t < \lambda$", 
    "Student": "undefined", 
    "Chi-squared": r"$ \left( 1 - 2t \right)^{d/2} $ for $t < \dfrac{1}{2}$",
    "Fisher": "does not exist", 
    "Beta": r"$ \displaystyle 1 + \sum_{k=1}^{\infty} \left( \prod_{r=0}^{k-1} \frac{\alpha + r}{\alpha + \beta + r} \right) \frac{t^k}{k!} $", 
    "Gamma":r"$ \left( 1 - \dfrac{t}{\lambda} \right)^{-\alpha} $ for $t < \lambda$", 
    "Cauchy": "does not exist"    
}

proba_gen_func_map = {
    "Bernoulli": r"$(1-p) + pz$ ",
    "Binomial": r"$ \left( (1-p) + pz \right)^n $",
    "Poisson": r"$\exp \left( \lambda \left( z - 1 \right) \right)$",
    "Geometry": r"$\dfrac{p}{1 - (1-p)z}$ if domain := $\lbrace 0,1,\ldots \rbrace$ <br> <br> $\dfrac{pz }{1 - (1-p)z}$ if domain := $\lbrace 1,2,\ldots \rbrace$",
    "HyperGeometry": "does not have a closed-form formula in general [until now]", 
    "Negative Binomial": r"$\left( \dfrac{p}{1 - (1 - p)z} \right)^r$ for $ \vert z \vert < \frac{1}{p} $", 
    "Negative HyperGeometry": "not defined in general case",
    "Uniform (descrete type)":  r"$ \displaystyle k^{-1} \sum_{i=0}^k z^{x_k} $", 
    "Uniform (continuous type)": "cts vrs does not exist PGF", 
    "Normal": "cts vrs does not exist PGF", 
    "Exponential": "cts vrs does not exist PGF", 
    "Student": "cts vrs does not exist PGF", 
    "Chi-squared": "cts vrs does not exist PGF",
    "Fisher": "cts vrs does not exist PGF", 
    "Beta": "cts vrs does not exist PGF", 
    "Gamma": "cts vrs does not exist PGF", 
    "Cauchy": "cts vrs does not exist PGF"
}

fisher_info_map = {
    "Bernoulli": r"$ \dfrac{1}{p(1-p)} $",
    "Binomial": r"$ \dfrac{n}{p( 1 - p)} $", 
    "Poisson": r"$\lambda^{-1}$",
    "Geometry": r"$\dfrac{1}{p^2(1 - p)}$",
    "HyperGeometry": "does not have a closed-form formula in general [until now]", 
    "Negative Binomial": r"$\dfrac{r}{p^2(1 - p)}$", 
    "Negative HyperGeometry": "not defined in general case",
    "Uniform (descrete type)": "not defined in general case", 
    "Uniform (continuous type)": r"$ \dfrac{1}{(b - a)^2} $", 
    "Normal": r"$ \begin{array}{ccl} \mathcal{I}(\mu, \sigma) &=& \begin{pmatrix} \sigma^{-2} & 0 \\ 0 & 2 \sigma^{-2} \end{pmatrix} \\ \mathcal{I}(\mu, \sigma^2) &=& \begin{pmatrix} \sigma^{-2} & 0 \\ 0 & \frac{1}{2}\sigma^{-4} \end{pmatrix} \end{array} $", 
    "Exponential":  r"$ \lambda^{-2} $", 
    "Student": r"$ \sigma^{-2} \begin{pmatrix} \frac{d + 1}{d} & 0 \\ 0 & \frac{2(d + 1)}{d} \end{pmatrix} $", 
    "Chi-squared": "No closed-form (numerical via log-likelihood)",
    "Fisher": "No closed-form (numerical via log-likelihood)", 
    "Beta": r"$\begin{bmatrix} \operatorname{var}[\ln X] & \operatorname{cov}[\ln X, \ln(1 - X)] \\ \operatorname{cov}[\ln X, \ln(1 - X)] & \operatorname{var}[\ln(1 - X)] \end{bmatrix} $", 
    "Gamma": r" $ \left( \begin{array}{cc} \psi^{(1)}(\alpha) & -\lambda^{-1} \\ -\lambda^{-1} & \alpha \lambda^{-2} \end{array} \right) $ where $\psi$ is the `digamma function` is defined as the logarithmic derivative of the `gamma function`, i.e. <br> $\qquad \quad \psi^{(1)}(z) = \dfrac{d}{dz} \Gamma(z) $", 
    "Cauchy": r"$\dfrac{1}{2\sigma^2}$"
}

entropy_mapping = {
    "Bernoulli": r"$ -p \log p - (1-p) \log (1-p) $",
    "Binomial": r" $\dfrac{1}{2} \log_2 \left( 2\pi e n p (1 - p) \right) + O\left( n^{-1} \right) $ ",
    "Poisson": r"$\begin{array}{ccl} \displaystyle \lambda \left[1 - \log(\lambda) \right] + e^{-\lambda} \sum_{k=0}^{\infty} \frac{\lambda^k \log(k!)}{k!} & & \text{or for large } \lambda \\ \approx \frac{1}{2} \log(2 \pi e \lambda) - \frac{1}{12 \lambda} - \frac{1}{24 \lambda^2} - \frac{19}{360 \lambda^3} + \mathcal{O} \left( \frac{1}{\lambda^4} \right) \end{array}$",
    "Geometry": r"$ \dfrac{-p \log p - (1-p) \log (1-p)}{p} $",
    "HyperGeometry": "does not have a closed-form formula in general [until now]", 
    "Negative Binomial": "does not have a closed-form formula in general [until now]", 
    "Negative HyperGeometry": "not defined in general case",
    "Uniform (descrete type)": "not defined in general case", 
    "Uniform (continuous type)": r"$ \ln (b-a) $", 
    "Normal": r"$ \ln \left( 2\pi e \sigma^2 \right) $", 
    "Exponential": r"$ 1 - \ln \lambda$", 
    "Student": r"$ \frac{d + 1}{2} \left[ \psi\left( \frac{d + 1}{2} \right) - \psi\left( \frac{d}{2} \right) \right] + \ln \left[ \sqrt{d} \, B\left( \frac{d}{2}, \frac{1}{2} \right) \right] $ <br> where $\psi, B$ are the `digamma function` and `Beta functions` respectively (check in Gamma and beta distribution) ", 
    "Chi-squared": r"$\dfrac{d}{2} + \ln \left( 2 \Gamma \left( \frac{d}{2} \right) \right) + \left( 1 - \frac{d}{2} \right) \psi \left( \frac{d}{2} \right)$ <br> where $\Gamma$ is `(upper) Gamma function` and $\psi$ is `dimgamma function`",
    "Fisher": r"$\begin{array}{ccl} H(X) &=& \ln \left( \frac{d_1}{d_2} \right)^{d_1/2} + \ln \mathrm{B}\left( \frac{d_1}{2}, \frac{d_2}{2} \right) + \left( 1 - \frac{d_1}{2} \right) \psi\left( \frac{d_1}{2} \right) \\ && - \left( 1 + \frac{d_2}{2} \right) \psi\left( \frac{d_2}{2} \right) + \left( \frac{d_1 + d_2}{2} \right) \psi\left( \frac{d_1 + d_2}{2} \right) \end{array}$ <br> where $B$ is `Beta function` and $\psi$ is `dimgamma function`", 
    "Beta": r"$\ln B(\alpha, \beta) - (\alpha - 1)\psi(\alpha) - (\beta - 1)\psi(\beta) + (\alpha + \beta - 2)\psi(\alpha + \beta) $", 
    "Gamma": r"$ \alpha - \ln \lambda + \ln \Gamma(\alpha) + (1 - \alpha) \psi(\alpha) $", 
    "Cauchy": r"$\log (4 \pi \sigma) $"
}

def get_distr_features(distr_name, features_name):
    if features_name == "Notation":
        return notation_map[distr_name]
    elif features_name == "Description":
        return description_map[distr_name]
    elif features_name == "Parameters":
        return params_mapping[distr_name]
    elif features_name == "Domain":
        return domain_mapping[distr_name]
    elif features_name == "pmf / pdf":
        return pdf_pmf_mapping[distr_name]
    elif features_name == "cdf":
        return cdf_mapping[distr_name]
    elif features_name == "Expectation":
        return expec_mapping[distr_name]
    elif features_name == "mode":
        return mode_mapping[distr_name]
    elif features_name == "median":
        return median_mapping[distr_name] 
    elif features_name == "variance":
        return variance_mapping[distr_name]
    elif features_name == "Kurtosis":
        return kurtosis_mapping[distr_name]
    elif features_name == "Skewness":
        return skewness_mapping[distr_name] 
    elif features_name == "Fisher information":
        return fisher_info_map[distr_name]
    elif features_name == "Entropy":
        return entropy_mapping[distr_name]
    elif features_name == "Characteristic func":
        return charfunc_mapping[distr_name]
    elif features_name == "Moment generating func":
        return moment_gen_func_map[distr_name]
    elif features_name == "Proba generating func":
        return proba_gen_func_map[distr_name]