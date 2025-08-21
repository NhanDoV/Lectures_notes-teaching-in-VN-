import streamlit as st
import pandas as pd

dict_notes = {
    "Replacement tips": ["Replacement vs numbers of failures"],
    "Distribution tips": ["For all continuous distr", "approximation rules", "Moment methods and deravative equation"], 
    "Markov chain": ["Markov process", "Martingale", "Filter-Adaption"], 
    "Regression": ["Assumptions"], 
    "Convergence Theorems": ["Central Limit Theorem", "Large Law Numbers"]
}

def Replacement_tips(note: str):
    df = pd.DataFrame({
        "": ["With replacements", "No replacements"],
        "Given number of draws": ["binomial distribution", "hypergeometric distribution"],
        "Given number of failures": ["negative binomial distribution", "negative hypergeometric distribution"]        
    })
    st.dataframe(df, hide_index=True)

def distr_tips(note: str):
    def cts_vrs_note():
        st.write("#### 1. Chi-squared distribution")
        st.write(r"For $Z_1, Z_2, \cdots, Z_d$ are $d$ `independent, standard normal rvs` $\mathcal{N}(0, 1)$, then the sum of their squares,")
        st.latex(r" \chi_d^2 = \sum_{k=1}^d Z_k^2 ")
        st.write("--------")
        st.write("#### 2. Student distribution")
        st.write(r"Student's t-distribution with $d$ `degrees of freedom` can be defined as the distribution of the random variable $T$ with")
        st.latex(r" T = \dfrac{\mathcal{N}(0, 1)}{\chi^2_d / d} ")
        st.write(r"where $\mathcal{N}(0, 1)$ and $\chi^2_d$ are independent")
        st.write("--------")
        st.write("#### 3. Fisher distribution")
        st.write(r"The F-distribution with $d_1$ and $d_2$ `degrees of freedom` is the distribution of")
        st.latex(r" F = \dfrac{\chi^2_{d_1} / d_1}{\chi^2_{d_2} / d_2} ")
    def approx_rule():
        st.subheader(note)
        st.write("#### Binomial ~ Poisson")
        st.latex(r" \mathcal{B}(n, p)  \overset{n \to \infty}{\approx} \mathcal{P}\left( np \right) ")
        st.markdown("<li> When events are rare but trials are many <br> <li> for <i>n</i> large while <i>p</i> is small enough but <i>np</i> is fixed and moderate",
                    unsafe_allow_html=True)
        st.write('----------')
        st.write("#### Binomial ~ Normal")
        st.latex(r" \mathcal{B}(n, p)  \overset{n \to \infty}{\longrightarrow} \mathcal{N}\left( np, \sqrt{np(1-p)} \right) ")
        st.markdown("<li> Converges by CLT <br> <li> for <i>n</i> large enough, <i>p</i> small enough <br> <li> <i>p</i> not close to 0 or 1 <br> <li> <i>np</i> and <i>1 - p</i> > 5", 
                    unsafe_allow_html=True)

    def moment_note():
        st.subheader(note)
        c1, _, c2 = st.columns([6, 1, 6])
        with c1:
            st.write("#### Moment methods")
            st.write(r"For any `statistic parametric distribution`, such as $\mathcal{N}(\mu, \sigma), B(\alpha, \beta)$, $\Gamma(\alpha, \lambda), \cdots$; then, we can estimate these parameters based on these 1-3 first moments. Generally, we define $\mu_k$ is the `empirical noncentral moment` of any variables for the $\mathbb{E} X^k$ - the `theorictical moment`")
            st.latex(r" \mu_k = n^{-1} \sum_{i=1}^n x_i^k ")
            st.write(r"and this is an `un-biased estimator` for $\mathbb{E}X^k$")
            st.write("------------")
            st.write("##### Example")
            st.latex(r" \begin{array}{l} X \sim \mathcal{N}(\mu, \sigma^2) \Rightarrow \left \lbrace \begin{array}{ccl} \mu &=& \mathbb{E} X \\ \sigma^2 &=& \mathbb{E}X^2 - (\mathbb{E}X)^2 \end{array} \right. \\ \\ X \sim B(\alpha, \beta) \Rightarrow \left \lbrace \begin{array}{ccl}  \alpha &=& \mathbb{E} X \cdot \left( \frac{ \mathbb{E}X (1 - \mathbb{E}X) }{\mathbb{E}X^2 - (\mathbb{E}X)^2} - 1 \right) \\  \beta &=& \left( 1 - \mathbb{E} X  \right)\cdot \left( \frac{ \mathbb{E}X (1 - \mathbb{E}X) }{\mathbb{E}X^2 - (\mathbb{E}X)^2} - 1 \right) \end{array} \right. \\ \end{array} ")            

        with c2:
            st.write("#### Finding high order moment")
            st.write("`Using CF (Characteristic function)`")
            st.latex(r" \mathbb{E}X^k = \frac{1}{i^{k}} \cdot \left. \left( \frac{d^k}{dt^k} \varphi_X(t) \right) \right \vert_{t=0} ")
            st.write("where")
            st.latex(r" \varphi_X(t) := \mathbb{E} e^{itX} ")
            st.write("------------")
            st.write("`Using MGF (Moment generating function)`")
            st.latex(r" \mathbb{E}X^k = \left. \left( \frac{d^k}{dt^k} M_X(t) \right) \right \vert_{t=0} ")
            st.write("where")
            st.latex(r" M_X(t) := \mathbb{E} e^{tX} ")
            st.write("------------")
            st.write("#### Finding proba with PGF")
            st.latex(r" P(X = k) = \dfrac{1}{k!} \left. \left( \frac{d^k}{dt^k} G_X(t) \right) \right \vert_{t=1}")
            st.write("where")
            st.latex(r" G_X(t) := \mathbb{E} t^{X} ")

    if note == "For all continuous distr":
        cts_vrs_note()
    elif note == "Moment methods and deravative equation":
        moment_note()
    else:
        approx_rule()    

def show_notes(tips_type:str, note: str):
    if tips_type == "Replacement tips":
        Replacement_tips(note)
    elif tips_type == "Distribution tips":
        dist_note = distr_tips(note)
        