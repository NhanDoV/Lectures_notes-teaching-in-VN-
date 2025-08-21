import streamlit as st 
import numpy as np
import matplotlib.pyplot as plt 

def bernoulli_all_proofs(note: str):
    from .distr_illus import bernoulli_show
    c1, _, c2 = st.columns([5, 1, 10])
    with c1:
        st.write("#### illustration")
        p = st.number_input("Select a value of `p`", value=0.2, min_value=0.01, max_value=1.0, help="Tham số xác suất thành công")         
        bernoulli_show(p)
    with c2:
        c21, c22 = st.columns(2)
        if note == "cdf":
            with c21:         
                st.write("#### proof of cdf") 
            with c22:
                button_trig = st.button("Show the proof") 
            if button_trig:
                st.write("We have the pmf of Bernoulli distributions defined by:")
                st.latex(r" P(X=x) = p^x (1-p)^{1-x} = \left\lbrace \begin{array}{cl} p & x = 1 \\ 1 - p & x = 0 \end{array} \right. ")
                st.write("Hence, the cdf (cumulative distribution function) will be")
                st.latex(r" P(X < x) = \displaystyle \sum_{k < x} P(X = k) = \left\lbrace \begin{array}{cl} 0 & x < 0 \\ 1 - p & x \in [0, 1) \\ 1 & x > 1 \end{array} \right. ")
                st.write("The first equality comes since the discrete variables")
        elif note == "Expectation":
            with c21:         
                st.write("#### proof of Expectation") 
            with c22:
                button_trig = st.button("Show the proof") 
            if button_trig:
                st.write("We have the pmf of Bernoulli distributions defined by:")
                st.latex(r" P(X=x) = p^x (1-p)^{1-x} = \left\lbrace \begin{array}{cl} p & x = 1 \\ 1 - p & x = 0 \end{array} \right. ")
                st.write("Therefore,")
                st.latex(r" \begin{array}{rcl} \mathbb{E}X &:=& \displaystyle \sum_{k=0}^1 x P(X = x) \\ &=& 0*P(X = 0) + 1*P(X = 1) &=& p \end{array}")
        elif note == "mode":
            with c21:   
                st.write("#### proof of Mode") 
            with c22:
                button_trig = st.button("Show the proof") 
            if button_trig:
                st.write("We have the pmf of Bernoulli distributions defined by:")
                st.latex(r" P(X=x) = p^x (1-p)^{1-x} = \left\lbrace \begin{array}{cl} p & x = 1 \\ 1 - p & x = 0 \end{array} \right. ")
                st.write("Hence,")
                st.latex(r"X_{\text{mode}} = \argmax_{x} P(X = x) \in \lbrace 0, 1 \rbrace ")
                st.write(r" $\bullet$ When $p < 0.5$ then $P(X = 0) = 1 - p > p = P(X = 1)$")
                st.write(r" $\bullet \qquad p > 0.5$ then $P(X = 1) = p > 1 - p = P(X = 0)$")
                st.write(r" $\bullet \qquad p = 0.5$ then $P(X = 0) = 1 - p = p = P(X = 1)$")
                st.write("Hence")
                st.latex(r"X_{\text{mode}} = \left\lbrace \begin{array}{cl} 0 & p < 0.5 \\ 1 & p > 0.5 \\ \lbrace 0, 1 \rbrace & p = 0.5 \end{array} \right. ")
        elif note == "median":
            with c21:         
                st.write("#### proof of median") 
            with c22:
                button_trig = st.button("Show the proof") 
            if button_trig:
                st.write("We have the pmf of Bernoulli distributions defined by:")
                st.latex(r" P(X=x) = p^x (1-p)^{1-x} = \left\lbrace \begin{array}{cl} p & x = 1 \\ 1 - p & x = 0 \end{array} \right. ")
                st.write("Hence")
                st.latex(r"X_{\text{median}} = \{ x_m : P(X \leq x_m) \geq 0.5 \text{ and } P(X \geq x_m) \geq 0.5 \}")
                st.write(r"$\bullet$ When $p < 0.5$ then $P(X \leq 0) = P(X = 0) = 1 - p > 0.5$")
                st.write(r"$\bullet \quad$  $p > 0.5$ then $P(X \geq 1) = P(X = 1) = p > 0.5$")
                st.write(r"$\bullet \quad$  $p = 0.5$ then $P(X \leq 0) = 0.5$ and $P(X \geq 1) = 0.5$")
                st.write("Hence")
                st.latex(r"X_{\text{median}} = \begin{cases} 0 & \text{if } p < 0.5 \\ 1 & \text{if } p > 0.5 \\ [0, 1] & \text{if } p = 0.5 \end{cases}") 
        elif note == "variance":
            with c21:
                st.write("#### proof of variance") 
            with c22:
                button_trig = st.button("Show the proof") 
            if button_trig:
                st.write("We have the pmf of Bernoulli distributions defined by:")
                st.latex(r" P(X=x) = p^x (1-p)^{1-x} = \left\lbrace \begin{array}{cl} p & x = 1 \\ 1 - p & x = 0 \end{array} \right. ")
                st.write("Hence")
                st.latex(r" \begin{array}{ccl} \text{Var} X &=& \mathbb{E} X^2 - \left( \mathbb{E} X \right)^2 \\ &=& \displaystyle \left[ \sum_{x=0}^1 x^2 P(X=x) \right] - p^2 \\ &=& p - p^2 \\ &=& p(1 - p) \end{array} ")
        elif note == "Skewness":
            with c21:
                st.write("#### proof of Skewness") 
            with c22:
                button_trig = st.button("Show the proof") 
            if button_trig:
                st.write("We have the pmf of Bernoulli distributions defined by:")
                st.latex(r" P(X=x) = p^x (1-p)^{1-x} = \left\lbrace \begin{array}{cl} p & x = 1 \\ 1 - p & x = 0 \end{array} \right. ")
                st.write("By the result of expectation and variance, we obtain")
                st.latex(r"\begin{array}{ccc} \mathbb{E}\left( \dfrac{ X - \mathbb{E} X }{ \sqrt{ \text{Var} X } } \right)^3 &=& \dfrac{ \mathbb{E} (X - p)^3 }{ \left[ p(1-p) \right]^{3/2} } \\ \\ &=& \dfrac{\mathbb{E}X^3 - 3p \mathbb{E}X^2 + 3p^2 \mathbb{E}X - p^3 }{p(1-p)\sqrt{p(1-p)}} \\ \\ &=& \dfrac{p - 3p^2 + 3p^3 - p^3}{p(1-p)\sqrt{p(1-p)}} \\ \\ &=& \dfrac{p(2p^2 - 3p + 1)}{p(1-p)\sqrt{p(1-p)}} \\ \\ &=& \dfrac{1-2p}{\sqrt{p(1-p)}} \end{array}")
        elif note == "Kurtosis":
            with c21:
                st.write("#### proof of Kurtosis") 
            with c22:
                button_trig = st.button("Show the proof") 
            if button_trig:
                st.write("We have the pmf of Bernoulli distributions defined by:")
                st.latex(r" P(X=x) = p^x (1-p)^{1-x} = \left\lbrace \begin{array}{cl} p & x = 1 \\ 1 - p & x = 0 \end{array} \right. ")
                st.write("By the result of expectation and variance, we obtain")
                st.latex(r"\begin{array}{ccc} \mathbb{E}\left( \dfrac{ X - \mathbb{E} X }{ \sqrt{ \text{Var} X } } \right)^4 &=& \dfrac{ \mathbb{E} (X - p)^4 }{ \left[ p(1-p) \right]^{2} } \\ \\ &=& \dfrac{\mathbb{E}X^4 - 4p \mathbb{E}X^3 + 6p^2 \mathbb{E}X^2 - 4p \mathbb{E}X + p^4 }{p^2(1-p)^2} \\ \\ &=& \dfrac{p - 4p^2 + 6p^3 - 4p^4 + p^4}{p^2(1-p)^2} \\ \\ &=& \dfrac{-p(3p^3 - 6p^2 + 4p - 1)}{p^2(1-p)^2} \\ \\ &=& \dfrac{1-6p(1-p)}{p(1-p)} \end{array}")
        elif note == "Characteristic func":
            with c21:
                st.write("#### proof of Characteristic function") 
            with c22:
                button_trig = st.button("Show the proof") 
            if button_trig:
                st.write("We have the pmf of Bernoulli distributions defined by:")
                st.latex(r" P(X=x) = p^x (1-p)^{1-x} = \left\lbrace \begin{array}{cl} p & x = 1 \\ 1 - p & x = 0 \end{array} \right. ")
                st.write("Hence")
                st.latex(r"\begin{array}{ccl} \varphi_X(t) &:=& \mathbb{E} e^{itX} \\ &=& \displaystyle \sum_{x=0}^1 e^{itx} P(X = x) \\ &=& p e^{it*1} + (1 - p)e^{it*0} &=& (1-p) + pe^{it} \end{array}")
        elif note == "Moment generating func":
            with c21:
                st.write("#### proof of Moment generating function") 
            with c22:
                button_trig = st.button("Show the proof") 
            if button_trig:
                st.write("We have the pmf of Bernoulli distributions defined by:")
                st.latex(r" P(X=x) = p^x (1-p)^{1-x} = \left\lbrace \begin{array}{cl} p & x = 1 \\ 1 - p & x = 0 \end{array} \right. ")
                st.write("Hence")
                st.latex(r"\begin{array}{ccl} M_X(t) &:=& \mathbb{E} e^{tX} \\ &=& \displaystyle \sum_{x=0}^1 e^{tx} P(X = x) \\ &=& p e^{t*1} + (1 - p)e^{t*0} &=& (1-p) + pe^{t} \end{array}")
        elif note == "Proba generating func":
            with c21:
                st.write("#### proof of Probability generating function") 
            with c22:
                button_trig = st.button("Show the proof") 
            if button_trig:
                st.write("We have the pmf of Bernoulli distributions defined by:")
                st.latex(r" P(X=x) = p^x (1-p)^{1-x} = \left\lbrace \begin{array}{cl} p & x = 1 \\ 1 - p & x = 0 \end{array} \right. ")
                st.write("Hence")
                st.latex(r"\begin{array}{ccl} P_X(t) &:=& \mathbb{E} z^X \\ &=& \displaystyle \sum_{x=0}^1 z^x P(X = x) \\ &=& p z^1 + (1 - p)z^{0} &=& (1-p) + pz \end{array}")
        elif note == "Fisher information":
            with c21:
                st.write("#### proof of Fisher information") 
            with c22:
                button_trig = st.button("Show the proof") 
            if button_trig:
                st.write("We have the pmf of Bernoulli distributions defined by:")
                st.latex(r" P(X=x) = p^x (1-p)^{1-x} = \left\lbrace \begin{array}{cl} p & x = 1 \\ 1 - p & x = 0 \end{array} \right. ")
                st.write("Hence")
                st.latex(r"\begin{array}{ccl} I_{(\theta = p)}^X &=& \mathbb{E} \left( \left. \dfrac{d}{d \theta} \log f(X, \theta) \right\vert \theta = p\right)^2 \\ &=& \mathbb{E} \left( \dfrac{d}{d p} \log \left[ p^X (1 - p)^{1 - X} \right] \right)^2 \\ &=& \mathbb{E} \left( \dfrac{d}{d p} \left[ X \log p + (1 - X) \log (1-p) \right] \right)^2 \\ &=& \mathbb{E} \left( \left[ \dfrac{X}{p} - \dfrac{1 - X}{1 - p} \right] \right)^2 \\ &=& \dfrac{ \mathbb{E} (X - p)^2 }{p^2(1-p)^2} = \dfrac{ \text{Var} X }{p^2(1-p)^2} = \dfrac{1}{p(1-p)}\end{array}")
        elif note == "Entropy":
            with c21:
                st.write("#### proof of Entropy") 
            with c22:
                button_trig = st.button("Show the proof") 
            if button_trig:
                st.write("We have the pmf of Bernoulli distributions defined by:")
                st.latex(r" P(X=x) = p^x (1-p)^{1-x} = \left\lbrace \begin{array}{cl} p & x = 1 \\ 1 - p & x = 0 \end{array} \right. ")
                st.write("Hence")
                st.latex(r"\begin{array}{ccl} H(X, p) &=& \mathbb{E} \left( - \log f(X, p) \right) \\ &=& - \mathbb{E} \left[ X \log p + (1-X) \log(1-p) \right] \\ &=& - \left[\log p \cdot \mathbb{E} X +\log(1-p) \cdot \mathbb{E}(1 - X) \right] \\&=& - p \log p - (1 - p) \log(1- p) \end{array}")

def binomial_all_proofs(note: str):
    from .distr_illus import binomial_show
    c1 ,_, c2 = st.columns([5,1,10])
    with c1:
        st.write("#### illustration")
        c11, c12 = st.columns(2)
        with c11:
            p = st.number_input("Select a value of `p`", value=0.2, min_value=0.01, max_value=1.0, help="Tham số xác suất thành công")
        with c12:
            n = st.number_input("Select value of `n`", value=20, min_value=5, max_value=200)
        binomial_show(n, p)
    with c2:
        st.write("We have some notes in this distributions")
        st.latex(r" \begin{array}{rcl}  \displaystyle \sum_{k=0}^{n} \binom{n}{k} a^k b^{n-k} &=& (a + b)^n \\ \displaystyle k \binom{n}{k} &=& \displaystyle n \binom{n-1}{k-1} \\ k^2 &=& k(k-1) + k \\ k^3 &=& k(k-1)(k-2) + 6k(k-1) + k \\ k^4 &=& k(k-1)(k-2)(k-3) + 6k(k-1)(k-2) + 7k(k-1) + k \end{array} ")
        c21, c22 = st.columns(2)
        if note == "cdf":
            with c21:
                st.write("#### proof of cdf") 
            with c22:
                button_trig = st.button("Show the proof") 
            if button_trig:
                st.write("We have the pmf of Binomial distribution defined by:")
                st.latex(r" P(X=x) = \binom{n}{x} p^x (1-p)^{n-x} ")
                st.write("Hence")
                st.latex(r" P(X \leq x) = \sum_{k=0}^x P(X = k) = \sum_{k=0}^x \binom{n}{k} p^k (1-p)^{n-k} ")
        elif note == "Expectation":
            with c21:
                st.write("#### proof of Expectation") 
            with c22:
                button_trig = st.button("Show the proof") 
            if button_trig:
                st.write("#### Approach 1")
                st.write("We have the pmf of Binomial distribution defined by:")
                st.latex(r" P(X=x) = \binom{n}{x} p^x (1-p)^{n-x} ")
                st.write("Hence")
                st.latex(r"\begin{array}{lcl} \mathbb{E}X &=& \displaystyle \sum_{k=0}^n k \left(\begin{array}{c} n \\ k \end{array}\right) p^k (1-p)^{n-k} \\ &=& \displaystyle \sum_{k=1}^n \left[ k \left(\begin{array}{c} n \\ k \end{array}\right) \right] p^k (1-p)^{n-k} \\ &=& \displaystyle \sum_{i=k-1}^{n-1} \left[ n \left(\begin{array}{c} n - 1 \\ k - 1 \end{array}\right) \right] p^{i+1} (1-p)^{n-(k + 1)} \\ & = & np \displaystyle \sum_{i=0}^{n-1} \left(\begin{array}{c} n - 1 \\ i \end{array}\right) p^i (1-p)^{(n-1)-i} \\ \\ & = & np \left[ p + (1-p) \right]^{n-1} \\ \\ &=& np \end{array} ")
                st.write("The `4th equality` follows from")
                st.latex(r"k * \dfrac{n!}{k! (n-k)!} = n * \dfrac{(n - 1)!}{(k - 1)! (n - 1 -k)!} ")
                st.write("----------")
                st.write("#### Approach 2")
                st.write("By the `identically independent assumption` of bernoulli variables,")
                st.latex(r"\mathbb{E} \mathcal{B}(n, p) = \mathbb{E} \left( \sum_{i=1}^n \mathcal{B}(1, p) \right) = \sum_{i=1}^n \mathbb{E} \mathcal{B}(1, p) = n \mathbb{E}  \mathcal{B}(1, p) = np")
                st.write("----------")
                st.write("#### Approach 3")
                st.write("By the result of charactersistic function of binomial: ")
                st.latex(r"\varphi_X(t) = \left( (1-p) + pe^{it} \right)^n")
                st.write("Then")
                st.latex(r" \begin{array}{ccl} \mathbb{E}X := \displaystyle \frac{1}{i} \left( \frac{d}{dt} \varphi_X(t) \right) \Bigg|_{t=0} &=& \displaystyle \frac{1}{i} \left( \frac{d}{dt} \left( (1-p) + pe^{it} \right)^n \right) \Bigg|_{t=0} \\ &=& \displaystyle \dfrac{1}{i} \left( npi e^{it} \cdot \left( (1-p)+pe^{it}) \right)^{n-1} \right) \Bigg|_{t=0} &=& np\end{array} ")
                st.write("----------")
                st.write("#### Approach 4")
                st.write("By the result of MGF (moment generating function), we have")
                st.latex(r"M_X(t) = \left( (1-p) + pe^{t} \right)^n")
                st.write("Then")
                st.latex(r" \begin{array}{ccl} \mathbb{E}X := \displaystyle \left( \frac{d}{dt} M_X(t) \right) \Bigg|_{t=0} &=& \displaystyle \left( \frac{d}{dt} \left( (1-p) + pe^{t} \right)^n \right) \Bigg|_{t=0} \\ &=& \displaystyle \left( np e^{t} \cdot \left( (1-p)+pe^{t}) \right)^{n-1} \right) \Bigg|_{t=0} &=& np\end{array} ")
        elif note == "mode":
            with c21:
                st.write("#### proof of mode")
            with c22:
                button_trig = st.button("Show the proof") 
            if button_trig:
                st.write("We have the pmf of Binomial distribution defined by:")
                st.latex(r" P(X=x) = \binom{n}{x} p^x (1-p)^{n-x} ")
                st.write("Hence")
                st.latex(r" \begin{array}{ccl} x_{\text{mode}}^{*} &=& \underset{0 \leq k \leq n}{\arg\max} \; \mathbb{P} (X = k) \\ \\ &=& \underset{0 \leq k \leq n}{\arg\max} \left[ \left(\begin{array}{c} n\\ k \end{array}\right) p^k (1-p)^{n-k} \right] \\ \\ &=& \left\lbrace \text{ floor} [p(n+1)] ; \text{ ceil} [p(n+1)] - 1  \rbrace\right. \end{array} ")
        elif note == "median":
            with c21:
                st.write("#### proof of median")
            with c22:
                button_trig = st.button("Show the proof") 
            if button_trig:
                st.write("We have the pmf of Binomial distribution defined by:")
                st.latex(r" P(X=x) = \binom{n}{x} p^x (1-p)^{n-x} ")
                st.write("Hence")
                st.latex(r"X_{\text{median}} = \{ x_m : P(X \leq x_m) \geq 0.5 \text{ and } P(X \geq x_m) \geq 0.5 \}")
                st.latex(r"\lfloor np \rfloor \leq X_{\text{median}} \leq \lceil np \rceil")
                st.write("Therefore")
                st.latex(r"X_{\text{median}} = \lfloor np \rfloor \text{ or } \lceil np \rceil ")
        elif note == "variance":
            with c21:
                st.write("#### proof of variance")
            with c22:
                button_trig = st.button("Show the proof") 
            if button_trig:
                st.write("#### Approach 1")
                st.write("By the assumption summing 𝑛 n i.i.d. Bernoulli variables")
                st.latex(r" \text{Var} X = \text{Var} \left( \sum_{i=1}^n \mathcal{B}(1, p) \right) = \sum_{i=1}^n \text{Var} \mathcal{B}(1, p) = n \text{Var} \mathcal{B}(1, p) = np(1-p)")
                st.write("----")
                st.write("#### Approach 2")
                st.write("We have the pmf of Binomial distribution defined by:")
                st.latex(r" P(X=x) = \binom{n}{x} p^x (1-p)^{n-x} ")
                st.write("Hence")
                st.latex(r" \begin{array}{ccl} \mathbb{E} X^2 := \displaystyle \sum_{k=0}^n k^2 P(X = k) &:=& \displaystyle \sum_{k=0}^n k^2 \cdot \left( \binom{n}{k} p^k (1 - p)^{n-k} \right) \\ &=& \displaystyle \sum_{k=0}^n \left( k(k-1) + k \right) \binom{n}{k} p^k (1 - p)^{n-k} \\ &=& A + B \end{array} ")
                st.write("where")
                st.latex(r" \begin{array}{ccl} A &:=& \displaystyle \sum_{k=0}^n \left(k(k-1) \binom{n}{k} \right) \cdot p^k(1-p)^{n-k} \qquad \text{since the first 2 elements are } 0 \\ &=& \displaystyle \sum_{k=2}^n \left(k(k-1) \binom{n}{k} \right) \cdot p^k(1-p)^{n-k} \\ &=& \displaystyle \sum_{k=2}^n \left( n(n-1) \binom{n-2}{k-2}\right) p^k(1-p)^{n-k} \qquad \text{by letting } i = k -2 \\ &=&  \displaystyle n(n-1) p^2 \left[ \sum_{i=0}^{n-2} \binom{n-2}{i} p^i(1-p)^{n-2-i} \right] \\ &=& n(n - 1)p^2 \end{array} ")
                st.write("and")
                st.latex(r" \begin{array}{ccl} B &:=& \displaystyle \sum_{k=0}^n \left(k \binom{n}{k} \right) \cdot p^k(1-p)^{n-k} \\ &=& \displaystyle \sum_{k=0}^n k P(X = k) &=& \mathbb{E} X &=& np \end{array} ")
                st.write("Therefore")
                st.latex(r" \text{Var} X = \mathbb{E} X^2 - \left( \mathbb{E} X \right)^2 = \left[ n(n - 1) p^2 + np \right] - (np)^2 = np(1 - p) ") 
                st.write("----")
                st.write("#### Approach 3")
                st.write("You can use one of MGF or CF to deduce the 2nd order moment, for exampless")
                st.latex(r" \begin{array}{ccl} \mathbb{E}X^2 := \displaystyle \left( \frac{d^2}{dt^2} M_X(t) \right) \Bigg|_{t=0} &=& \displaystyle \left( \frac{d^2}{dt^2} \left( (1-p) + pe^t \right)^n \right) \Bigg|_{t=0} \\ &=& \left( n(n-1)p^2e^t \cdot \left( (1-p) + pe^t \right)^{n-2} + npe^t \cdot \left( (1-p) + pe^t \right)^{n-1} \right)\Bigg|_{t=0} \\ &=& n(n-1)p^2 + np \end{array} ")
        elif note == "Skewness":
            with c21:
                st.write("#### proof of Skewness")
            with c22:
                button_trig = st.button("Show the proof") 
            if button_trig:
                st.write("Generally, we have")
                st.latex(r" \begin{array}{ccl} \mathbb{E} \left( \dfrac{ X - \mathbb{E}X }{\sqrt{\text{Var}X}} \right)^3 &=& \dfrac{ \mathbb{E}X^3 - 3np\mathbb{E}X^2 + 3(np)^2 \mathbb{E}X - (np)^3 }{np(1-p)\sqrt{np(1-p)}} \\ &=& \dfrac{\mathbb{E}X^3 - 3np \cdot \left( n(n-1)p^2 + np \right) + 3(np)^2 \cdot (np) - (np)^3}{np(1-p)\sqrt{np(1-p)}} \\ &=& \dfrac{\mathbb{E}X^3 - 3np \cdot \left( (np)^2 + np(1-p) \right) + 2(np)^3}{np(1-p)\sqrt{np(1-p)}} \\ &=& \dfrac{\mathbb{E}X^3 - (np)^3 - 3(np)^2(1 - p)}{np(1-p)\sqrt{np(1-p)}} \end{array} ")
                st.write("To compute the 3rd order moment, we can apply one of 2 following methods")
                st.write("---------")
                st.write("#### Approach 1 \n Using one of MGF or CF,")
                st.latex(r"\begin{array}{ccl} \mathbb{E}X^3 := \displaystyle \left( \frac{d^3}{dt^3} M_X(t) \right) \Bigg|_{t=0} &=& \displaystyle \left( \frac{d^3}{dt^3} \left( (1-p) + pe^t \right)^n \right) \Bigg|_{t=0} \\ &=& n(n-1)(n-2)p^3 + 3n(n - 1)p^2 + np \end{array}")
                st.write("---------")
                st.write("#### Approach 2 \n Expand the pmf of 3rd moment, noting that")
                st.latex(r" \begin{array}{ccl} k^3 = k\cdot( k(k - 1) + k ) &=& k \cdot ( (k-1)(k-2+2) + k ) \\ &=& k\left[ (k-1)(k-2) + 2(k-1) + k \right] \\ &=& k(k-1)(k-2) + \left[ 2k(k-1) + k^2 \right] \\ &=& k(k-1)(k-2) + 3k(k-1) + k \end{array} ")
                st.write("So")
                st.latex(r" \begin{array}{ccl} \mathbb{E}X^3 &:=& \displaystyle \sum_{k=0}^n k^3 \binom{n}{k} p^k(1-p)^{n-k} \\ &=& \displaystyle \sum_{k=0}^n \left[ k(k-1)(k-2) + 2k(k-1) + k \right] \cdot \binom{n}{k} p^k(1-p)^{n-k} &:=& A+B+C \end{array} ")
                st.write("where")
                st.latex(r""" \begin{array}{ccl} A &:=& \displaystyle \sum_{k=0}^n k(k-1)(k-2)\binom{n}{k} p^k(1-p)^{n-k} \quad \text{noting that the first 3 elements be zeros} \\ &=& \displaystyle \sum_{k=3}^n n(n-1)(n-2)\binom{n-3}{k-3} p^k (1-p)^{n-k} \quad \text{now letting } i = k-3 \\ &=& n(n-1)(n-2)p^3\displaystyle \sum_{k=0}^{n-3} \binom{n-3}{i} p^i (1 - p)^{n-i} \\ &=& n(n-1)(n-2)p^3 \\ B &:=& \displaystyle \sum_{k=0}^n 3k(k-1)\binom{n}{k} p^k(1-p)^{n-k} \quad \text{the first 2 elements be zeros} \\ &=& 3 \displaystyle \sum_{k=2}^n n(n-1)\binom{n-2}{k-2} p^k(1-p)^{n-k} \\ &=& 3 n(n-1) p^2 \\ C &:=& \displaystyle \sum_{k=0}^n k \binom{n}{k} p^k(1-p)^{n-k} = np \end{array} """)
                st.write("----------")
                st.write("Therefore")
                st.latex(r" \begin{array}{ccl} \mathbb{E} \left( \dfrac{ X - \mathbb{E}X }{ \sqrt{\text{Var}X} } \right)^3 &=& \dfrac{\mathbb{E}X^3 - (np)^3 - 3(np)^2(1-p)}{np(1-p)\sqrt{np(1-p)}} \\ &=& \dfrac{np\left(\left[ (n-1)(n-2)p^2 + 3(n-1)p + 1 \right] - (np)^2 - 3np(1-p) \right)}{np(1-p)\sqrt{np(1-p)}} \\ &=& \dfrac{\left[ (n^2-3n+2)p^2 -3p + 1 - (np)^2 + 3np^2 \right]}{(1-p)\sqrt{np(1-p)}} \\ &=& \dfrac{2p^2 -3p+1}{(1-p)\sqrt{np(1-p)}} \\ &=& \dfrac{1-2p}{\sqrt{np(1-p)}} \end{array} ")
        elif note == "Kurtosis":
            with c21:
                st.write("#### proof of Kurtosis")
            with c22:
                button_trig = st.button("Show the proof") 
            if button_trig:
                st.write("Generally, we have")
                st.latex(r" \begin{array}{ccl} \mathbb{E} \left( \dfrac{ X - \mathbb{E}X }{ \sqrt{\text{Var}X} } \right)^4 &=& \dfrac{ \mathbb{E}X^3 - 4np\mathbb{E}X^3 + 6(np)^2 \mathbb{E}X^2 - 4(np)^3 \mathbb{E}X + (np)^4 }{n^2p^2(1-p)^2} \\ &=& \dfrac{\mathbb{E}X^4 - 4np \cdot \left( n(n-1)(n-2)p^3 + 3n(n-1)p^2 + np \right)}{n^2p^2(1-p)^2} \\ & & + \dfrac{ 6 (np)^2 (n(n-1)p + (np)^2) - 4(np)^3\cdot(np) + (np)^4}{n^2p^2(1-p)^2} \\ &=& \dfrac{\mathbb{E}X^4 - 4(np)^2 \cdot \left[(n-1)(n-2)p^2 + 3(n-1)p + 1 + 6n(n-1)p + 3(np)^2 \right]}{n^2p^2(1-p)^2} \end{array} ")
                st.write("To compute the 4th order moment, we can apply one of 2 following methods")
                st.write("---------")
                st.write("#### Approach 1 \n Using one of MGF or CF,")
                st.latex(r" \begin{array}{ccl} \mathbb{E}X^4 := \displaystyle \left( \frac{d^4}{dt^4} M_X(t) \right) \Bigg|_{t=0} &=& \displaystyle \left( \frac{d^4}{dt^4} \left( (1-p) + pe^t \right)^n \right) \Bigg|_{t=0} \\ \\ &=& n(n-1)(n-2)(n-3)p^4 + 6n(n - 1)(n-2)p^3 + 7n(n-1)p^2 + np \end{array} ")
                st.write("---------")
                st.write("#### Approach 2 \n Expand the pmf of 3rd moment, noting that")
                st.latex(r" \begin{array}{ccl} k^4 = k\cdot k^3 &=& (k-3 + 3)\cdot( k(k-1)(k-2) + 3k(k-1) + k) \\&=& k(k-1)(k-2)(k-3) + 6k(k-1)(k-2) + 7k(k-1) + k \end{array} ")
                st.write("So")
                st.latex(r" \begin{array}{ccl} \mathbb{E}X^4 &:=& \displaystyle \sum_{k=0}^n k^4 \binom{n}{k} p^k(1-p)^{n-k} \\ &=& \displaystyle \sum_{k=0}^n \left[ k(k-1)(k-2) + 6k(k-1)(k-2) + 7k(k-1) + k \right] \cdot \binom{n}{k} p^k(1-p)^{n-k} \\ &:=& A+B+C+D \end{array} ")
                st.write("where")
                st.latex(r" \begin{array}{ccl} A &:=& \displaystyle \sum_{k=0}^n k(k-1)(k-2)(k-3)\binom{n}{k} p^k(1-p)^{n-k} \quad \text{noting that the first 4 elements be zeros} \\ &=& \displaystyle \sum_{k=4}^n n(n-1)(n-2)(n-3)\binom{n-4}{k-4} p^k (1-p)^{n-k} \quad \text{now letting } i = k-4 \\ &=& n(n-1)(n-2)(n-3)p^4\displaystyle \sum_{k=0}^{n-4} \binom{n-4}{i} p^i (1 - p)^{n-i} \\ &=& n(n-1)(n-2)(n-3)p^4 \\ B &:=& \displaystyle \sum_{k=0}^n 6k(k-1)(k-2)\binom{n}{k} p^k(1-p)^{n-k} \quad \text{the first 3 elements be zeros} \\ &=& 6 \displaystyle \sum_{k=3}^n n(n-1)(n-2)\binom{n-3}{k-3} p^k(1-p)^{n-k} \\ &=& 6 n(n-1)(n-2) p^3 \\ C&:=& \displaystyle \sum_{k=0}^n 7k(k-1) \binom{n}{k} p^k(1-p)^{n-k} = 7n(n-1)p^2 \\ D &:=& \displaystyle \sum_{k=0}^n k \binom{n}{k} p^k(1-p)^{n-k} = np \end{array} ")
                st.write("-----------")
                st.write("Therefore")
                st.latex(r" \begin{array}{ccl} \mathbb{E} \left( \dfrac{ X - \mathbb{E}X }{\sqrt{\text{Var}X} } \right)^4 &=& \dfrac{np \left( 1 - 7p + 12p^2 - 6p^3 \right)}{n^2p^2(1-p)^2} \\ &=& \dfrac{np(1-p)(1 - 6p + 6p^2)}{n^2p^2(1-p)^2} \\ &=& \dfrac{1 - 6p(1-p)}{np(1-p)} \end{array} ")
        elif note == "Characteristic func":
            with c21:
                st.write("#### proof of CF")
            with c22:
                button_trig = st.button("Show the proof") 
            if button_trig:
                st.write("By definition, we have")
                st.latex(r" \begin{array}{ccl} \varphi_X(t) := \mathbb{E} e^{itX} &=& \displaystyle \sum_{x=0}^n e^{itx} \cdot \left( \binom{n}{x} p^x (1-p)^{n-x} \right) \\ &=& \displaystyle \sum_{x=0}^n \binom{n}{x} \cdot \left( pe^{it} \right)^x \cdot (1 - p)^{n-x} \\ &=& \left( (1-p) + pe^{it} \right)^n \end{array} ")
        elif note == "Moment generating func":
            with c21:
                st.write("#### proof of MGF")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("By definition, we have")
                st.latex(r"\begin{array}{ccl} M_X(t) := \mathbb{E} e^{tX} &=& \displaystyle \sum_{x=0}^n e^{tx} \cdot \left( \binom{n}{x} p^x (1-p)^{n-x} \right) \\ &=& \displaystyle \sum_{x=0}^n \binom{n}{x} \cdot \left( pe^{t} \right)^x \cdot (1 - p)^{n-x} \\ &=& \left( (1-p) + pe^{t} \right)^n \end{array}") 
        elif note == "Proba generating func":
            with c21:
                st.write("#### proof of PGF")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("By definition, we have")
                st.latex(r" \begin{array}{ccl} G_X(t) := \mathbb{E} z^{X} &=& \displaystyle \sum_{x=0}^n z^{x} \cdot \left( \binom{n}{x} p^x (1-p)^{n-x} \right) \\ &=& \displaystyle \sum_{x=0}^n \binom{n}{x} \cdot \left( pz \right)^x \cdot (1 - p)^{n-x} \\ &=& \left( (1-p) + pz \right)^n \end{array} ")                                           
        elif note == "Fisher information":
            with c21:
                st.write("#### proof of Fisher information")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("By definition, we have")
                st.latex(r" \begin{array}{ccl} I_{(\theta = p)}^X &=& \mathbb{E} \left( \left. \dfrac{d}{d \theta} \log f(X, \theta) \right\vert \theta = p\right)^2 \\ &=& \mathbb{E} \left( \dfrac{d}{d p} \log \left[ \binom{n}{X} p^X (1 - p)^{n - X} \right] \right)^2 \\ &=& \mathbb{E} \left( \dfrac{d}{d p} \left[ X \log p + (n - X) \log (1-p) + \log \left[ \binom{n}{X} \right] \right] \right)^2 \\ &=& \mathbb{E} \left( \left[ \dfrac{X}{p} - \dfrac{n - X}{1 - p} \right] \right)^2 \\ &=& \dfrac{ \mathbb{E} (X - np)^2 }{p^2(1-p)^2} = \dfrac{ \text{Var} X }{p^2(1-p)^2} = \dfrac{n}{p(1-p)}\end{array} ")
                st.write("----------")
                st.write("Another approach: using the summing of `n-independent identical Bernoulli`")
                st.latex(r" I_{p}^{\mathcal{B}(n, p)} = I_{p}^{ \sum_{i=1}^n \mathcal{B}(1, p)} = n I_{p}^{\mathcal{B}(1, p)} = \dfrac{n}{p(1-p)}")
        elif note == "Entropy":
            with c21:
                st.write("#### proof of Entropy")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("By definition, we have")
                st.latex(r" H(X, p):= \mathbb{E} \left( -\log f(X, p) \right) = \displaystyle -\sum_{x=0}^n \log f(X, p) \cdot P(X=x) ")
                st.write("Hence")
                st.latex(r" \begin{array}{ccl} H(X, p) &=& \displaystyle -\sum_{k=0}^n \binom{n}{k}p^k(1-p)^{n-k} \cdot \log \left[ \binom{n}{k}p^k(1-p)^{n-k} \right] \\ &=& \displaystyle -\sum_{k=0}^n \binom{n}{k}p^k(1-p)^{n-k}\cdot \left[ k \log p + (n-k) \log(1-p) + \log \binom{n}{k} \right] \\ &:=& A + B + C \end{array} ")
                st.write("where")
                st.latex(r" \begin{array}{ccl} A &:=& \displaystyle - \sum_{k=0}^n \left( k \log p \right) \cdot \left( \binom{n}{k}p^k(1-p)^{n-k} \right) \\ &=& - \log p \displaystyle \sum_{k=0}^n k \binom{n}{k} p^k (1-p)^{n-k} \quad = \quad \mathbb{E} X &=&-np \log p \\ B &:=& \displaystyle - \sum_{k=0}^n \left( (n-k) \log (1-p) \right) \cdot \left( \binom{n}{k}p^k(1-p)^{n-k} \right) = \mathbb{E}(n - X) &=& -(n-np) \\ C &:=& \displaystyle - \sum_{k=0}^n \left( \log \binom{n}{k} \right) \cdot \left( \binom{n}{k}p^k(1-p)^{n-k} \right) \\ &=& - \displaystyle \mathbb{E} \log \binom{n}{X} \qquad \text{Then, apply Stirling’s approximation} & \approx & \displaystyle \binom{n}{ \lceil np \rceil } \end{array} ")
                st.write("Therefore")
                st.latex(r" H(X, p) \approx - n \left[ p \log p + (1-p) \log(1 - p) \right] + \log \binom{n}{ \lceil np \rceil } ")
                st.write("--------")
                st.write("For n large enough, then")
                st.latex(r" H(X, p) \approx \dfrac{1}{2} \log \left( 2 \pi e np(1-p) \right) + O \left( n^{-1} \right) ")
                st.write("by `normal approximation` ")

def poisson_all_proofs(note: str):
    from .distr_illus import poisson_show
    c1, _, c2 = st.columns([5, 1, 10])
    with c1:
        st.write("#### illustration")
        lamb = st.number_input("Select a value of `lambda`", value=2.0, min_value=0.01)         
        poisson_show(lamb)
    with c2:
        st.write("We have some notes in this distributions")
        st.latex(r" \begin{array}{ccl} \displaystyle \sum_{k=0}^{\infty} \dfrac{t^k}{k!} = e^t & \text{and} & \displaystyle \dfrac{d^k}{dt^k} \exp\left( \lambda \left( e^t - 1 \right) \right) = \left( \sum_{i=1}^k a_i \left( \lambda e^t \right)^i \right) \cdot \exp\left( \lambda \left( e^t - 1 \right) \right) \end{array} ")        
        c21, c22 = st.columns(2)
        if note == "cdf":
            with c21:
                st.write("#### proof of cdf") 
            with c22:
                button_trig = st.button("Show the proof") 
            if button_trig:
                st.write("We have the pmf of Poisson distribution defined by:")
                st.latex(r" P(X = k) = \dfrac{\lambda^k e^{-\lambda}}{k!} ")
                st.write("Hence")
                st.latex(r" P(X \leq x) = \sum_{k=0}^x P(X = k) = \sum_{k=0}^x \dfrac{\lambda^k e^{-\lambda}}{k!} ") 
        elif note == "Expectation":
            c21, c22 = st.columns(2) 
            with c21:
                st.write("#### proof of Expectation") 
            with c22:
                button_trig = st.button("Show the proof") 
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} \mathbb{E} X &=& \displaystyle \sum_{k=0}^{\infty} k \cdot \left( \dfrac{\lambda^k e^{-\lambda}}{k!} \right) \qquad (\text{noting that the first element in this series is } 0) \\ &=& \displaystyle \sum_{k=1}^{\infty} k \cdot \left( \dfrac{\lambda^k e^{-\lambda}}{k!} \right) = \displaystyle \sum_{i=k-1}^{\infty} \dfrac{(i+1)\lambda^{i+1} e^{-\lambda}}{(i+1)!} = \left( \lambda e^{-\lambda} \right) \cdot \left( \sum_{i=0}^{\infty} \dfrac{\lambda^i}{i!} \right) &=& \lambda \end{array} ")
        elif note == "mode":
            c21, c22 = st.columns(2) 
            with c21:
                st.write("#### proof of mode")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have nothing now")
        elif note == "median":
            c21, c22 = st.columns(2) 
            with c21:
                st.write("#### proof of median")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have nothing now")
        elif note == "variance":
            c21, c22 = st.columns(2) 
            with c21:
                st.write("#### proof of variance")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} \mathbb{E} X^2 &=& \displaystyle \sum_{k=0}^{\infty} k^2 \cdot \left( \dfrac{\lambda^k e^{-\lambda}}{k!} \right) \qquad (\text{noting that the first element in this series is } 0) \\ &=& \displaystyle \sum_{k=1}^{\infty} \left( k(k-1) + k \right) \cdot \left( \dfrac{\lambda^k e^{-\lambda}}{k!} \right) \\ &=& \displaystyle \left[ \sum_{k=1}^{\infty} \dfrac{k(k-1) e^{-\lambda} \lambda^k }{k!} \right] + \left[ \sum_{k=1}^{\infty} \dfrac{k e^{-\lambda} \lambda^k}{k!} \right] \\ &=& \displaystyle \left[ \sum_{k=2}^{\infty} \dfrac{k(k-1) e^{-\lambda} \lambda^k }{k!} \right] + \left[ \sum_{k=1}^{\infty} \dfrac{k e^{-\lambda} \lambda^k}{k!} \right] \\ &=& \displaystyle \left[ \sum_{k=2}^{\infty} \dfrac{e^{-\lambda} \lambda^k}{(k - 2)!} \right] + \left[ \sum_{k=1}^{\infty} \dfrac{ e^{-\lambda} \lambda^k}{(k - 1)!} \right] \\ &=& \displaystyle \lambda^2 \cdot \left( \sum_{i=0}^{\infty} \dfrac{ e^{-\lambda} \lambda^i}{i!} \right) + \lambda \cdot \left( \sum_{i=0}^{\infty} \dfrac{ e^{-\lambda} \lambda^i}{i!} \right) \\ &=& \lambda + \lambda^2 \end{array} ")
                st.write("--------")
                st.write("Also, you can use the consequence of MGF or CF to find this 2nd moment")
                st.latex(r" \begin{array}{ccl} \mathbb{E}X^2 = \dfrac{d^2}{dt^2} M_X(t) \Big\vert_{t=0} &=& \dfrac{d}{dt} \left( \dfrac{d}{dt} \left[ \exp \left( \lambda \left( e^{t} - 1 \right) \right) \right] \right) \Big\vert_{t=0} \\ &=& \dfrac{d}{dt} \left( \lambda e^t M_X(t) \right)\Big\vert_{t=0} \\ &=& \left[ \left( \lambda e^t \right)^2 M_X(t) + \left( \lambda e^t \right) M_X(t) \right] \Big\vert_{t=0} \\ &=& \lambda^2 + \lambda \end{array} ")
                st.write("--------")                
                st.write("Hence")
                st.latex(r" \text{Var} X = \mathbb{E}X^2 - \left( \mathbb{E} X \right)^2 = \lambda ")
        elif note == "Skewness":
            c21, c22 = st.columns(2) 
            with c21:
                st.write("#### proof of Skewness")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} \mathbb{E} \left( \dfrac{X - \mathbb{E}X }{ \sqrt{\text{Var} X} } \right)^3 &=& \dfrac{ \mathbb{E}X^3 - 3\lambda\mathbb{E}X^2 + 3 \lambda^2 \mathbb{E}X - \lambda^3 }{\lambda^{3 / 2} } \\ &=& \dfrac{\mathbb{E}X^3 - 3\lambda \left( \lambda^2 + \lambda \right) + 2\lambda^3}{\lambda^{3/2}} &=& \dfrac{\mathbb{E}X^3 - \lambda^3 - 3\lambda^2}{\lambda^{3/2}} \end{array} ")
                st.write("To find the 3rd moment, we can also using MGF/CF or even the expression of $k^3$,")
                st.latex(r" k^3 = k(k-1)(k-2) + 3k(k-1) + k ")
                st.write(" To simplify this computation we just apply the 3rd derivaties of MGF")
                st.latex(r" \begin{array}{ccl} \mathbb{E}X^3 := \dfrac{d^3}{dt^3} M_X(t) \Big\vert_{t=0} &=& \dfrac{d}{dt} \left( \dfrac{d^2}{dt^2} \left[ \exp \left( \lambda \left( e^{t} - 1 \right) \right) \right] \right) \Big\vert_{t=0} \\ &=& \dfrac{d}{dt} \left( \left[ \left( \lambda e^t \right)^2 + \left( \lambda e^t \right) \right] M_X(t) \right) \Big\vert_{t=0} \\ &=& \left[ \left( \left( \lambda e^t \right)^3 + 3\left( \lambda e^t \right)^2 +\left( \lambda e^t \right) \right) M_X(t) \right]  \Big\vert_{t=0} \\ &=& \lambda^3 + 3 \lambda^2 + \lambda \end{array} ")
                st.write("Hence")
                st.latex(r" \mathbb{E} \left( \dfrac{X - \mathbb{E}X }{ \sqrt{\text{Var} X} } \right)^3 = \lambda^{-1/2} ")
        elif note == "Kurtosis":
            c21, c22 = st.columns(2) 
            with c21:
                st.write("#### proof of Kurtosis")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} \mathbb{E} \left( \dfrac{X - \mathbb{E}X }{ \sqrt{ \text{Var} X} } \right)^4 &=& \dfrac{ \mathbb{E}X^4 - 4\lambda\mathbb{E}X^3 + 6 \lambda^2 \mathbb{E}X^2 - 4 \lambda^3 \mathbb{E}X + \lambda^4 }{\lambda^2 } \\ &=& \dfrac{\mathbb{E}X^4 - 4\lambda \left( \lambda^3 + 3 \lambda^2 + \lambda \right) + 6\lambda^2 \left( \lambda^2 + \lambda \right) - 3\lambda^4}{\lambda^2} &=& \dfrac{\mathbb{E}X^4 - \lambda^4 - 6\lambda^3 - 4\lambda^2}{\lambda^2} \end{array} ")
                st.write("To find the 4rd moment, we can also using MGF/CF or even the expression of $k^4$,")
                st.latex(r" k^4 = k(k-1)(k-2)(k-3) + 3k(k-1)(k-2) + 7k(k-1) + k ")
                st.write(" To simplify this computation we just apply the 4rd derivaties of MGF")
                st.latex(r" \begin{array}{ccl} \mathbb{E}X^4 := \dfrac{d^4}{dt^4} M_X(t) \Big\vert_{t=0} &=& \dfrac{d}{dt} \left( \dfrac{d^3}{dt^3} \left[ \exp \left( \lambda \left( e^{t} - 1 \right) \right) \right] \right) \Big\vert_{t=0} \\ &=& \dfrac{d}{dt} \left( \left[ \left( \lambda e^t \right)^3 + 3 \left( \lambda e^t \right)^2 + \left( \lambda e^t \right) \right] M_X(t) \right) \Big\vert_{t=0} \\ &=& \left[ \left( \left( \lambda e^t \right)^4 + 6 \left( \lambda e^t \right)^3 + 7 \left( \lambda e^t \right)^2 + \lambda e^t \right) M_X(t)\right] \Big\vert_{t=0} \\ &=& \lambda^4 + 6 \lambda^3 + 7 \lambda^2 + \lambda \end{array} ")
                st.write("Hence")
                st.latex(r" \mathbb{E} \left( \dfrac{X - \mathbb{E}X }{ \sqrt{\text{Var} X} } \right)^4 = 3 + \lambda^{-1} ")
                st.write("")
        elif note == "Characteristic func":
            c21, c22 = st.columns(2) 
            with c21:
                st.write("#### proof of CF")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} \varphi_X(t) := \mathbb{E} e^{itX} &=& \displaystyle \sum_{k=0}^{\infty} e^{itk} \cdot \left( \dfrac{\lambda^k e^{-\lambda}}{k!} \right) \\ &=& e^{-\lambda} \displaystyle \sum_{k=0}^{\infty} \dfrac{ \left( \lambda e^{it} \right)^k }{k!} \\ &=& e^{-\lambda} \cdot \exp \left( \lambda e^{it} \right) &=& \exp \left( \lambda \left( e^{it} - 1 \right) \right) \end{array} ")
        elif note == "Moment generating func":
            c21, c22 = st.columns(2) 
            with c21:
                st.write("#### proof of MGF")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} M_X(t) := \mathbb{E} e^{tX} &=& \displaystyle \sum_{k=0}^{\infty} e^{tk} \cdot \left( \dfrac{\lambda^k e^{-\lambda}}{k!} \right) \\ &=& e^{-\lambda} \cdot \displaystyle \sum_{k=0}^{\infty} \dfrac{ \left( \lambda e^{t} \right)^k }{k!} \\ &=& e^{-\lambda} \cdot \exp \left( \lambda e^{t} \right) &=& \exp \left( \lambda \left( e^{t} - 1 \right) \right) \end{array} ")
        elif note == "Proba generating func":
            c21, c22 = st.columns(2)
            with c21:
                st.write("#### proof of PGF")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} G_X(t) := \mathbb{E} z^X &=& \displaystyle \sum_{k=0}^{\infty} z^k \cdot \left( \dfrac{\lambda^k e^{-\lambda}}{k!} \right) \\ &=& e^{-\lambda} \cdot \displaystyle \sum_{k=0}^{\infty} \dfrac{ \left( \lambda z \right)^k }{k!} \\ &=& e^{-\lambda} \cdot \exp \left( \lambda z \right) &=& \exp \left( \lambda \left( z - 1 \right) \right) \end{array} ")
        elif note == "Fisher information":
            c21, c22 = st.columns(2)
            with c21:
                st.write("#### proof of Fisher information")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} I_{(\theta = \lambda)}^X &=& \mathbb{E} \left( \left. \dfrac{d}{d \theta} \log f(X, \theta) \right\vert \theta = \lambda \right)^2 \\ &=& \mathbb{E} \left( \dfrac{d}{d \lambda} \log \left[\dfrac{e^{-\lambda} \lambda^{X}}{X!} \right] \right)^2 \\ &=&  \mathbb{E} \left( \dfrac{d}{d \lambda} \left[ -\lambda + X \log \lambda - \log(X!) \right] \right)^2 \\ &=& \mathbb{E} \left( \dfrac{X}{\lambda} - 1 \right)^2 \\ &=& \dfrac{\mathbb{E} \left( X - \lambda \right)^2}{\lambda^2} \qquad =\qquad \dfrac{ \text{Var}X }{\lambda^2} &=& \dfrac{1}{\lambda } \end{array} ")
        elif note == "Entropy":
            with c21:
                st.write("#### proof of Fisher information")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} H(X, \lambda) &=& \mathbb{E} \left( - \log f(X, p) \right) \\ &=& - \mathbb{E} \left[ \log \left( \dfrac{e^{-\lambda} \lambda^{X}}{X!} \right) \right] \\ &=& - \displaystyle \mathbb{E} \left[ -\lambda +X\log \lambda - \log \left( X! \right) \right] \\ &=& \lambda \cdot \left( 1 - \log \lambda \right) + \mathbb{E} \log(X!) \\ &=&  \lambda \cdot \left( 1 - \log \lambda \right) + \displaystyle e^{-\lambda} \cdot \sum_{x=0}^{\infty} \dfrac{\log(x!) \lambda^x }{x!} \end{array} ")
                st.write(r"For $\lambda$ large enough, then")
                st.latex(r" H(X, \lambda) \approx \dfrac{1}{2} \log \left( 2\pi e \lambda \right) - \dfrac{1}{12\lambda} - \dfrac{1}{24 \lambda^2} - \dfrac{19}{360 \lambda^3} + O \left( \lambda^{-4} \right) ")

def geometry_all_proofs(note: str):
    from .distr_illus import geometry_show
    c1, _, c2 = st.columns([5, 1, 10])
    with c1:
        st.write("#### illustration")
        p = st.number_input("Select a value of `p`", value=.2, min_value=0.01, max_value=1.0)         
        geometry_show(p)
    with c2:
        c21, c22 = st.columns(2)
        st.write("We have some notes in this distributions")
        st.latex(r" \begin{array}{rrrrrr} \displaystyle \sum_{k=0}^{n} c^k = \dfrac{1 - c^{n+1}}{1 - c} & & & & \quad & \forall c \neq 1 \\ \displaystyle \sum_{k=0}^{\infty} c^k = \dfrac{1}{1-c} & \text{and} & \displaystyle \sum_{k=1}^{\infty} k c^{k-1} &=& \dfrac{1}{(1-c)^2} & \forall \vert c \vert < 1 \\ & & \displaystyle \sum_{k=2}^{\infty} k(k-1) c^{k-2} &=& \dfrac{2}{(1-c)^3} \\ & & \displaystyle \sum_{k=3}^{\infty} k(k-1)(k-2) c^{k-3} &=& \dfrac{6}{(1-c)^4} \\ \end{array} ")        
        if note == "cdf":
            with c21:
                st.write("#### proof of cdf")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} P(X \leq x) = \displaystyle\sum_{k=0}^{\left\lfloor x \right\rfloor} P(X = k) &=& \displaystyle \sum_{k=0}^{\left\lfloor x \right\rfloor} p ( 1 - p)^{k} & & , \text{where}  \left \lfloor x \right \rfloor = \text{floor} \left( x \right)\\ &=& \displaystyle p \sum_{k=0}^{\left\lfloor x \right\rfloor} (1-p)^{k} \\ &=& \displaystyle p \cdot \left( \dfrac{1 - (1-p)^{\left\lfloor x \right\rfloor+1}}{1 - (1 - p)} \right) &=& 1-(1-p)^{\left\lfloor x \right\rfloor+1} \end{array} ")
        elif note == "Expectation":
            with c21:
                st.write("#### proof of Expectation")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("Apply the result of MGF, we have")
                st.latex(r" \begin{array}{ccl} \mathbb{E}X := \left( \dfrac{d}{dt} M_X(t) \right) \Big\vert_{t=0} &=& \dfrac{d}{dt} \left( \dfrac{p}{1 - (1-p)e^t} \right) \Big\vert_{t=0} \\ &=& \left. \dfrac{p(1-p)e^t}{\left( 1 - (1-p)e^t \right)^2 } \right\vert_{t=0} &=& \dfrac{1-p}{p} \end{array} ")
        elif note == "mode":
            with c21:
                st.write("#### proof of mode")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have nothing now")
        elif note == "median":
            with c21:
                st.write("#### proof of median")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have nothing now")
        elif note == "variance":
            with c21:
                st.write("#### proof of variance")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("Using MGF to find the 2nd moment, and the result of the 1st derivaties (see from the proof of `Expectation`)")
                st.latex(r" \begin{array}{ccl} \mathbb{E}X^2 := \left. \left( \dfrac{d^2}{dt^2} M_X(t) \right) \right\vert_{t=0} &=& \left. \dfrac{d}{dt} \left( \dfrac{p(1-p)e^t}{ \left( 1 - (1-p)e^t \right)^2} \right) \right\vert_{t=0} \\ &=& \left. \dfrac{p \cdot\left[  (1-p)e^t + \left( (1- p) e^t \right)^2 \right]}{\left( 1 - (1-p)e^t \right)^3 } \right\vert_{t=0} \\ &=& \dfrac{1-p}{p^2} + \dfrac{\left( 1 - p \right)^2}{p^2} \end{array} ")
                st.write("Hence")
                st.latex(r" \text{Var} X = \mathbb{E} X^2 - \left( \mathbb{E} X \right)^2 = \dfrac{1-p}{p^2} ")    
        elif note == "Skewness":
            with c21:
                st.write("#### proof of skewness")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("Using MGF to find the 3rd moment, and the result of the 1st, 2nd derivaties (see from the proof of `Expectation` and `variance`)")
                st.latex(r" \begin{array}{ccl} \mathbb{E}X^3 := \left. \left( \dfrac{d^3}{dt^3} M_X(t) \right) \right\vert_{t=0} &=& \left.\dfrac{d}{dt} \left( \dfrac{ p \cdot\left[  (1-p)e^t + \left( (1- p) e^t \right)^2 \right] }{ \left( 1 - (1-p)e^t \right)^3} \right) \right\vert_{t=0} \\ &=& \left. \dfrac{ p \cdot \left[ (1-p)e^t + 4\left( (1 - p) e^t \right)^2 + \left( (1-p)e^t \right)^3 \right] }{\left( 1 - (1-p)e^t \right)^4 } \right\vert_{t=0} \\ &=& \dfrac{1-p}{p^3} + \dfrac{4\left( 1 - p \right)^2}{p^3} + \dfrac{\left( 1 - p \right)^3}{p^3} \end{array} ")
                st.write("So, the `skewness` will become")
                st.latex(r" \begin{array}{ccl} \mathbb{E} \left( \dfrac{ X - \mathbb{E}X }{\sqrt{\text{Var}X}} \right)^3 &=& \dfrac{\mathbb{E}X^3 - 3\mathbb{E}X^2 \cdot \left( \dfrac{1-p}{p} \right) + 3 \mathbb{E}X \cdot \left( \dfrac{1-p}{p} \right)^2 - \left( \dfrac{1-p}{p} \right)^3 }{ \left( \dfrac{1-p}{p^2} \right)^{3/2} } \\ &=& \dfrac{\mathbb{E}X^3 - 3 \left( \dfrac{(1-p)^2 + (1-p)^3}{p^3} \right) + 2 \left( \dfrac{1-p}{p} \right)^3 }{ \left( \dfrac{1-p}{p^2} \right)^{3/2} } \\ &=& \dfrac{ \left( \dfrac{1-p}{p^3} + \dfrac{4\left( 1 - p \right)^2}{p^3} + \dfrac{\left( 1 - p \right)^3}{p^3} \right) - \dfrac{3(1-p)^2 }{p^3} - \dfrac{(1-p)^3}{p^3} }{ \left( \dfrac{(1-p)\sqrt{1-p}}{p^3} \right) } \\ &=& \qquad \dfrac{1 + (1-p)}{\sqrt{1-p}} \qquad \text{ simplifies both terms for } \dfrac{1-p}{p^3} \\ \\ &=& \qquad  \qquad \dfrac{2-p}{\sqrt{1-p}} \end{array} ")
        elif note == "Kurtosis":
            with c21:
                st.write("#### proof of Kurtosis")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("Using MGF to find the 4th moment, and the result of the 1st, 2nd and 3rd derivaties (see from the proofs of `Expectation`, `variance` and `Skewness`)")
                st.latex(r" \begin{array}{ccl} \mathbb{E}X^4 := \left. \left( \dfrac{d^4}{dt^4} M_X(t) \right) \right\vert_{t=0} &=& \left.\dfrac{d}{dt} \left( \dfrac{ p \cdot\left[  (1-p)e^t + \left( (1-p)e^t \right)^2 + \left( (1- p) e^t \right)^3 \right] }{ \left( 1 - (1-p)e^t \right)^4} \right) \right\vert_{t=0} \\ &=& \left. \dfrac{ p \cdot \left[ (1-p)e^t + 11\left( (1 - p) e^t \right)^2 + 11\left( (1-p)e^t \right)^3 + \left( (1-p)e^t \right)^4 \right] }{\left( 1 - (1-p)e^t \right)^5 } \right\vert_{t=0} \\ &=& \dfrac{1-p}{p^4} + \dfrac{11\left( 1 - p \right)^2}{p^4} + \dfrac{11\left( 1 - p \right)^3 }{p^4} + \dfrac{\left( 1 - p \right)^4}{p^4} \end{array}  ")
                st.write("So, the `kurtosis` becomes")
                st.latex(r" \begin{array}{ccl} \mathbb{E} \left( \dfrac{ X - \mathbb{E}X }{\sqrt{\text{Var}X}} \right)^4 &=& \dfrac{\mathbb{E}X^4 - 4\mathbb{E}X^3 \cdot \left( \dfrac{1-p}{p} \right) + 6 \mathbb{E}X^2 \cdot \left( \dfrac{1-p}{p} \right)^2 - 4 \mathbb{E}X \cdot \left( \dfrac{1-p}{p} \right)^3 + \left( \dfrac{1-p}{p} \right)^4 }{ \left( \dfrac{1-p}{p^2} \right)^{2} } \\   &=& \dfrac{\mathbb{E}X^4 - 4\left( \dfrac{(1-p)^2 + 4(1-p)^3 + (1-p)^4 }{p^4} \right) + 6 \left( \dfrac{(1-p)^3 + (1-p)^4 }{p^4} \right) - 3 \left( \dfrac{1-p}{p} \right)^4 }{ \left( \dfrac{1-p}{p^2} \right)^{2} } \\   &=& \dfrac{ \left( \dfrac{(1-p)^4+11(1-p)^3 + 11(1-p)^2 + (1-p)}{p^4}\right) - \dfrac{(1-p)^4+10(1-p)^3+4(1-p)^2}{p^4} }{ \left( \dfrac{(1-p)^2}{p^4} \right) } \\   &=& \qquad \dfrac{ (p-1)^2 - 4(1-p) + 1 }{1-p} \qquad \text{ simplifies both terms for } \dfrac{1-p}{p^4} \\ \\      &=& \qquad  6 + \dfrac{p^2}{1-p} \end{array} ")
        elif note == "Characteristic func":
            with c21:
                st.write("#### proof of CF")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} \varphi_X(t) := \mathbb{E} e^{itX} &=& \displaystyle \sum_{k=0}^{\infty} e^{itk} \cdot \left( p \left( 1 - p \right)^k \right) \\ &=& p \cdot \displaystyle \left[ \sum_{k=0}^{\infty} \left( (1-p)e^{it} \right)^k \right] \\ &=& p \cdot \dfrac{1}{1 - (1-p)e^{it}} \end{array} ")
                st.write("with the noting that")
                st.latex(r" 0 \leq \lim_{x \to \infty} \Big\vert \left[ (1-p) e^{it} \right]^x \Big\vert \leq \lim_{x \to \infty} \left| 1-p \right|^x = 0 ")
                st.write("since")
                st.latex(r" \left| e^{itx} \right| =\left| \cos tx + i\sin tx \right| \leq 1 \qquad \forall x ")
        elif note == "Moment generating func":
            with c21:
                st.write("#### proof of MGF")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} M_X(t) := \mathbb{E} e^{tX} &=& \displaystyle \sum_{k=0}^{\infty} e^{tk} \cdot \left( p \left( 1 - p \right)^k \right) \\ &=& p \cdot \displaystyle \left[ \sum_{k=0}^{\infty} \left( (1-p)e^{t} \right)^k \right] \\ \\ &=& \dfrac{p}{1 - (1-p)e^{t}} & \forall t \in \left( 0, - \ln \left( 1 - p \right) \right) \end{array} ")
                st.write(r"Noting that for real number (not complex like in CF), then the `geometric series` $\sum_{k=0}^{\infty} ((1-p)e^{t})^k$ converges iff")
                st.latex(r" (1-p) e^t < 1 \Leftrightarrow t < - \ln (1-p) ")
        elif note == "Proba generating func":
            with c21:
                st.write("#### proof of PGF")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} G_X(t) := \mathbb{E} z^{X} &=& \displaystyle \sum_{k=0}^{\infty} z^{k} \cdot \left( p \left( 1 - p \right)^k \right) \\ &=& p \cdot \displaystyle \left[ \sum_{k=0}^{\infty} \left( (1-p)z \right)^k \right] \\ \\ &=& \dfrac{p}{1 - (1-p)z} & \forall z \in \left( 0, \left( 1 - p \right)^{-1}\right) \end{array} ")
        elif note == "Fisher information":
            with c21:
                st.write("#### proof of Fisher information")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} I_{\theta}^X := \mathbb{E} \left[ \frac{d}{d\theta} \log f(X, \theta) \Big\vert \theta = p \right]^2 &=& \mathbb{E} \left[ \dfrac{d}{dp} \log \left( p (1 - p)^X \right) \right]^2 \\&=& \mathbb{E} \left[ \dfrac{d}{dp} \left( \log p + X \log(1 - p) \right) \right]^2 \\ &=& \mathbb{E} \left[ \dfrac{1}{p} - \dfrac{X}{1-p} \right]^2 \\  &=& \mathbb{E} \left( \dfrac{-1}{1-p} \cdot\left[ X - \dfrac{1-p}{p} \right] \right)^2 \\  &=& \dfrac{ \mathbb{E} \left( X - \mathbb{E}X \right)^2}{(1-p)^2} \\  &=& \dfrac{1-p}{p^2} \cdot \dfrac{1}{(1-p)^2}  &=& \dfrac{1}{p^2(1-p)} \end{array} ")
        elif note == "Entropy":
            with c21:
                st.write("#### proof of Entropy")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} H(X, \theta) := \mathbb{E} \left[ - \log f(X, \theta) \right] &=& \mathbb{E} \left[ - \log \left( p(1-p)^X \right) \right] \\ &=& \mathbb{E}\left[ -\log p - X \log(1-p) \right] \\ &=& -\log p - \mathbb{E}X \cdot \log(1-p) \\ &=& -\log p - \left( \dfrac{1-p}{p} \right) \cdot \log(1-p) \\ &=& - \left( \dfrac{p \log p + (1-p) \log(1-p)}{p} \right)  \end{array} ")

def hypergeometry_all_proofs(note: str):
    from .distr_illus import hypergeometry_show
    c1, _, c2 = st.columns([5, 1, 10])
    with c1:
        st.write("#### illustration") 
        N = st.number_input("Select a value of `N`", value=10, min_value=2, max_value=200, help="population size")
        n = st.number_input("Select a value of `n`", value=5, min_value=2, max_value=N, help="numbers of draws")
        K = st.number_input("Select a value of `K`", value=6, min_value=2, max_value=N, help="total success in population") 
        hypergeometry_show(N, K, n)
    with c2:
        st.write("We have some notes in this distributions")
        st.latex(r" \begin{array}{ccl} \displaystyle \sum_{k=0}^n \binom{a}{k} \binom{b}{n-k} &=& \displaystyle \binom{a+b}{n} \\ \displaystyle \binom{n}{k} &=& \displaystyle \binom{n-1}{k} + \binom{n-1}{k-1} \\ \text{HyperGeo}(N, K, n) &=& \displaystyle \sum_{i=1}^n S_i \end{array} ")
        st.write(r"where $S_i$  is the indicator that the $i$-th draw is a success. Hence $S_i \sim \mathcal{B}\left( 1, \dfrac{K}{N} \right)$") 
        c21, c22 = st.columns(2)
        if note == "cdf":       
            with c21:
                st.write("#### proof of cdf")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} P(X < x) &=& \displaystyle \sum_{k= \max \lbrace 0, n+K-N \rbrace }^{ \left\lfloor x \right\rfloor } P(X = k) \\ &=& \displaystyle \sum_{k= \max \lbrace 0, n+K-N \rbrace }^{ \left\lfloor x \right\rfloor } \dfrac{\binom{K}{k} \binom{N-K}{n-k} }{\binom{N}{n}} \\ &=& \displaystyle \binom{N}{n}^{-1} \sum_{k= \max \lbrace 0, n+K-N \rbrace }^{ \left\lfloor x \right\rfloor } \binom{K}{k} \binom{N-K}{n-k} \end{array} ")
        elif note == "Expectation":
            with c21:
                st.write("#### proof of Expecation")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("In this distribution, using the MGF or CF may be too complicated to understand (since this based on the `generalized hypergeometric function`). We have 2 approachs to obtain this")
                st.write("----------")
                st.write("#### Approach 1. Trick")
                st.write("By the decomposition of `HyperGeo` into n-independent $S_i$, then")
                st.latex(r" \mathbb{E} X = \sum_{i=1}^n \mathbb{E} S_i = n \mathbb{E} S_1 = \dfrac{nK}{N} ")
                st.write(r"Because each vrs $S_i$ has equality distribution with success proba is $\dfrac{K}{N}$ (i.e, $K$ possible successes in population)")                
                st.write("----------")
                st.write("#### Approach 2. Hard-core")
                st.write("Look at these notes that I mentioned in this distribution. Then, we have")
                st.latex(r" \begin{array}{ccl} \mathbb{E}X &=& \displaystyle \sum_{k=\max \lbrace 0, n+K-N \rbrace }^{\min \lbrace n, K \rbrace } k \cdot\left[ \dfrac{\binom{K}{k} \binom{N - K}{n - k}}{ \binom{N}{n} } \right] \\  &=& \displaystyle \binom{N}{n}^{-1} \sum_k \left[ k \binom{K}{k} \right] \cdot \binom{N-K}{n-k} \\ &=& \displaystyle \binom{N}{n}^{-1}  \sum_k \left[ K \binom{K-1}{k-1} \right] \cdot \binom{N-K}{n-k} \\ &=& \displaystyle K \binom{N}{n}^{-1}  \sum_k \binom{K-1}{k-1} \binom{N-K}{n-k} \\ &=& \displaystyle K \binom{N}{n}^{-1} \underbrace{\sum_{i=k-1} \binom{K-1}{i} \binom{N-K}{n-1-i}} \\ &=& \displaystyle \quad K \binom{N}{n}^{-1} \cdot \qquad \binom{N-1}{n-1} \\ &=& \qquad K \qquad \cdot \qquad \dfrac{n}{N} &=& \dfrac{nK}{N} \end{array} ")
        elif note == "mode":
            with c21:
                st.write("#### proof of mode")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("Finish later")
        elif note == "median":
            with c21:
                st.write("#### proof of median")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("Finish later")
        elif note == "variance":
            with c21:
                st.write("#### proof of median")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig: 
                st.write("Approach 1. Trick")
                st.latex(r" \begin{array}{ccl}   \text{Var} X &=& \displaystyle \text{Var} \left( \sum_{k=1}^n S_i \right) \\ &=& \displaystyle \left( \sum_{i=1}^n \text{Var} S_i \right) + 2 \left( \sum_{1 \leq i < j \leq n} \text{Cov} \left( S_i, S_j \right) \right) \\ &=& n \cdot \text{Var} S_1 + n(n-1) \cdot \text{Cov} \left( S_1, S_2 \right) \\ &=& n \cdot \left( \dfrac{K}{N} \cdot \left( 1 - \dfrac{K}{N} \right) \right) + n(n-1) \left( \dfrac{K}{N}\cdot \left( 1 - \dfrac{K}{N} \right) \cdot \dfrac{-1}{N-1} \right) \\ &=& n \cdot \dfrac{K}{N} \cdot \dfrac{N-K}{N} \cdot \left( 1 - \dfrac{n-1}{N-1} \right) \\ &=& n \cdot \dfrac{K}{N} \cdot \dfrac{N-K}{N} \cdot \dfrac{N-n}{N-1} \end{array} ")
                st.write("Indeed, these $S_i, S_j$ are `not independent` but have the same distribution, so" )
                st.latex(r" \begin{array}{rcl} \text{Var} S_1 &=& \text{Var} S_2 = \ldots = \text{Var} S_n = p (1 - p) & ,& p= \dfrac{K}{N} \\ \text{Cov} \left( S_1, S_2 \right) &=& \mathbb{E} \left( S_1 S_2 \right) - \mathbb{E} S_1 \cdot \mathbb{E} S_2 \\ &=& \dfrac{K}{N} \cdot \dfrac{K-1}{N-1} - \left( \dfrac{K}{N} \right)^2 \\ &=& \dfrac{K}{N} \cdot \left( \dfrac{K-1}{N-1} - \dfrac{K}{N} \right) \\ &=& \dfrac{K}{N} \cdot \dfrac{N(K - 1) - K(N - 1)}{N(N-1)} \\ &=& \dfrac{K}{N} \cdot \left( \dfrac{K - N}{N} \cdot \dfrac{-1}{N-1} \right) \\  &=& \dfrac{K}{N} \cdot \left( 1 - \dfrac{K}{N} \right) \cdot \dfrac{-1}{N-1} \end{array} ")
                st.write("--------")
                st.write("Approach 2")
                st.write("By the same arguments in computing Expectation, but we have a note that")
                st.latex(r" \text{Var} X = \mathbb{E} X^2 - \left( \mathbb{E} X \right)^2 = \left[ \mathbb{E}\left( X(X-1) \right) + \mathbb{E} X \right] - \left( \mathbb{E} X \right)^2 ")
                st.write("Now, we have")
                st.latex(r" \begin{array}{ccl} \mathbb{E}(X(X-1)) &=& \displaystyle \sum_k k(k-1) \cdot \left( \dfrac{ \binom{K}{k} \binom{N-K}{n-k} }{\binom{N}{n}} \right) \\ &=& \displaystyle \binom{N}{n}^{-1} \cdot \sum_k \left[ k(k-1) \binom{K}{k} \right] \cdot \binom{N-K}{n-k} \\ &=& \displaystyle \binom{N}{n}^{-1} \cdot \sum_k \left[ K(K-1) \binom{K-2}{k-2} \right] \cdot \binom{N-K}{n-k} \\ &=& \displaystyle \binom{N}{n}^{-1} K(K-1) \cdot \sum_k \binom{K-2}{k-2} \binom{N-K}{n-k} \\ &=& \displaystyle \binom{N}{n}^{-1} K(K-1) \cdot \underbrace{\sum_{i=k-2} \binom{K-2}{i} \binom{N-K}{n-2-i}} \\ &=& \displaystyle \quad K(K-1) \quad \underbrace{\binom{N}{n}^{-1} \cdot \qquad \binom{N-2}{n-2}} \\ &=& \qquad K(K-1) \cdot \qquad \dfrac{n(n-1)}{N(N-1)} &=& n (n-1)\dfrac{K}{N} \dfrac{K-1}{N-1}\end{array} ")
                st.write("Hence")
                st.latex(r" \begin{array}{ccl} \text{Var} X &=& \left[ \left(n (n-1)\dfrac{K}{N} \dfrac{K-1}{N-1} \right) + \dfrac{nK}{N} \right] - \left( \dfrac{nK}{N} \right)^2 \\ &=& n \dfrac{K}{N} \left[ \dfrac{(n-1\displaystyle )(K-1)}{N-1} + 1 - \dfrac{nK}{N} \right] \\ &=& n \dfrac{K}{N} \left[ \dfrac{nK - K - n +1}{N-1} + \dfrac{N - nK}{N} \right] \\ &=& n \dfrac{K}{N} \cdot \dfrac{N^2 - kN +kn- Nn}{N(N-1)} \\ &=& n \dfrac{K}{N} \cdot \left( \dfrac{N-K}{N} \cdot \dfrac{N-n}{N-1} \right) \end{array} ")
        elif note == "Skewness":
            with c21:
                st.write("#### proof of Skewness")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("Firstly, we all known")
                st.latex(r" \mathbb{E}\left( \dfrac{X - \mu}{\sigma} \right)^3 = \dfrac{\mathbb{E}X^3 - 3\mu \mathbb{E}X^2 + 2\mu^3 }{\sigma^3} ")
                st.write(r"where $\mu = \mathbb{E}X$ and $\sigma^2 = \text{Var}X$")
                st.write("You can apply hard-core tips as I have shown in `Expectation, variance` parts. But now I just focus on using the decomposition of `n-dependent vrs` $S_i$. We have")  
                st.latex(r" \begin{array}{ccl} \mathbb{E}X^3 := \displaystyle \mathbb{E} \left( \sum_{i=1}^n S_i \right)^3 &=& \displaystyle \left( \sum_{i=1}^n \mathbb{E} S_i^3 \right) + 3 \left( \sum_{i < j}^n \mathbb{E} \left( S_i^2 S_j \right) \right) + 6 \left( \sum_{i < j < k}^n \mathbb{E} \left( S_i S_j S_k \right) \right) \\ &=& A + 3B + 6C \end{array} ")
                st.write("where")
                st.latex(r" \begin{array}{clrcl} A &:=& \displaystyle \sum_{ i=1 }^n \mathbb{E} S_i^3 &=& \displaystyle \sum_{ i=1 }^n \mathbb{E} S_i = n\mathbb{E}S_i = \dfrac{nK}{N} \\ B &:=& \displaystyle \sum_{i < j } \mathbb{E}\left( S_i^2 S_j \right) &=& \dfrac{n(n-1)}{2} \mathbb{E} \left( S_1^2 S_2 \right) \\ & & &=& \dfrac{n(n-1)}{2} \mathbb{E} \left( S_1 S_2 \right) \qquad \text{since } S_i^2 = S_i \\  & & &=& \dfrac{n(n-1)}{2} \cdot \left( \dfrac{K}{N} \cdot \dfrac{K-1}{N-1} \right) \\ C &:=& \displaystyle \sum_{i < j < k} \mathbb{E}\left( S_i S_j S_k \right) &=& \dfrac{n(n-1)(n-2)}{6} \mathbb{E} \left( S_1 S_2 S_3 \right) \\  & & &=& \dfrac{n(n-1)(n-2)}{6} \cdot \left( \dfrac{K}{N} \cdot \dfrac{K-1}{N-1} \cdot \dfrac{K-2}{N-2} \right)  \end{array} ")
                st.write("Then simplify carefully")
                st.latex(r" \mathbb{E} X^3 = \dfrac{nK}{N}\left[ 1 + \dfrac{(K-1)(n-1)}{N-1} + \dfrac{(K-1)(n-1)}{N-1} \cdot \dfrac{(K-2)(n-2)}{N-2} \right]")
                st.write("Substitute the 2 first moments and the variance, we have")
                st.latex(r" \begin{array}{ccl} \mathbb{E}X^3 - 3\mu \mathbb{E}X^2+2\mu^3  &=& \mu \left[ 1 + \dfrac{(K-1)(n-1)}{N-1} \cdot \left( 1 + \dfrac{(K-2)(n-2)}{N-2} \right) \right] \\  & & - 3\mu \cdot \left[ \mu \left( 1 +  \dfrac{(K-1)(n-1)}{N-1} \right) \right] + 2 \mu^3 \\ \\ \Rightarrow \mathbb{E} \left( \dfrac{X - \mu}{\sigma} \right)^3 &=& \displaystyle \frac {(N-2K)(N-1)^{\frac {1}{2}}(N-2n)}{[nK(N-K)(N-n)]^{\frac {1}{2}}(N-2)} \end{array} ")
        elif note == "Kurtosis":
            with c21:
                st.write("#### proof of Kurtosis")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("Do the same techinques like I have done in `skewness`, with the noting that")
                st.latex(r" \mathbb{E} \left( \dfrac{X - \mu}{\sigma} \right)^4 = \dfrac{\mathbb{E}X^4 - 4\mu \mathbb{E}X^3 + 6 \mu^2 \mathbb{E}X^2 -3 \mu^4}{\sigma^4} ")
                st.write("and")
                st.latex( r" \begin{array}{ccl} \mathbb{E} X^4 & = & \displaystyle \left( \sum_{i=1}^n \mathbb{E} S_i^4 \right) + \left( \sum_{ i, j } \mathbb{E} \left( S_i^3 S_j \right) \right) + \left( \sum_{ i, j } \mathbb{E} \left( S_i^2 S_j^2 \right) \right) + \left( \sum_{ i, j, k } \mathbb{E} \left( S_i^2 S_j S_k \right) \right) + \left( \sum_{ i, j, k, m } \mathbb{E} \left( S_i S_j S_k S_m \right) \right) \\ & = & \displaystyle \left( \sum_{i=1}^n \mathbb{E} S_i \right) + \left( \sum_{ i, j } \mathbb{E} \left( S_i S_j \right) \right) + \left( \sum_{ i, j } \mathbb{E} \left( S_i S_j \right) \right) + \left( \sum_{ i, j, k } \mathbb{E} \left( S_i S_j S_k \right) \right) + \left( \sum_{ i, j, k, m } \mathbb{E} \left( S_i S_j S_k S_m \right) \right) \end{array} ")
                st.write("Combine all of them, we obtain")
                st.latex(r" \mathbb{E} \left( \frac{X - \mu}{\sigma} \right)^4 = \frac{\Big[ (N-1)N^2 \left( N(N+1) - 6K(N-K) - 6n(N-n) \right) \Big]}{nK(N-K)(N-n)(N-2)(N-3)} + \dfrac{6(5N - 6)}{(N-2)(N-3)} ")
        elif note == "Characteristic func":
            with c21:
                st.write("#### proof of CF")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("Using the sum of ...")
                
def nega_binom_all_proofs(note: str):
    from .distr_illus import Nega_binom_show
    c1, _, c2 = st.columns([5, 1, 10])
    with c1:
        st.write("#### illustration") 
        r = st.number_input("Select a value of `r`", value=10, min_value=2, max_value=200, help="number of successes until the experiment is stopped")
        p = st.number_input("Select a value of `p`", value=0.2, min_value=0.01, max_value=0.99, help="probability in each experiment") 
        Nega_binom_show(r, p)
    with c2:
        st.write("Beside some `combination expression tricks` on `HyperGeometric` distirbution, we have some notes in `Negative Binomial` distribution")
        st.latex(r" \begin{array}{ccl} \displaystyle k \binom{r+k-1}{k} &=& \displaystyle r \binom{r+k-1}{k-1} \\ \displaystyle \sum_{k=0}^{\infty} \binom{r+k}{k} z^k &=& \dfrac{1}{(1-z)^{r+1}} & \forall \vert z \vert < 1  \\ \text{Nega Binom}(r, p) &=& \displaystyle \sum_{i=1}^r G_i & , G_i \sim \text{Geo}(1, p) \qquad \forall i \end{array} ")
        c21, c22 = st.columns(2)
        if note == "cdf":
            with c21:
                st.write("#### proof of cdf")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} P(X < x) &=& \displaystyle \sum_{k = 0 }^{ \left\lfloor x \right\rfloor } P(X = k) \\ &=& \displaystyle \sum_{k= 0 }^{ \left\lfloor x \right\rfloor } \binom{k+r-1}{k} p^r (1-p)^k &=& p^r \displaystyle \sum_{k= 0 }^{ \left\lfloor x \right\rfloor } (1-p)^k \binom{k+r-1}{k} \end{array} ")
        elif note == "Expectation":
            with c21:
                st.write("#### proof of Expectation")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} \mathbb{E}X &=& \displaystyle \sum_{k=0}^{\infty} k \cdot \left( \binom{k+r-1}{k} p^r(1-p)^k \right) \\  &=& p^r \displaystyle \sum_{k=0}^{\infty} \left[ k \cdot \binom{k+r-1}{k} \right] \cdot (1-p)^k \\ &=& p^r \displaystyle \sum_{k=1}^{\infty} \left[ r \binom{k+r-1}{k-1} \right] (1-p)^k  \\ &=& rp^r \displaystyle \sum_{i=k-1}^{\infty} \binom{i+r}{i} (1-p)^{i+1} \\  &=& rp^r (1-p) \cdot \dfrac{1}{(1 - (1-p))^{r+1}} &=&\dfrac{r(1-p)}{p} \end{array} ")
        elif note == "mode":
            with c21:
                st.write("#### proof of mode")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have nothing now")
        elif note == "median":                          
            with c21:
                st.write("#### proof of median")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have nothing now")
        elif note == "variance":
            with c21:
                st.write("#### proof of variance")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have known")
                st.latex(r" \text{Var} X = \mathbb{E}\left[ X(X-1) \right] + \mu - \mu^2, \qquad \text{where} \mu = \mathbb{E} X ")
                st.write("Beside that")
                st.latex(r" \begin{array}{ccl} \mathbb{E}\left[ X(X-1) \right] &=& \displaystyle \sum_{k=0}^{\infty} k(k-1) \cdot \left( \binom{k+r-1}{k} p^r(1-p)^k \right) \\  &=& \displaystyle p^r \cdot \left( \sum_{k=2}^{\infty} \underbrace{\left[ k(k-1) \binom{k+r-1}{k} \right]} (1-p)^{k} \right) \qquad \text{the 2 first elements be zero} \\  &=& p^r \displaystyle \left( \sum_{k=2}^{\infty} \left[ r(r+1) \binom{k+r-1}{k-2} \right] (1-p)^{k} \right) \\  &=& r(r+1) p^r \displaystyle \cdot \left( \sum_{i=k-2}^{\infty} \binom{i + (r+1))}{i} (1-p)^{i+2} \right) \\  &=& r(r+1)p^r (1-p)^2 \cdot \displaystyle \left( \sum_{i=0}^{\infty} \binom{i + (r+1))}{i} (1-p)^{i} \right) \\ &=& \quad r(r+1)p^r (1-p)^2 \cdot \dfrac{1}{(1 - (1-p))^{(r+1) + 1}} \\  &=& \qquad \dfrac{r(r+1)(1-p)^2}{p^2} \end{array} ")
                st.write("Hence")
                st.latex(r" \begin{array}{ccl} \text{Var} X &=& \dfrac{r(r+1)(1-p)^2}{p^2} + \dfrac{r(1-p)}{p} - \left( \dfrac{r(1-p)}{p} \right)^2 \\ &=& \dfrac{r\left( 1-p \right) \left[ (r+1)(1-p) + p -r(1-p) \right]}{p^2} &=& \dfrac{r(1-p)}{p^2} \end{array} ")
                st.write("with the noting that")
                st.latex(r" k(k-1)\dfrac{(k+r-1)!}{k!(r-1)!} = r(r+1)\dfrac{(k+r-1)!}{(k-2)!(r+1)!} ")
        elif note == "Skewness": 
            with c21:
                st.write("#### proof of skewness")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have known")
                st.latex(r" \begin{array}{ccl}  \mathbb{E}\left( \dfrac{X - \mathbb{E}X}{\sqrt{\text{Var}X}} \right)^3 &=& \dfrac{\mathbb{E}X^3 - 3\mu \mathbb{E}X^2 + 2\mu^3}{\sigma^3} &=& \dfrac{\mathbb{E}X^3 - 3\mu \sigma^2  - \mu^3}{\sigma^3} \end{array} ")
                st.write("and")
                st.latex(r" k(k-1)(k-2) \binom{r+k-1}{k} = r(r+1)(r+2) \binom{r+k-1}{k-3} ")
                st.write(r"where $\mu = \mathbb{E}X$ and $\sigma^2 = \text{Var} X$. Beside that, by the same argument as we have done in `Expectation` and `variance`")
                st.latex(r" \begin{array}{ccl}  \mathbb{E} X^3 &=& \mathbb{E}\left[ X(X-1)(X-2)+3X(X-1)+X \right] \\  &=& \dfrac{r(r+1)(r+2)(1-p)^3}{p^3} + 3 \dfrac{r(r+1)(1-p)^2}{p^2} + \dfrac{r(1-p)}{p} \\ &=& \dfrac{\left( r^3+3r^2+2 \right)(1-p)^3+3p(1-p)\left( r^2+r \right)+p^2(1-p)r}{p^3} \\ &=& \qquad \dfrac{r(1-p)(2-p)}{p^3} \qquad + \qquad 3 \dfrac{r^2(1-p)^2}{p^3} \qquad + \qquad \dfrac{r^3(1-p)^3}{p^3} \\ \\ &=& \overbrace{\left( \left[ \dfrac{\left( r(1-p) \right)^{3/2}}{p^3} \right] \cdot \dfrac{2-p}{\sqrt{r(1-p)}} \right)} \qquad + \qquad  3 \mu \sigma^2 \qquad + \qquad  \mu^3 \\ \\ &=& \sigma^3 \cdot \dfrac{2-p}{\sqrt{r(1-p)}} + 3\mu\sigma^2 + \mu^3 \end{array} ")
                st.write("Therefore")
                st.latex(r" \mathbb{E}\left( \dfrac{X - \mathbb{E}X}{\sqrt{\text{Var}X}} \right)^3 = \dfrac{2-p}{\sqrt{r(1-p)}} ")
        elif note == "Kurtosis":
            with c21:
                st.write("#### proof of Kurtosis")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have known")
                st.latex(r"  \begin{array}{ccl} \mathbb{E}\left( \dfrac{X - \mathbb{E}X}{\sqrt{\text{Var}X}} \right)^4  &=& \dfrac{\mathbb{E}X^4 - 4\mu \mathbb{E}X^3 + 6\mu^2\mathbb{E}X^2+3\mu^4}{\sigma^4}  \\ &=& \dfrac{\mathbb{E}X^4 - 4\mu \mathbb{E}X^3 + 6 \mu^2 \sigma^2 +9\mu^4}{\sigma^4} \\   X^4 &=& X(X-1)(X-2)(X-3) + 6X(X-1)(X-2)+7X(X-1) + X  \end{array} ")
                st.write("and")
                st.latex(r" \begin{array}{ccl} k(k-1)(k-2)(k-3) \binom{r+k-1}{k} &=& r(r+1)(r+2)(r+3) \binom{r+k-1}{k-4} \\ \mathbb{E} \left[ X(X-1)(X-2)(X-3) \right] &=& r(r+1)(r+2)(r+3) \cdot \left( \dfrac{1-p}{p} \right)^4 \end{array} ")
                st.write("Do the same thing like we have used in Skewness, we obtain")
                st.latex(r" \mathbb{E}\left( \dfrac{X - \mathbb{E}X}{\sqrt{\text{Var}X}} \right)^4 = \dfrac{6}{r} + \dfrac{p^2}{r(1-p)} ")
        elif note == "Characteristic func":
            with c21:
                st.write("#### proof of skewness")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r"\begin{array}{ccl}  \varphi_X(t) := \mathbb{E}e^{itX} := \displaystyle \sum_{k=0}^{\infty} e^{itk} P(X=k) &=& \displaystyle \sum_{k=0}^{\infty} e^{itk} \cdot \left( \binom{k+r-1}{k} p^r(1-p)^k \right) \\  &=& \displaystyle p^r \sum_{k=0}^{\infty} \binom{k+r-1}{k} \cdot \left( (1-p)e^{it} \right)^k \\ &=& \displaystyle p^r \underbrace{\sum_{k=0}^{\infty} \binom{k+(r-1)}{k} \cdot \left( (1-p)e^{it} \right)^k} \\ &=& p^r \quad \cdot \quad \dfrac{1}{\left( 1 - (1-p)e^{it} \right)^{1 + (r-1)}} &=& \left( \dfrac{p}{1 - (1-p)e^{it}} \right)^r  \end{array}")
        elif note == "Moment generating func":
            with c21:
                st.write("#### proof of MGF")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} M_X(t) := \mathbb{E}e^{tX} := \displaystyle \sum_{k=0}^{\infty} e^{tk} P(X=k) &=& \displaystyle \sum_{k=0}^{\infty} e^{tk} \cdot \left( \binom{k+r-1}{k} p^r(1-p)^k \right) \\  &=& \displaystyle p^r \sum_{k=0}^{\infty} \binom{k+r-1}{k} \cdot \left( (1-p)e^{t} \right)^k \\ &=& \displaystyle p^r \sum_{k=0}^{\infty} \binom{k+(r-1)}{k} \cdot \left( (1-p)e^{t} \right)^k \\ &=& \left( \dfrac{p}{1 - (1-p)e^{t}} \right)^r \qquad \forall t < - \ln(1-p) \end{array} ")
        elif note == "Proba generating func":
            with c21:
                st.write("#### proof of MGF")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} G_X(t) := \mathbb{E}z^{X} := \displaystyle \sum_{k=0}^{\infty} z^{k} P(X=k) &=& \displaystyle \sum_{k=0}^{\infty} z^k \cdot \left( \binom{k+r-1}{k} p^r(1-p)^k \right) \\  &=& \displaystyle p^r \sum_{k=0}^{\infty} \binom{k+r-1}{k} \cdot \left( (1-p)z \right)^k \\ &=& \displaystyle p^r \sum_{k=0}^{\infty} \binom{k+(r-1)}{k} \cdot \left( (1-p)z \right)^k \\ &=& \left( \dfrac{p}{1 - (1-p)z} \right)^r \qquad \forall \vert z \vert < p^{-1} \end{array} ")            
        elif note == "Fisher information":
            with c21:
                st.write("#### proof of Fisher information")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} I_{\theta}^X := \mathbb{E} \left[ \left. \dfrac{d}{d\theta} \ln f(X,\theta) \right\vert \theta = p \right]^2  &=& \mathbb{E} \left[ \dfrac{d}{dp} \ln \left( \binom{X+r-1}{X} \cdot p^r (1-p)^X \right) \right]^2 \\ &=& \mathbb{E} \left[ \dfrac{d}{dp} \left( r \ln p + X \ln (1-p) + \ln \binom{X+r-1}{X} \right) \right]^2 \\ &=& \mathbb{E} \left[ - \left( 1-p \right)^{-1} \left( X - \dfrac{r(1-p)}{p}  \right) \right]^2 \\ &=& \left( 1-p \right)^{-2} \cdot \mathbb{E} \left( X -\mathbb{E}X \right)^2 \\ &=& \dfrac{1}{(1-p)^2} \cdot \dfrac{r(1-p)}{p^2} \\ \\ &=& \quad \quad \dfrac{r}{p^2(1-p)} \end{array} ")
        elif note == "Entropy":
            with c21:
                st.write("#### proof of Entropy")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} H(X, \theta) := \mathbb{E} \left[ \left. - \ln f(X,\theta) \right\vert \theta = p \right] &=& - \mathbb{E} \left[ \left( r\ln p + X \ln (1-p) + \ln \binom{X+r-1}{X} \right) \right] \\ &=& - \left( r \ln p + \mathbb{E}X \cdot \ln(1-p) + \mathbb{E}\left[ \ln \binom{X+r-1}{X} \right] \right) \\ &=& - \left( r \ln p + \dfrac{r(1-p)}{p} \cdot \ln(1-p) + \mathbb{E}\left[ \ln \binom{X+r-1}{X} \right] \right) \\ \end{array} ")

def nega_hypergeo_all_proofs(note: str):
    from .distr_illus import Nega_HyperGeo_show
    c1, _, c2 = st.columns([5, 1, 10])
    with c1:
        st.write("#### illustration") 
        N = st.number_input("Select a value of `N`", value=10, min_value=2, max_value=200, help="total number of elements")
        K = st.number_input("Select a value of `K`", value=7, min_value=0, max_value=N, help="total number of `success` elements")
        r = st.number_input("Select a value of `r`", value=2, min_value=0, max_value=(N-K), help="number of failures when experiment is stopped")
        Nega_HyperGeo_show(N, K, r)
    with c2:
        st.write("Beside some `combination expression tricks` on `HyperGeometric, Negative Binomial` distirbution, we have some notes in `Negative HyperGeometric` distribution")
        st.latex(r" \begin{array}{rcl} \displaystyle \sum_{k=0}^m \binom{a}{k} \binom{b}{m-k} &=& \displaystyle \binom{a+b+1}{m} \\ \displaystyle \dfrac{k+r}{r} \cdot \binom{k+r-1}{k} &=& \displaystyle \binom{k+r}{r} \\ \displaystyle (k+r)(k+r+1) \binom{k+r-1}{k} &=& \displaystyle r(r+1) \binom{k+r+1}{r+1} \end{array} ")
        c21, c22 = st.columns(2)
        if note == "cdf":
            with c21:
                st.write("#### proof of cdf")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{rcl} P(X < x) &=& \displaystyle \sum_{k=0}^{ \left\lfloor x \right\rfloor } P(X = x) &=& \displaystyle \sum_{k=0}^{ \left\lfloor x \right\rfloor } \dfrac{\binom{k+r-1}{k} \binom{N-r-k}{K-k}}{\binom{N}{K}} \end{array} ")
        elif note == "Expectation":
            with c21:
                st.write("#### proof of Expectation")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{rcl}  \mathbb{E}X = \displaystyle \sum_{k=0}^K k \cdot P(X=x) &=& \displaystyle \sum_{k=0}^K \left[ r\cdot\left( \dfrac{k+r}{r} \right) - r \right] P(X=x) \\ &=& r \cdot \left( \binom{N}{K}^{-1} \cdot \displaystyle \sum_{k=0}^K \underbrace{\left[ \frac{k+r}{r} \cdot\binom{k+r-1}{k} \right]} \cdot \binom{N-r-k}{K-k} \right) - r \displaystyle \left( \sum_{k=0}^K P(X=x) \right) \\ &=& \qquad r \quad \binom{N}{K}^{-1} \cdot \left( \displaystyle \sum_{k=0}^K \overbrace{\binom{k+r}{r}} \binom{N-r-k}{K-k} \right) \qquad - \qquad r \\ \\ &=& \displaystyle \quad \qquad r \qquad \binom{N}{K}^{-1} \cdot \binom{(k+r)+(N-r-k)+1}{k + (K-k)} \qquad - \qquad r \\ \\ &=& \qquad \qquad  r \qquad \binom{N}{K}^{-1} \qquad \cdot \qquad \binom{N+1}{K} \qquad - \qquad r \\ \\ &=& \qquad \qquad \quad r \quad \cdot \frac{K!(N-K)!}{N!} \cdot \frac{(N+1)!}{K!(N-K+1)!} \quad - \quad r \\ \\ &=& \qquad \qquad \qquad \dfrac{rK}{N-K+1} \end{array} ")
        elif note == "variance":
            with c21:
                st.write("#### proof of variance")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("This is easy to see that")
                st.latex(r" k^2 = (k+r)(k+r-1) - (2r + 1)k - r(r + 1) ")
                st.write("Therefore")
                st.latex(r" \mathbb{E}X^2 = \left[ \sum_{k=0}^K (k+r)(k+r-1) P(X=x) \right] - (2r + 1) \mathbb{E}X - r(r+1) ")
                st.write("and")
                st.latex(r" \begin{array}{ccl} \displaystyle \sum_{k=0}^K (k+r)(k+r-1) P(X=x) &=& \binom{N}{K}^{-1} \cdot \displaystyle \sum_{k=0}^K  \underbrace{\left[ (k+r)(k+r-1) \binom{k+r-1}{k} \right]} \cdot \binom{N-r-k}{K-k} \\  &=& \qquad \binom{N}{K}^{-1} \quad \cdot \quad \displaystyle \sum_{k=0}^K \left[ r(r+1) \binom{k+r+1}{k} \right] \binom{N-r-k}{K-k} \\ &=& \qquad \quad r(r+1) \cdot \binom{N}{K}^{-1} \cdot \displaystyle \binom{(N-r-k)+(k+r+1)+1}{(K-k)+k} \\ &=& \qquad \qquad r(r+1) \binom{N}{K}^{-1} \cdot \left[ \dfrac{K!(N-K)!}{N!} \cdot \dfrac{(N+2)!}{K!(N-K+2)} \right] \\ &=& \qquad \qquad \quad r(r+1) \quad \cdot \quad \dfrac{(N+2)(N+1)}{(N-K+2)(N-K+1)} \end{array} ")
                st.write("Hence")
                st.latex(r" \begin{array}{rcl} \mathbb{E}X^2 &=& \dfrac{r(r+1)(N+2)(N+1)}{(N-K+2)(N-K+1)} - \dfrac{(2r+1)rK}{N-K+1}-r(r+1) \\ &=& \qquad \qquad \dfrac{rK(n - r + Kr + 1)}{(N-K+2)(N-K+1)} \\ \Rightarrow \text{Var} X &=& \mathbb{E}X^2 - \left( \mathbb{E}X \right)^2 \\ &=& \dfrac{rK(n - r + Kr + 1)}{(N-K+2)(N-K+1)} - \left( \dfrac{rK}{N-K+1} \right)^2 \\ &=& \qquad \dfrac{rK(N+1)(N-K-r+1)}{(N-K+1)^2(N-K+2)} \end{array} ")

def unif_descrete_all_proofs(note: str):
    from .distr_illus import unif_descrete_show
    c1, _, c2 = st.columns([5, 1, 10])
    with c1:
        st.write("#### illustration") 
        N = st.number_input("Select a value of `n`", value=10, min_value=2, max_value=20, help="number of random points")
        a = st.number_input("Select a value of `a`", value=2, min_value=0, max_value=10, help="lower-bound of all random points")
        b = st.number_input("Select a value of `b`", value=7, min_value=0, max_value=a + 10, help="upper-bound for all random points")
        unif_descrete_show(N, a, b) 
    with c2:
        c21, c22 = st.columns(2)
        if note == "cdf":
            with c21:
                st.write("#### proof of cdf")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" P(X < x) = \sum_{i < x} P(X = i) = \dfrac{m}{k} ")
                st.write("where")
                st.latex(r" m = \lbrace i : a_{i-1} < x \leq a_i  \rbrace ")
        elif note == "Expectation":
            with c21:
                st.write("#### proof of Expectation")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \mathbb{E}X = \sum_{i=1}^k a_k P \left( X = a_i \right) = k^{-1} \sum_{i=1}^k a_i")
        elif note == "mode":
            with c21:
                st.write("#### proof of mode")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have nothing to prove")
        elif note == "median":
            with c21:
                st.write("#### proof of median")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have nothing to prove")
        elif note == "variance":
            with c21:
                st.write("#### proof of variance")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} \text{Var} X &=& \mathbb{E}X^2 - \left( \mathbb{E}X \right)^2 \\ &=& \displaystyle \left[ \sum_{i=1}^k a_i^2 P(X=a_i) \right] - \left[ \sum_{i=1}^k a_i P(X=a_i) \right]^2 \\ &=& \displaystyle k^{-1} \left( \sum_{i=1}^k a_i^2 \right) - k^{-2} \left( \sum_{i=1}^k a_i \right)^2 \end{array} ")
        elif note == "Skewness":
            with c21:
                st.write("#### proof of Skewness")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have nothing to prove for general case")
        elif note == "Kurtosis":
            with c21:
                st.write("#### proof of Kurtosis")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have nothing to prove for general case")
        elif note == "Fisher information":
            with c21:
                st.write("#### proof of Fisher information")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have nothing to prove for general case")
        elif note == "Entropy":
            with c21:
                st.write("#### proof of Entropy")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have nothing to prove for general case")
        elif note == "Characteristic func":
            with c21:
                st.write("#### proof of CF")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \varphi_X(t) = \mathbb{E} e^{itX} = \sum_{x=1}^k e^{it a_x} P(X = a_x) = k^{-1} \left( \sum_{x=1}^k e^{it a_x} \right) ")
        elif note == "Moment generating func":
            with c21:
                st.write("#### proof of MGF")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" M_X(t) = \mathbb{E} e^{tX} = \sum_{x=1}^k e^{ta_x} P(X = a_x) = k^{-1} \left( \sum_{x=1}^k e^{t a_x} \right) ")
        elif note == "Proba generating func":
            with c21:
                st.write("#### proof of PGF")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" G_X(t) = \mathbb{E} z^{X} = \sum_{x=1}^k z^{a_x} P(X = a_x) = k^{-1} \left( \sum_{x=1}^k z^{a_x} \right) ")

def unif_cts_all_proofs(note: str):
    from .distr_illus import unif_cts_show
    c1, _, c2 = st.columns([5, 1, 10])
    with c1:
        st.write("#### illustration") 
        a = st.number_input("Select a value of `a`", value=2, min_value=-10, max_value=10, help="lower-bound of all unif.cts")
        b = st.number_input("Select a value of `b`", value=a+1, min_value=a, max_value=a + 10, help="upper-bound for all unif.cts")
        unif_cts_show(a, b) 
    with c2:
        c21, c22 = st.columns(2)
        if note == "cdf":
            with c21:
                st.write("#### proof of cdf")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} P(X < x) := \displaystyle \int_{-\infty}^x f_X(t) dt &=& \displaystyle \int_{-\infty}^x \dfrac{1}{b-a} \cdot \mathcal{I}_{(a,b)}(t) dt \\ \\ & = & \left\lbrace  \begin{array}{ccl} 0 & & x \leq a \\ (b-a)^{-1} \int_{a}^x dt & & x \in (a, b] \\ 1 & & x > b \end{array} \right. \\ \\ & = & \left\lbrace  \begin{array}{ccl} 0 & & x \leq a \\ \frac{x-a}{b-a}  & & x \in (a, b] \\ 1 & & x > b \end{array} \right. \end{array} ")
        elif note == "Expectation":
            with c21:
                st.write("#### proof of expectation")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} \mathbb{E}X := \displaystyle \int_{\mathbb{R}} x f_X(x)dx &=& \displaystyle \int_{-\infty}^{\infty} x \cdot \left[ (b-a)^{-1} \mathcal{I}_{(a, b)}(x) \right] dx \\ &=& (b-a)^{-1} \displaystyle \int_a^b x dx \\  &=& \dfrac{b^2 - a^2}{b-a} &=& \dfrac{a+b}{2} \end{array} ")
        elif note == "mode":
            with c21:
                st.write("#### proof of mode")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("The `mode` of this distribution will be any value in (a, b) since")
                st.latex(r" P(X = x) = \dfrac{1}{b-a} \qquad \forall x \in (a, b) ")
        elif note == "median":
            with c21:
                st.write("#### proof of median")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We need to find $x_m$ such that")
                st.latex(r" P(X < x_m) = P(X > x_m) = 50\% ")
                st.write("Since")
                st.latex(r" P(X < x) = \left\lbrace \begin{array}{ccl} 0 & & x < a \\ \frac{x-a}{a-b} & & x \in (a, b) \\ 1 & & x > b \end{array} \right. ")
                st.write("So $x_m$ must be in $(a, b)$ and hence")
                st.latex(r" P(X < x_m) = \dfrac{x_m - a}{b - a} = \dfrac{1}{2} \Leftrightarrow x_m = \dfrac{b+a}{2}")
        elif note == "variance":
            with c21:
                st.write("#### proof of variance")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{lrlcr} \mathbb{E} X &=& \dfrac{b+a}{2} & &\text{see the proof in the Expectation} \\ \\ \mathbb{E} X^2 &=& \displaystyle \int_{\mathbb{R}} x^2 f_X(x)dx \\ &=&  \displaystyle \int_a^b \dfrac{x^2}{b-a}dx \\ &=& \quad \displaystyle \dfrac{b^3 - a^3}{3(b-a)} &=& \dfrac{a^2+ab+b^2}{3} \\ \\ \text{Var} X &=& \mathbb{E}X^2 - \left( \mathbb{E}X \right)^2 \\ &=& \dfrac{a^2+ab+b^2}{3} - \left( \dfrac{b+a}{2} \right)^2 &=& \qquad \dfrac{(b-a)^2}{12} \end{array} ")            
        elif note == "Skewness":
            with c21:
                st.write("#### proof of skewness")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("#### Approach 1")
                st.write("We have known")
                st.latex(r" \mathbb{E}\left( \dfrac{X - \mathbb{E}X}{ \sqrt{\text{Var}X}} \right)^3 := \mathbb{E}\left( \dfrac{X - \mu}{ \sigma} \right)^3 = \dfrac{\mathbb{E}X^3 - 3\mu\mathbb{E}X^2+2\mu^3}{\sigma^3} ")
                st.write("and")
                st.latex(r" \begin{array}{ccl} \mathbb{E}X^3 := \displaystyle \int_{\mathbb{R}} x^3 f_X(x) dx &=& \displaystyle  \int_a^b \dfrac{x^3}{b-a}dx \\ &=& \dfrac{b^4 - a^4}{4(b-a)} &=& \dfrac{(a^2+b^2)(b+a)}{4} \end{array} ")
                st.write(r"where $\mu = \mathbb{E}X = \frac{a+b}{2}$ and $\sigma^2 = \text{Var}X = \frac{(b-a)^2}{12}$. Now apply all the results found in the previous parts, we obtain")
                st.latex(r" \begin{array}{ccl} \mathbb{E}X^3 - 3\mu\mathbb{E}X^2+2\mu^3 &=& \dfrac{(a+b)(a^2 + b^2)}{4} - 3\cdot\dfrac{a+b}{2}\cdot\dfrac{a^2+ab+b}{3} + \dfrac{2(a+b)^3}{8} \\ &=& (a+b) \left[ \dfrac{a^2+b^2}{4} - \dfrac{a^2+ab+b}{2} + \dfrac{(a+b)^2}{4} \right]\\ &=& (a+b) \left[ \dfrac{(a^2+b^2)-2(a^2+ab+b^2)+(a^2+2ab+b^2)}{4} \right] &=& 0\\ \Rightarrow \mathbb{E}\left( \dfrac{X - \mathbb{E}X}{ \sqrt{\text{Var}X}} \right)^3 &=& 0 \end{array} ")
                st.write("---------")
                st.write("#### Approach 2")
                st.write("Directly, we have")
                st.latex(r" \begin{array}{ccl}  \mathbb{E}\left( \dfrac{X - \mathbb{E}X}{ \sqrt{\text{Var}X}} \right)^3 &=& \displaystyle \int_{\mathbb{R}} \left( \dfrac{x - \mu}{\sigma} \right)^3 f_X(x) dx \\ &=& \displaystyle (b-a)^{-1} \int_a^b \left( \dfrac{x - \frac{b+a}{2}}{\sigma} \right)^3 dx \\ &=& \displaystyle (b-a)^{-1} \int_{-(b-a)/2}^{(b-a)/2} \left( \dfrac{t}{\sigma} \right)^3 dt \qquad & & \text{by letting } t = x - \frac{a+b}{2} \\ &=& \dfrac{1}{(b-a)\cdot \sigma^3} \displaystyle \int_{-(b-a)/2}^{(b-a)/2}t^3 dt &=& \qquad 0 \end{array} ")
        elif note == "Kurtosis":
            with c21:
                st.write("#### proof of Kurtosis")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl}  \mathbb{E}\left( \dfrac{X - \mathbb{E}X}{ \sqrt{\text{Var}X}} \right)^4  &=& \displaystyle \int_{\mathbb{R}} \left( \dfrac{x - \mu}{\sigma} \right)^4 f_X(x) dx \\  &=& \displaystyle (b-a)^{-1} \int_a^b \left( \dfrac{x - \frac{b+a}{2}}{\sigma} \right)^4 dx \\  &=& \displaystyle (b-a)^{-1} \int_{-(b-a)/2}^{(b-a)/2} \left( \dfrac{t}{\sigma} \right)^4 dt \qquad & & \text{by letting } t = x - \frac{a+b}{2} \\  &=& \dfrac{1}{(b-a)\cdot \sigma^4} \cdot \underbrace{\dfrac{2}{5} \cdot \left[ \dfrac{b-a}{2} \right]^5} \\ &=& \dfrac{1}{(b-a)\cdot \left( \frac{(b-a)}{12} \right)^2} \cdot \dfrac{(b-a)^5}{80} &=& \dfrac{144}{80} \quad = \quad \dfrac{9}{5} \end{array} ")          
        elif note == "Characteristic func":
            with c21:
                st.write("#### proof of CF")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \varphi_X(t) := \mathbb{E} e^{itX} \quad=\quad \int_{\mathbb{R}} e^{itx} f_X(x)dx \quad =\quad \int_a^b \dfrac{e^{itx}}{b-a} dx \quad = \quad \dfrac{e^{itb} - e^{ita}}{it(b-a)} ")
        elif note == "Moment generating func":
            with c21:
                st.write("#### proof of MGF")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" M_X(t) := \mathbb{E} e^{tX} \quad=\quad \int_{\mathbb{R}} e^{tx} f_X(x)dx \quad =\quad \int_a^b \dfrac{e^{tx}}{b-a} dx \quad = \quad \dfrac{e^{tb} - e^{ta}}{(b-a)t} ")
        elif note == "Entropy":
            with c21:
                st.write("#### proof of Entropy")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} H_X(a,b) := \mathbb{E}\left[ -\ln f_X(x) \right] &=& \displaystyle - \int_{\mathbb{R}} \left( \ln f_X(x) \right) \cdot f_X(x) dx \\ &=& - \displaystyle \int_a^b \ln \left( \dfrac{1}{b-a} \right) \cdot \dfrac{1}{b-a} dx \\ &=& - \ln \left( \dfrac{1}{b-a} \right) \cdot \dfrac{x \Big \vert_{a}^{b}}{b-a} &=& \ln \left( b-a \right) \end{array} ")
        elif note == "Fisher information": 
            with c21:
                st.write("#### proof of Fisher information")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} I_X(b) &=& \mathbb{E} \left[ \dfrac{d}{db} \ln f_X(x,a,b) \right]^2 &=& \mathbb{E}\left[ \dfrac{d}{db} \ln \left( \frac{1}{b-a} \right) \right]^2 \\ & & & = & \displaystyle \int_a^b \left( \dfrac{1}{b-a} \right)^2 f_X(x) dx &=& \dfrac{1}{(b-a)^2} \\ I_X(a) &=& \mathbb{E} \left[ \dfrac{d}{da} \ln f_X(x,a,b) \right]^2 &=& \mathbb{E}\left[ \dfrac{d}{da} \ln \left( \frac{1}{b-a} \right) \right]^2 \\ & & & = & \displaystyle \int_a^b \left( - \dfrac{1}{b-a} \right)^2 f_X(x) dx &=& \dfrac{1}{(b-a)^2} \end{array} ")

def normal_all_proofs(note):
    from .distr_illus import normal_show
    c1, _, c2 = st.columns([5, 1, 10])
    with c1:
        st.write("#### illustration") 
        m = st.number_input("Select a value of `muy`", value=0, min_value=-10, max_value=10, help="muy")
        s = st.number_input("Select a value of `sigma`", value=1.0, min_value=0.01, help="standard deviation")
        normal_show(m, s) 
    with c2:
        st.write("We have some notes in normal distribution")
        st.latex(r" \begin{array}{ccl} \erf (x) &=& \displaystyle \dfrac{2}{\sqrt{\pi}} \int_0^x e^{-z^2} dz \\ \ln f_X(x, \mu, \sigma) &=& -\frac{1}{2} \ln (2\pi) - \frac{1}{2} \ln \sigma - \frac{(x-\mu)^2}{2\sigma^2} \end{array} ")
        c21, c22 = st.columns(2)
        if note == "cdf":
            with c21:
                st.write("#### proof of cdf")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl}  P(X < x) := \displaystyle \int_{-\infty}^x f_X(t)dt &=& \displaystyle \int_{-\infty}^x \dfrac{e^{-\frac{(t-\mu)^2}{2\sigma^2}}}{\sigma \sqrt{2\pi}} d t\\ \\ &=& \displaystyle \int_{-\infty}^{(x-\mu)/\sigma} \dfrac{e^{-\omega^2/2}}{\sigma \sqrt{2\pi}} \sigma d\omega & & \text{where } \omega = (t - \mu)/\sigma \\ \\  &=&  \displaystyle \int_{(-\infty, 0)} + \int_{0}^{(x-\mu)/\sigma} \dfrac{1}{\sqrt{2\pi}} e^{-\omega^2/2} d\omega \\ \\ &:=& \dfrac{1}{2} \left[ 1 + \erf \left( \dfrac{x-\mu}{\sigma \sqrt{2}} \right) \right] \end{array} ")
        elif note == "Expectation":
            with c21:
                st.write("#### proof of expectation")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl}  \mathbb{E}X := \displaystyle \int_{\mathbb{R}} xf_X(x)dx &=& \dfrac{1}{\sigma \sqrt{2\pi}} \displaystyle \int_{-\infty}^{\infty} x \cdot \exp\left( \frac{-(x-\mu)^2}{2\sigma^2} \right) dx \\ \\ &=& \dfrac{1}{\sigma\sqrt{2\pi}} \displaystyle \int_{-\infty}^{\infty} \left( \sigma t + \mu \right) \cdot \exp\left( \frac{-t^2}{2} \right) \cdot (\sigma dt) \\ \\ &=& \displaystyle \left( \dfrac{\sigma}{\sqrt{2\pi}} \underbrace{\int_{-\infty}^{\infty} t \cdot \exp\left( \frac{-t^2}{2} \right) dt} \right) + \mu \cdot \underbrace{\left( \dfrac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \exp\left( \frac{-t^2}{2} \right) dt \right)} \\ &=& \qquad \qquad \qquad \quad 0 \qquad \qquad \qquad + \quad \mu \qquad \quad \cdot \quad \quad 1 &=& \mu \end{array} ")            
        elif note == "mode":
            with c21:
                st.write("#### proof of mode")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{crl} x_{\text{mode}} := \underset{{x\in\mathbb{R}}}{\text{argmax}} \quad f_X(x) &=& \displaystyle \underset{{x\in\mathbb{R}}}{\text{argmax}} \left( \frac{1}{\sigma \sqrt{2\pi}} \exp \left( -\frac{(x-\mu)^2}{2\sigma^2} \right) \right) \\ \\ &=& \Big\lbrace x: \frac{1}{\sigma \sqrt{2\pi}} \exp \left( -\frac{(x-\mu)^2}{2\sigma^2} \right) \to \max \Big \rbrace \\ \\ &=& \Big\lbrace x:  \frac{(x-\mu)^2}{2\sigma^2} \to \min\Big \rbrace &=& \mu \end{array} ")
        elif note == "median":
            with c21:
                st.write("#### proof of median")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We need to find $x_m$ such that")
                st.latex(r" P(X < x_m) = P(X > x_m) = 50\% ")
                st.write("Hence")
                st.latex(r" \begin{array}{ccl} F_X(x_m) = \dfrac{1}{2} \left[ 1 + \text{erf} \left( \dfrac{x_m - \mu}{\sigma \sqrt{2}} \right) \right] = \frac{1}{2} & \Rightarrow & \dfrac{x_m - \mu}{2} = 0 & \Rightarrow & x_m = \mu \end{array} ")
        elif note == "Moment generating func":
            with c21:
                st.write("#### proof of MGF")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} M_X(t) := \mathbb{E} e^{tX} &=& \displaystyle \int_{\mathbb{R}} e^{tx} f_X(x) dx \\ &=& \displaystyle \dfrac{1}{\sigma \sqrt{2\pi}} \int_{\mathbb{R}} e^{tx} \exp \left( -\dfrac{(x - \mu)^2}{2\sigma^2} \right) dx \qquad \text{now letting } z = \dfrac{x-\mu}{\sigma} \\ &=& \displaystyle \dfrac{1}{\sqrt{2\pi}} \int_{\mathbb{R}} e^{t(\sigma z + \mu)} \exp \left( -\dfrac{z^2}{2} \right) dz \\ &=& \displaystyle e^{\mu t} \cdot \left[ \dfrac{1}{2\pi} \int_{\mathbb{R}} \exp \left( -\frac{z^2}{2} + \sigma t z  \right) dz \right] \\ &=& \displaystyle e^{\mu t} \cdot \left[ \dfrac{1}{2\pi} \int_{\mathbb{R}} \exp \left( - \frac{(z-\sigma t)^2}{2} \right) \cdot \exp \left( \frac{\sigma^2 t^2}{2} \right) dz \right] \\ &=& \displaystyle \exp \left( \mu t + \frac{\sigma^2 t^2}{2} \right) \cdot \left[ \dfrac{1}{2\pi} \int_{\mathbb{R}} \exp \left( - \frac{(z-\sigma t)^2}{2} \right) dz \right] \\ &=& \exp \left( \mu t + \dfrac{\sigma^2 t^2}{2} \right) \cdot 1 \end{array} ")
        elif note == "variance":
            with c21:
                st.write("#### proof of variance")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl}  \mathbb{E}X^2 := \left. \left[ \dfrac{d^2}{dt^2} M_X(t) \right] \right \vert_{t=0} &=& \left. \left[ \dfrac{d^2}{dt^2} \left( \exp \left( \mu t + \dfrac{\sigma^2 t^2}{2} \right) \right) \right] \right \vert_{t=0} \\ &=& \displaystyle \left. \left[ \dfrac{d}{dt} \underbrace{\left(  \dfrac{d}{dt} \exp \left( \mu t + \dfrac{\sigma^2 t^2}{2} \right) \right)} \right] \right \vert_{t=0} \\ &=& \left. \left[ \dfrac{d}{dt}\left[ (\mu + \sigma^2 t) \cdot \exp \left( \mu t + \dfrac{\sigma^2 t^2}{2} \right) \right] \right] \right \vert_{t=0} \\ &=& \left. \left[ \left( \left( \mu + \sigma^2 t^2 \right)^2 + \sigma^2 \right) \cdot \exp \left( \mu t + \dfrac{\sigma^2 t^2}{2} \right) \right] \right \vert_{t=0} &=& \mu^2 + \sigma^2 \end{array} ")
                st.write("Therefore")
                st.latex(r" \text{Var} X = \mathbb{E}X^2 - (\mathbb{E} X)^2 = \sigma^2 ")
        elif note == "Characteristic func":
            with c21:
                st.write("#### proof of CF")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl}  \varphi_X(t) := \mathbb{E} e^{itX} &=& \displaystyle \int_{\mathbb{R}} e^{itx} f_X(x) dx \\  &=& \displaystyle \dfrac{1}{\sigma \sqrt{2\pi}} \int_{\mathbb{R}} e^{itx} \exp \left( -\dfrac{(x - \mu)^2}{2\sigma^2} \right) dx & & \text{now letting } z = \dfrac{x-\mu}{\sigma} \\  &=& \displaystyle \dfrac{1}{\sqrt{2\pi}} \int_{\mathbb{R}} e^{it(\sigma z + \mu)} \exp \left( -\dfrac{z^2}{2} \right) dz \\  &=& \displaystyle e^{i \mu t} \cdot \left[ \dfrac{1}{2\pi} \int_{\mathbb{R}} \exp \left( -\frac{z^2}{2} + i \sigma t z  \right) dz \right] \\  &=& \displaystyle e^{i \mu t} \cdot \left[ \dfrac{1}{2\pi} \int_{\mathbb{R}} \exp \left( - \frac{(z-i \sigma t)^2}{2} \right) \cdot \exp \left( -\frac{\sigma^2 t^2}{2} \right) dz \right] \\  &=& \displaystyle \exp \left( i \mu t - \frac{\sigma^2 t^2}{2} \right) \cdot \left[ \dfrac{1}{2\pi} \int_{\mathbb{R}} \exp \left( - \frac{(z - i \sigma t)^2}{2} \right) dz \right] &=& \exp \left( i \mu t - \dfrac{\sigma^2 t^2}{2} \right) \end{array} ")
        elif note == "Skewness":
            with c21:
                st.write("#### proof of skewness")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("Generally, we have")
                st.latex(r" \mathbb{E} \left( X - \mu \right)^p = \left \lbrace \begin{array}{ccl} 0 & & n = 2k + 1 \\ \sigma^p \cdot (p-1)!! && n= 2k \end{array} \right. ")
                st.write("where `!!` denotes the `double factorial`")
                st.latex(r" \begin{array}{ccr} (2k)!! &=& (2k)\cdot(2k-2) \cdots 2 \\   (2k - 1)!! &=& (2k-1)\cdot(2k-3) \cdots 1  \end{array}")
                st.write("Now, we will prove the stament above,")
                st.latex(r"\mathbb{E} \left( X - \mu \right)^p = \int_{\mathbb{R}} (x - \mu)^p f_X(x) dx = \dfrac{1}{\sqrt{2\pi}} \int_{\mathbb{R}} (\sigma t)^p \cdot e^{-t^2 / 2} dt, \qquad \text{ where } t = \frac{x-\mu}{\sigma}")
                st.write("If $p$ is odd, then the `integration` will be `vanished` on the symmetric domain")
                st.latex(r" \int_{-a}^a t^{2k+1} e^{-t^2} dt \quad = \quad 0 \qquad \forall a , \forall k ")
                st.write("If $p$ is even, then applying `integration by part`")
                st.latex(r" \begin{array}{ccrcl} I_2 &:=& \displaystyle \frac{1}{\sqrt{2\pi}}\int_{\mathbb{R}} t^{2} e^{-t^2/2} dt &=& \displaystyle \frac{1}{\sqrt{2\pi}} \int_{\mathbb{R}} \underset{u}{\underbrace{t}} \cdot \underset{dv}{\underbrace{\left( te^{-t^2/2} dt \right)}} \\  && &=& \underset{0 \text{ (using L'Hopital)} }{\underbrace{\left( -\frac{1}{\sqrt{2\pi}} t \cdot e^{-t^2/2} \right)\Big \vert_{t \to \pm \infty}}} + \displaystyle \frac{1}{\sqrt{2\pi}} \int_{\mathbb{R}} e^{-t^2/2} \cdot (1 dt) &=& 1 \\ \\    I_4 &:=& \displaystyle \frac{1}{\sqrt{2\pi}} \int_{\mathbb{R}} t^{4} e^{-t^2/2} dt &=& \left( -\frac{1}{\sqrt{2\pi}} t^3 \cdot e^{-t^2/2} \right)\Big \vert_{t \to \pm \infty} + \displaystyle \underset{3 I_2}{\underbrace{\frac{1}{\sqrt{2\pi}} \int_{\mathbb{R}} e^{-t^2/2} \cdot (3t^2 dt)}} &=& 3 \\ \\    I_{2k} &:=& \displaystyle \frac{1}{\sqrt{2\pi}} \int_{\mathbb{R}} t^{2k} e^{-t^2/2} dt &=& \left( -\frac{1}{\sqrt{2\pi}}t^{2k-1} \cdot e^{-t^2/2} \right)\Big \vert_{t \to \pm \infty} + \displaystyle \underset{(2k - 1)\cdot I_{2k-1}}{\underbrace{\frac{1}{\sqrt{2\pi}} \int_{\mathbb{R}} e^{-t^2/2} \cdot ((2k-1)t^{2(k-1)} dt)}} &=& (2k - 1)!! \\ \end{array} ")
                st.write("Therefore")
                st.latex(r" \mathbb{E} \left( \frac{X- \mathbb{E}X}{\sqrt{\text{Var}X}} \right)^3= \dfrac{\mathbb{E}(X - \mu)^3}{\sigma^3} = 0 ")
        elif note == "Kurtosis":
            with c21:
                st.write("#### proof of Kurtosis")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("See the proofs in the Skewness, so we have")
                st.latex(r" \mathbb{E} \left( \frac{X- \mathbb{E}X}{\sqrt{\text{Var}X}} \right)^4= \dfrac{\mathbb{E}(X - \mu)^4}{\sigma^4} = (4 - 1)!! = 3 ")
        elif note == "Entropy":
            with c21:
                st.write("#### Proof of Entropy")
            with c22:
                button_trig = st.button("Show the proof")                
            if button_trig: 
                st.write("We have")
                st.latex(r" \begin{array}{ccl} H_X(\mu, \sigma^2) &:=& \mathbb{E} \left[ - \ln f_X(\mu, \sigma^2) \right] \\ &=& \displaystyle -\int_{\mathbb{R}} \underbrace{\ln \left[ \frac{1}{\sigma \sqrt{2\pi}} \exp \left( -\frac{(x-\mu)^2}{2\sigma^2} \right) \right]} \cdot \left( \frac{1}{\sigma \sqrt{2\pi}} \exp \left( -\frac{(x-\mu)^2}{2\sigma^2} \right) \right) dx \\ \\ &=& - \displaystyle \int \left[ - \ln(\sigma \sqrt{2\pi}) - \frac{(x-\mu)^2}{2\sigma^2} \right] \cdot \left( \frac{1}{\sigma \sqrt{2\pi}} \exp \left( -\frac{(x-\mu)^2}{2\sigma^2} \right) \right) dx \\ \\ &=& \displaystyle \frac{1}{\sigma \sqrt{2\pi}} \int  \left[ \ln(\sigma \sqrt{2\pi}) + \frac{(x-\mu)^2}{2\sigma^2} \right] \cdot \exp \left( -\frac{(x-\mu)^2}{2\sigma^2} \right) dx \\ \\ &=& \ln(\sigma \sqrt{2\pi}) \quad + \quad \displaystyle \frac{1}{\sigma \sqrt{2\pi}} \int \frac{(x-\mu)^2}{2\sigma^2} \cdot \exp \left( -\frac{(x-\mu)^2}{2\sigma^2} \right) dx \end{array} ")
                st.write(r"Letting $z = \dfrac{x - \mu}{\sigma}$, we obtain")
                st.latex(r" \begin{array}{ccl} H_X(\mu, \sigma^2) &=& \ln(\sigma \sqrt{2\pi}) \quad + \quad \displaystyle \frac{1}{\sigma \sqrt{2\pi}} \int \frac{-z^2}{2} \cdot \exp \left( \frac{z^2}{2} \right) (\sigma dz) \\ &=& \ln(\sigma \sqrt{2\pi}) \quad + \quad \displaystyle \dfrac{1}{2} \cdot \underset{1 \text{ (refer the proof in Skewness })}{\underbrace{\left( \frac{1}{\sqrt{2\pi}} \int z^2 \cdot \exp \left( -\frac{z^2}{2} \right)dz \right)}} \\ &=& \qquad \underset{\frac{1}{2} \ln ( (\sigma \sqrt{2\pi})^2 \cdot e )}{\underbrace{\ln(\sigma \sqrt{2\pi}) \quad + \quad \dfrac{1}{2} \quad \cdot \quad \ln e}} &=& \dfrac{1}{2} \ln \left( 2 \pi e \sigma^2 \right)  \end{array} ")
        elif note == "Fisher information":
            with c21:
                st.write("#### Proof of Fisher information")
            with c22:
                button_trig = st.button("Show the proof")                
            if button_trig: 
                st.write("We have 2 cases,")
                st.write("--------")
                st.write(r"**Case 1.** Find $I_X(\mu, \sigma)$, we have")                 
                st.latex(r" \begin{array}{l} \qquad \left \lbrace \begin{array}{ccl} \dfrac{d}{d\mu} \ln f_X(x, \mu, \sigma) &=& \dfrac{x-\mu}{\sigma^2} \\ \dfrac{d}{d\sigma} \ln f_X(x, \mu, \sigma) &=& \dfrac{1}{\sigma} -\dfrac{(x-\mu)^2}{\sigma^3} &=& \dfrac{-((x - \mu)^2 - \sigma^2)}{\sigma^3} \\ \end{array} \right. \\ \\ \Rightarrow  \left \lbrace \begin{array}{ccl} \mathbb{E} \left[ \dfrac{d}{d\mu} \ln f_X \right]^2 &=& \mathbb{E} \left( \dfrac{X-\mu}{\sigma^2} \right)^2 &=& \dfrac{\text{Var}X}{\sigma^4} &=& \dfrac{1}{\sigma^2} \\ \mathbb{E} \left[ \dfrac{d}{d\sigma} \ln f_X \right]^2 &=& \mathbb{E} \left( \dfrac{(X-\mu)^2 - \sigma^2}{\sigma^3} \right)^2 &=& \dfrac{\mathbb{E}\left[ (X-\mu)^2 - \sigma^2 \right]^2}{\sigma^6} &=& \dfrac{2}{\sigma^2} \\ \mathbb{E} \left[ \dfrac{d^2}{d \mu d\sigma} f_X \right] &=& \mathbb{E} \left( \dfrac{2(X - \mu)}{\sigma^3} \right) &=& \dfrac{2}{\sigma^3} \mathbb{E}(X - \mu) &=& 0  \end{array} \right. \\ \\ \Rightarrow I_X (\mu, \sigma) \quad = \quad \left[ \begin{array}{cc} \mathbb{E} \left[ \dfrac{d}{d\mu} \ln f_X \right]^2 & \mathbb{E} \left[ \dfrac{d^2}{d\mu d\sigma} f_X \right] \\ \mathbb{E} \left[ \dfrac{d^2}{d\sigma d\mu} \ln f_X \right] & \mathbb{E} \left[ \dfrac{d}{ d\sigma} f_X \right]^2 \end{array} \right] \quad = \quad \left[ \begin{array}{cc} \sigma^{-2} & 0 \\ 0 & 2 \sigma^{-2} \end{array} \right] \end{array} ")
                st.write("--------")
                st.write(r"**Case 2.** Find $I_X(\mu, \sigma^2)$, do the same thing with noting that for $\theta = \sigma^2 $, then")
                st.latex(r" \begin{array}{l}  \qquad \left \lbrace \begin{array}{ccl}  \dfrac{d}{d\mu} \ln f_X(x, \mu, \sigma) &=& \dfrac{x-\mu}{\theta} \\  \dfrac{d}{d\theta} \ln f_X(x, \mu, \sigma) &=& \dfrac{-1}{2\theta} +\dfrac{(x-\mu)^2}{2\theta^2} &=& \dfrac{(x - \mu)^2 - \theta}{2 \theta^2} \\ \end{array} \right. \\ \\  \Rightarrow  \left \lbrace \begin{array}{ccl}  \mathbb{E} \left[ \dfrac{d}{d\mu} \ln f_X \right]^2 &=& \mathbb{E} \left( \dfrac{X-\mu}{\theta} \right)^2 &=& \dfrac{\text{Var}X}{\theta^2} &=& \dfrac{1}{\theta} \\  \mathbb{E} \left[ \dfrac{d}{d\theta} \ln f_X \right]^2 &=& \mathbb{E} \left( \dfrac{(X-\mu)^2 - \theta}{2 \theta^2} \right)^2 &=& \dfrac{\mathbb{E}\left[ (X-\mu)^2 - \theta \right]^2}{4 \theta^4} &=& \dfrac{1}{2\theta^2} \\  \mathbb{E} \left[ \dfrac{d^2}{d \mu d\theta} f_X \right] &=& \mathbb{E} \left( \dfrac{-(X - \mu)}{\theta^2} \right) &=& \dfrac{-1}{\theta^2} \mathbb{E}(X - \mu) &=& 0  \end{array} \right. \\ \\ \Rightarrow I_X (\mu, \sigma) \quad = \quad \left[ \begin{array}{cc} \theta^{-1} & 0 \\ 0 & 1/ (2 \theta^{2}) \end{array} \right] \quad = \quad \left[ \begin{array}{cc} 1/ \sigma^{2} & 0 \\ 0 & 1 / (2 \sigma^{4}) \end{array} \right] \end{array} ")

def expo_all_proofs(note):
    from .distr_illus import expon_show
    c1, _, c2 = st.columns([5, 1, 10])
    with c1:
        st.write("#### illustration") 
        lambd = st.number_input("Select a value of `lambda`", value=0.1, min_value=0.01, max_value=9.99, help="lambda")
        expon_show(lambd)
    with c2:
        st.write("We have some notes in `exponential distribution`")
        st.latex(r" \begin{array}{lclrl}  \displaystyle \int_0^{\infty} x^k  \lambda e^{-\lambda x} dx &=& \left. \dfrac{d}{dt^k} \left( \dfrac{\lambda}{\lambda -t} \right) \right \vert_{t=0} &=& \dfrac{\lambda k!}{\lambda^{k+1}} &=& \dfrac{k!}{\lambda^k} \end{array} ")
        c21, c22 = st.columns(2)
        if note == "cdf":
            with c21:
                st.write("#### proof of cdf")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} P(X < x) := \displaystyle \int_{-\infty}^x f_X(t) dt &=& \displaystyle \int_0^x \lambda e^{-\lambda t} dt \\ &=& (-e^{-\lambda t}) \Big \vert_{t = 0}^{t \to x} &=& \displaystyle 1 - e^{-\lambda x} \end{array} ")
        elif note == "mode":
            with c21:
                st.write("#### proof of mode")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} x_{\text{mode}} := \underset{x \in \mathbb{R}}{\text{argmax}} \quad f_X(x) &=& \underset{x \in \mathbb{R}}{\text{argmax}} \left( \lambda e^{-\lambda x}  \cdot \mathcal{I}_{[0, \infty)}(x) \right) \\ &=& \underset{x \geq 0}{\text{argmax}} \quad e^{-\lambda x} \\&=& 0 \end{array} ")
        elif note == "median":
            with c21:
                st.write("#### proof of median")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} x_m := \lbrace x: F_X(x) = \frac{1}{2} \rbrace &=& \Big \lbrace x \geq 0 \Big\vert 1 - e^{-\lambda x} = \frac{1}{2} \Big \rbrace \\ &=& \Big \lbrace x \geq 0 \Big\vert -\lambda x = \ln \left( \frac{1}{2} \right) \Big \rbrace &=& \dfrac{\ln 2}{\lambda} \end{array} ")
        elif note == "Expectation":
            with c21:
                st.write("#### proof of Expectation")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("By the note in this distribution, we have")
                st.latex(r" \mathbb{E}X := \int_{\mathbb{R}} xf_X(x) dx = \int_0^{\infty} x \lambda e^{-\lambda x} dx = \dfrac{1!}{\lambda} = \lambda^{-1}  ")
                st.write("-------")
                st.write("Now we will prove the note in this distribution")
                st.latex(r" \begin{array}{ccl} I_1 &:=& \displaystyle \int_0^{\infty} x \lambda e^{-\lambda x} dx  &=& \left( - x e^{-\lambda x} \right) \Big \vert_{x=0}^{x \to \infty} + \displaystyle \int_0^{\infty} e^{-\lambda x} dx \\ &&&=& \qquad 0 \qquad \qquad + \dfrac{1}{\lambda} &=& \lambda^{-1} \\ I_2 &:=& \displaystyle \int_0^{\infty} x^2 \lambda e^{-\lambda x} dx &=& \underset{\text{ tends to 0 by L'Hopital}}{\underbrace{\left( - x^2 e^{-\lambda x} \right) \Big \vert_{x=0}^{x \to \infty}}} + \displaystyle \underset{ 2 \cdot \lambda^{-1} \cdot I_1 }{\underbrace{\int_0^{\infty} e^{-\lambda x} \cdot \left( 2x dx \right)}} &=& 2\lambda^{-2} \\ I_k &:=& \displaystyle \int_0^{\infty} x^k \lambda e^{-\lambda x} dx &=& \underset{\text{ tends to 0 by L'Hopital}}{\underbrace{\left( - x^{k} e^{-\lambda x} \right) \Big \vert_{x=0}^{x \to \infty}}} + \displaystyle \underset{ k \cdot \lambda^{-1} \cdot I_{k-1} }{\underbrace{\int_0^{\infty} e^{-\lambda x} \cdot \left( kx^{k-1} dx \right)}} &=& k!\lambda^{-k} \end{array} ")
                st.write("and")
                st.latex(r" \begin{array}{ccl} \dfrac{d^k}{dt^k} \left( \dfrac{1}{\lambda - t} \right) &=& \dfrac{d^{k-1}}{dt^{k-1}} \underset{(\lambda - t)^{-2}}{\underbrace{ \left( \dfrac{d}{dt} \left( \lambda - t \right)^{-1} \right)}} \\ &=& \dfrac{d^{k-2}}{dt^{k-2}} \underset{2(\lambda - t)^{-3}}{\underbrace{\left( \dfrac{d}{dt} (\lambda - t)^{-2} \right)}} \\ &=& ... \\ &=& k!(\lambda - t)^{-(k+1)} \end{array} ")
        elif note == "variance":
            with c21:
                st.write("#### proof of variance")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} \text{Var}X := \mathbb{E}X^2 - \left( \mathbb{E}X \right)^2 &=& \displaystyle \underbrace{\left( \int_0^{\infty} x^2 \lambda e^{-\lambda x} dx \right)} - \left( \lambda^{-1} \right)^{2} \\ &=& \qquad \left[ 2! \cdot \lambda^{-2} \right] \quad - \quad \lambda^{-2} &=& \lambda^{-2} \end{array} ")
        elif note == "Skewness":
            with c21:
                st.write("#### proof of Skewness")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} \mathbb{E}\left( \frac{X - \mathbb{E}X}{\sqrt{ \text{Var}X }} \right)^3 &=& \dfrac{\mathbb{E}X^3 - 3\mu \mathbb{E}X^2 + 2\mu^3}{\sigma^3} & \text{where } \mu = \lambda^{-1}, & \sigma^2 = \lambda^{-2} \\ \\ &=& \dfrac{\left( 3! \cdot \lambda^{-3} \right)-3\lambda^{-1} \cdot \left( 2! \cdot \lambda^{-2} \right) + 2 \left( \lambda^{-1} \right)^3}{\lambda^{-3}} \\ \\ &=& \qquad (3!) \quad - \quad 3 \cdot (2!) \quad + \quad 2 &=& 2 \end{array} ")
        elif note == "Kurtosis":
            with c21:
                st.write("#### proof of Kurtosis")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl}  \mathbb{E}\left( \frac{X - \mathbb{E}X}{\sqrt{ \text{Var}X }} \right)^4 &=& \dfrac{\mathbb{E}X^4 - 4\mu \mathbb{E}X^3 + 6 \mu^2 \mathbb{E}X^2 -3\mu^4}{\sigma^4} & \text{where } \mu = \lambda^{-1}, & \sigma^2 = \lambda^{-2} \\ \\  &=& \dfrac{\left( 4! \cdot \lambda^{-4} \right) - 4\lambda^{-1} \cdot \left( 3! \cdot \lambda^{-3} \right) + 6 \lambda^{-2} \left( 2! \cdot \lambda^{-2} \right) - 3 \lambda^{-4}}{\lambda^{-4}} \\ \\  &=& \qquad (4!) \quad - \quad 4 \cdot (3!) \quad + \quad 6 \cdot (2!) \quad - \quad 3 &=& 9  \end{array} ")        
        elif note == "Characteristic func":
            with c21:
                st.write("#### proof of CF")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} \varphi_X(t) := \mathbb{E}e^{itX} &=& \displaystyle \int_0^{\infty} e^{itx} \cdot \lambda e^{-\lambda x} dx \\ &=& \lambda \displaystyle \int_0^{\infty} e^{(it -\lambda)x} dx \\ &=& \displaystyle \dfrac{\lambda}{\lambda - it} \left( 1 - \underset{0 \text{ (for all } \lambda > 0) }{\underbrace{\lim_{x\to \infty} \left( e^{(it - \lambda)x} \right)}} \right) &=& \dfrac{\lambda}{\lambda - it} \end{array} ")
        elif note == "Moment generating func":
            with c21:
                st.write("#### proof of MGF")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl}  M_X(t) := \mathbb{E}e^{tX} &=& \displaystyle \int_0^{\infty} e^{tx} \cdot \lambda e^{-\lambda x} dx \\  &=& \lambda \displaystyle \int_0^{\infty} e^{(t -\lambda)x} dx \\  &=& \displaystyle \dfrac{\lambda}{\lambda - t} \left( 1 - \underset{0 \text{ (if } (t-\lambda) < 0) }{\underbrace{\lim_{x\to \infty} \left( e^{(t - \lambda)x} \right)}} \right)  &=& \dfrac{\lambda}{\lambda - t} \qquad \forall t < \lambda \end{array} ")
        elif note == "Entropy":
            with c21:
                st.write("#### proof of Entropy")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl}  H_X(\lambda) := \mathbb{E} \left[ - \ln f_X(X, \lambda) \right] &=& - \displaystyle \int_0^{\infty} \ln \left( \lambda e^{-\lambda x} \right) \cdot \lambda e^{-\lambda x} dx \\ &=& - \displaystyle \int_0^{\infty} \left[ -\lambda x + \ln \lambda \right] \cdot \lambda e^{-\lambda x} dx \\ &=& \displaystyle \underset{\lambda \cdot \lambda^{-1} = 1}{\underbrace{\left( \lambda \cdot \int_0^{\infty} \lambda xe^{-\lambda x} dx \right)}} - \left[ (\ln \lambda) \cdot \underset{1}{\underbrace{\int_0^{\infty} \lambda e^{-\lambda x} dx}} \right] &=& 1 - \ln \lambda \end{array} ")
        elif note == "Fisher information":
            with c21:
                st.write("#### proof of Fisher information")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl}   I_X(\lambda) := \mathbb{E} \left[ \dfrac{d}{d\lambda} \ln f_X(\lambda) \right]^2 &=& \mathbb{E} \left[ \dfrac{d}{d\lambda} \left( -\lambda X + \ln \lambda \right) \right]^2 \\ &=& \mathbb{E} \left( -X + \dfrac{1}{\lambda} \right)^2 \\ &=& \displaystyle \text{Var} X &=& \lambda^{-2} \end{array} ")

def cauchy_all_proofs(note):
    from .distr_illus import cauchy_show
    c1, _, c2 = st.columns([5, 1, 10])
    with c1:
        st.write("#### illustration") 
        muy = st.number_input("Select a value of `muy`", value=0.1, min_value=0.01, max_value=9.99, help="location")
        sig = st.number_input("Select a value of `sigma`", value=0.1, min_value=0.01, max_value=9.99, help="scale / shape")
        cauchy_show(muy, sig)
    with c2:
        st.write("We have some notes in `Cauchy distribution`")
        st.latex(r" \begin{array}{lclllll}   \displaystyle \int \dfrac{dx}{1+x^2} &=& \arctan x & \text{, and} & \displaystyle \int_0^{\infty} \dfrac{e^{tx}}{1+x^2} dx & \to & \infty \\ \\ \displaystyle \lim_{x \to \pm \infty} \arctan x & = & \pm \dfrac{\pi}{2} &,  & \displaystyle \int_0^{\infty} \dfrac{e^{itx}}{1+x^2} dx &=& \dfrac{\pi}{2} e^{-|t|} \end{array} ")
        c21, c22 = st.columns(2)
        if note == "cdf":
            with c21:
                st.write("#### proof of cdf")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write(r"By letting $z =  \frac{t - \mu}{\sigma}$, we have")
                st.latex(r" \begin{array}{ccl} P(X < x) := \displaystyle \int_{-\infty}^x f_X(t) dt &=& \displaystyle \int_{-\infty}^x \dfrac{1}{\sigma \pi \left[ 1 + \left( \frac{t - \mu}{\sigma} \right) ^2 \right]} dt \\ &=& \displaystyle \int_{-\infty}^{(x-\mu)/\sigma} \dfrac{1}{\sigma \pi (1 + z^2)} \cdot\left( \sigma dz \right) \\ &=& \dfrac{1}{\pi} \cdot \left[ \left. \arctan z \Big \vert_{z \to - \infty}^{ z = (x-\mu)/ \sigma} \right. \right] \\ &=& \displaystyle \dfrac{1}{\pi} \left[ \arctan \left( \frac{x-\mu}{\sigma} \right) - \lim_{z \to -\infty} \arctan z \right] \\ &=& \displaystyle \dfrac{1}{\pi} \left[ \arctan \left( \frac{x-\mu}{\sigma} \right) - \left( \dfrac{-\pi}{2} \right) \right] \\ &=& \dfrac{1}{2} + \dfrac{1}{\pi} \arctan \left( \dfrac{x-\mu}{\sigma} \right) \end{array} ")
        elif note == "mode":
            with c21:
                st.write("#### proof of mode")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have known")
                st.latex(r" \begin{array}{ccl} x_{\text{mode}} &=& \underset{x \in \mathbb{R}}{\text{argmax}} \dfrac{1}{\sigma \pi \left[ 1 + \left( \frac{x - \mu}{\sigma} \right)^2 \right]} \qquad \sigma > 0 \\ \\ &=& \underset{x \in \mathbb{R}}{\text{argmin}} \left[ 1 + \left( \frac{x - \mu}{\sigma} \right)^2 \right] &=& \mu \end{array} ")
        elif note == "median":
            with c21:
                st.write("#### proof of median")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have known")
                st.latex(r" \begin{array}{ccl} x_{\text{med}} &=& \Big\lbrace x \in \mathbb{R} : P(X < x_{\text{med}}) = \frac{1}{2} \Big \rbrace \\ &=& \Big\lbrace x \in \mathbb{R} : \frac{1}{2} + \frac{1}{\pi} \arctan \left( \frac{x - \mu}{\sigma} \right) = \frac{1}{2} \Big \rbrace \\ &=& \Big\lbrace x \in \mathbb{R} : \arctan \left( \frac{x - \mu}{\sigma} \right) = 0 \Big \rbrace &=&  \mu \end{array} ")
        elif note == "Expectation":
            with c21:
                st.write("#### proof of expectation")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write(r"By letting $z =  \frac{t - \mu}{\sigma}$, we have")
                st.latex(r" \begin{array}{ccl} \mathbb{E}X := \displaystyle \int_{\mathbb{R}} x f_X(x) dx &=& \displaystyle \int_{-\infty}^{\infty} \dfrac{x}{\sigma \pi \left[ 1 + \left( \frac{x - \mu}{\sigma} \right)^2 \right]} dx \\ \\ &=& \dfrac{1}{\pi} \displaystyle \int_{-\infty}^{\infty} \dfrac{\sigma z+\mu}{1 + z^2} dz \\  \\ &=& \dfrac{\sigma}{\pi} \displaystyle \underset{=\lim_{z\to \infty} \ln(1+z^2)}{\underbrace{\int_{-\infty}^{\infty} \dfrac{z}{1+z^2} dz}} \quad + \quad \dfrac{\mu}{\pi} \underset{=1}{\underbrace{\int_{-\infty}^{\infty} \dfrac{1}{1+z^2} dz}}  &=& \infty \end{array} ")
                st.write("Hence this distribution **does not exist Expectation**")
        elif note == "variance":
            with c21:
                st.write("#### proof of expectation")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write(r"By letting $z =  \frac{t - \mu}{\sigma}$, we have")
                st.latex(r" \begin{array}{rcl} \mathbb{E}X^2 := \displaystyle \int_{\mathbb{R}} x^2 f_X(x) dx &=& \displaystyle \int_{-\infty}^{\infty} \dfrac{x^2}{\sigma \pi \left[ 1 + \left( \frac{x - \mu}{\sigma} \right)^2 \right]} dx \\ \\ &=& \dfrac{1}{\pi} \displaystyle \int_{-\infty}^{\infty} \dfrac{\overset{=\sigma^2z^2 + 2\sigma \mu z+\mu^2}{\overbrace{(\sigma z+\mu)^2}}}{1 + z^2} dz \\ \\  &=& \dfrac{1}{\pi} \displaystyle \int_{-\infty}^{\infty} \left[  \underset{>0}{\underbrace{\dfrac{\sigma^2 z^2}{1+z^2}}} +  \dfrac{2\mu\sigma z}{1+z^2} + \underset{>0}{\underbrace{\dfrac{\mu^2}{1+z^2}}} \right] dz \\ \\ &\geq & \dfrac{2\mu\sigma}{\pi} \displaystyle \underset{=\lim_{z\to \infty} \ln(1+z^2)}{\underbrace{\int_{-\infty}^{\infty} \dfrac{z}{1+z^2} dz}}  &=& \infty \\ \\ \Rightarrow \text{Var} X &=& \mathbb{E}X^2 - \left( \mathbb{E}X \right)^2 &:=&  \text{undefined} \end{array} ")
        elif note == "Skewness":
            with c21:
                st.write("#### proof of Skewness")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write(r"By the same arguments in the computation of `Expectation` and $\mathbb{E}X^2$ in the `Variance`, this term also does not exist")
        elif note == "Kurtosis":
            with c21:
                st.write("#### proof of Kurtosis")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write(r"By the same arguments in the computation of `Expectation` and $\mathbb{E}X^2$ in the `Variance`, this term also does not exist")  
        elif note == "Characteristic func":
            with c21:
                st.write("#### proof of CF")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write(r"Again, letting $z = \frac{x - \mu}{\sigma}$; we obtain")
                st.latex(r" \begin{array}{ccl} \varphi_X(t) := \mathbb{E} e^{itX} &=& \displaystyle \int_{-\infty}^{\infty} \dfrac{e^{itx}}{\sigma \pi \left[ 1 + \left( \frac{x - \mu}{\sigma} \right)^2 \right]} dx \\ \\ &=& \dfrac{1}{\pi} \displaystyle \int_{-\infty}^{\infty} \dfrac{e^{it(\sigma z + \mu)}}{1+z^2} dz \\ &=& e^{it \mu} \cdot \underset{\exp(-\sigma |t| )}{\underbrace{\dfrac{1}{\pi} \displaystyle \int_{-\infty}^{\infty} \dfrac{e^{iz (t\sigma)}}{1+z^2} dz}} &=& \exp\left( -\sigma |t| + it \mu \right) \end{array} ")
                st.write(r"To prove the `last integration`, we will apply `Residual theorem` with 2 simple poles $z = \pm i$")
        elif note == "Moment generating func":
            with c21:
                st.write("#### proof of MGF")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write(r"Again, letting $z = \frac{x - \mu}{\sigma}$; we obtain")
                st.latex(r" \begin{array}{ccl}  M_X(t) := \mathbb{E} e^{tX} &=& \displaystyle \int_{-\infty}^{\infty} \dfrac{e^{tx}}{\sigma \pi \left[ 1 + \left( \frac{x - \mu}{\sigma} \right)^2 \right]} dx \\ \\ &=& \dfrac{1}{\pi} \displaystyle \int_{-\infty}^{\infty} \dfrac{e^{t(\sigma z + \mu)}}{1+z^2} dz \\ &=& e^{t \mu} \cdot \displaystyle \int_{-\infty}^{\infty} \dfrac{1}{\pi} \underset{ \text{Noting that } e^u \geq u }{\underbrace{ \dfrac{e^{\sigma t z}}{1+z^2} }} dz \\ & \geq & e^{t\mu} \displaystyle \int_{-\infty}^{\infty} \dfrac{1}{\pi} \cdot \dfrac{\sigma t z}{1+z^2} dz & \to & +\infty \end{array} ")
        elif note == "Entropy":
            with c21:
                st.write("#### proof of Entropy")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write(r"Again, letting $z = \frac{x - \mu}{\sigma}$; we obtain")
                st.latex(r" \begin{array}{ccl} H_X  := \mathbb{E} \left[ -\ln f_X \right] &=& \displaystyle \int_{-\infty}^{\infty} -\ln \left( \dfrac{1}{\sigma \pi \left[ 1 + \left( \frac{x - \mu}{\sigma} \right)^2 \right]} \right) \cdot \dfrac{1}{\sigma \pi \left[ 1 + \left( \frac{x - \mu}{\sigma} \right)^2 \right]} dx \\ \\ &=& \displaystyle \int_{-\infty}^{\infty} \left[ \ln (\sigma \pi) + \ln \left[ 1 + \left( \frac{x - \mu}{\sigma} \right)^2 \right] \right] \cdot \dfrac{1}{\sigma \pi \left[ 1 + \left( \frac{x - \mu}{\sigma} \right)^2 \right]} dx \\ \\ &=& \displaystyle \int_{-\infty}^{\infty} \left[ \ln (\sigma \pi) + \ln \left( 1 + z^2 \right) \right] \cdot \dfrac{1}{\pi (1+z^2)} dz \\ &=& \ln (\sigma \pi) \quad + \quad \dfrac{1}{\pi} \displaystyle \int_{-\infty}^{\infty} \dfrac{\ln \left( 1 + z^2 \right)}{1+z^2} dz \end{array} ")                
                st.write(r"Now, letting $\theta = \arctan z$, then")
                st.latex(r" \left \lbrace \begin{array}{ccl}  z &=& \tan \theta \\ dz &=& \dfrac{1}{\cos^2 \theta} d\theta \\ \ln(1+z^2) &=& \ln \left( \underset{ \equiv \frac{1}{\cos^2 \theta} }{\underbrace{ 1 + \tan^2 \theta}} \right) &=& -2 \ln \left( \cos \theta \right) \\ \dfrac{1}{1+z^2} \cdot dz &=& \cos^2 \theta \cdot \left( \dfrac{1}{\cos^2 \theta} d\theta \right) &=& d\theta  \end{array} \right. ")
                st.write("and hence")
                st.latex(r"  H_X = \ln (\sigma \pi) + \underset{= \ln 4}{\underbrace{ - \frac{1}{\pi} \int_{-\pi / 2}^{\pi / 2} 2 \ln (\cos \theta) d\theta}} = \ln (\sigma \pi \cdot 4 )")
        elif note == "Fisher information":
            with c21:
                st.write("#### proof of Fisher information")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("Firstly, we have")
                st.latex(r" \begin{array}{ccl} I_X(\sigma) := \mathbb{E} \left[ \dfrac{d}{d\sigma} \ln f_X(\sigma) \right]^2 &=& \mathbb{E} \left[ \dfrac{d}{d\sigma} \left( -\ln \pi - \ln \sigma - \ln \left[ 1 + \left( \frac{X-\mu}{\sigma} \right)^2 \right] \right) \right]^2 \\ \\ &=& \mathbb{E} \left[ \left(  - \dfrac{1}{\sigma} - \dfrac{\dfrac{-2(X-\mu)^2}{\sigma^3}}{ \left[ 1 + \left( \frac{X-\mu}{\sigma} \right)^2 \right]} \right) \right]^2 \end{array} ")
                st.write(r"Next, let $Z = \frac{X - \mu}{\sigma}$")
                st.latex(r" \begin{array}{ccl}  -\dfrac{1}{\sigma} + \dfrac{2(X-\mu)^2}{\sigma^3 \left[ 1+ \left( \frac{X - \mu}{\sigma} \right)^2 \right]} &=& \dfrac{-\sigma^2 \left[ 1+ \left( \frac{X - \mu}{\sigma} \right)^2 \right] + 2(X-\mu)^2}{\sigma^3 \left[ 1+ \left( \frac{X - \mu}{\sigma} \right)^2 \right]} \\ &=& \dfrac{ -\sigma^2 + (X-\mu)^2}{ \sigma^3 \left[ 1 + \left( \frac{X - \mu}{\sigma} \right)^2 \right]} &=& \dfrac{Z^2 - 1}{\sigma(Z^2 + 1)} \end{array} ")
                st.write("Hence")
                st.latex(r" \begin{array}{ccl}   I_X (\sigma) &=& \dfrac{1}{\sigma^2} \displaystyle \int_{-\infty}^{\infty} \left( \dfrac{1 - z^2}{1+z^2} \right)^2 \cdot \dfrac{1}{\pi (1 + z^2)} dz &=& \dfrac{1}{\sigma^2}  \displaystyle \int_{-\infty}^{\infty} \dfrac{z^4 - 2z^2 + 1}{\pi (1+z^2)^3} dz \end{array} ")
                st.write(r"Again, implement the same techniques like in `Entropy` with $\theta = \arctan z$ and the `power reduction formula`, we obtain")
                st.latex(r" \begin{array}{l}  I_1 &:=& \displaystyle \int_{-\infty}^{\infty} \dfrac{1}{(1+z^2)^3} dz &=& \displaystyle \int_{-\pi/2}^{\pi /2} \cos^4 \theta d\theta &=& \dfrac{3\pi}{8} \\ I_2 &:=& \displaystyle \int_{-\infty}^{\infty} \dfrac{z^2}{(1+z^2)^3} dz &=& \displaystyle \int_{-\pi/2}^{\pi /2} \sin^2 \theta \cos^2 \theta d\theta &=& \dfrac{\pi}{8} \\ I_3 &:=& \displaystyle \int_{-\infty}^{\infty} \dfrac{z^4}{(1+z^2)^3} dz &=& \displaystyle \int_{-\pi/2}^{\pi /2} \sin^4 \theta d\theta &=& \dfrac{3\pi}{8} \\ \end{array} ")
                st.write("Therefore")
                st.latex(r" I_X(\sigma) \quad = \quad \dfrac{1}{\sigma^2} \cdot \dfrac{1}{\pi} \cdot \underset{\frac{4\pi}{8}}{\underbrace{\left( I_1 - 2 I_2 + I_3 \right)}} \quad = \quad \dfrac{1}{2\sigma^{2}} ")                

def student_all_proofs(note):
    from .distr_illus import student_show
    c1, _, c2 = st.columns([5, 1, 10])
    with c1:
        st.write("#### illustration")
        deg = st.number_input("Select a value of `deg`", value=2, min_value=2, max_value=20, help="degrees of freedom")
        student_show(deg)
    with c2:
        st.write("We have some notes in `Student distribution`")
        a21, a22 = st.columns(2)
        with a21:
            st.write("`Gamma function`")
            st.latex(r"\Gamma(z) = \int_0^{\infty} t^{z-1} e^{-t} dt")
        with a22:
            st.write(" Well known properties ")
            st.latex(r" \begin{array}{ccl} \Gamma(1) &=& 1 \\ \Gamma \left( \frac{1}{2} \right) &=& \sqrt{\pi} \\ \Gamma(z + 1) &=& z \Gamma(z) \end{array} ")
        st.write("and some must known other functions")
        b1, b2 = st.columns(2)
        with b1:
            st.write("`Digamma function`")
            st.latex(r"\psi(z) = \dfrac{d}{dz} \ln \Gamma(z)")
            st.write(" `Beta function` ")
            st.latex(r" \begin{array}{ccl} B(z_1, z_2) &=& \displaystyle \int_0^1 t^{z_1 - 1} (1 - t)^{z_2 - 1} dt \\ &=& \dfrac{\Gamma(z_1) \Gamma(z_2)}{\Gamma(z_1 + z_2)} \end{array}")
        with b2:
            st.write(" `2nd kind of Bessel function`")
            st.latex(r" K_{\alpha} (x) = \left\lbrace \begin{array}{lcl} \frac{\pi}{2} i^{\alpha + 1} H_{\alpha}^{(1)} (ix) & & \arg x \in \left( -\pi , \frac{\pi}{2} \right] \\ \frac{\pi}{2}(-i)^{\alpha + 1}H_{\alpha}^{(2)}(-ix) & & \arg x \in \left( \frac{\pi}{2}, \pi \right] \end{array} \right. ")
            st.write(r"where $H_{\alpha}$ is `Hankel function`")
            st.latex(r" \begin{array}{ccl} H_{\alpha}^{(1)}(x) &=& \displaystyle \dfrac{1}{\pi i} \int_{-\infty}^{i \pi + \infty} e^{x \sinh t - \alpha t} dt \\ H_{\alpha}^{(2)}(x) &=& \displaystyle \dfrac{-1}{\pi i} \int_{-\infty}^{-i \pi + \infty} e^{x \sinh t - \alpha t} dt \end{array} ")            
        c21, c22 = st.columns(2)
        if note == "cdf":
            with c21:
                st.write("#### proof of cdf")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("Firstly, we have")
                st.latex(r" \begin{array}{ccl} P(X < x) := \displaystyle \int_{-\infty}^x f_X(t) dt &=& \displaystyle \int_{-\infty}^x \dfrac{ \Gamma\left( \frac{d+1}{2} \right) }{ \sqrt{\pi d} \cdot \Gamma\left( \frac{d}{2} \right) } \cdot \left( 1 + \frac{t^2}{d} \right)^{ - \frac{d+1}{2} } dt \\ &=& \dfrac{ \Gamma\left( \frac{d+1}{2} \right) }{ \sqrt{\pi d} \Gamma\left( \frac{d}{2} \right) } \cdot \displaystyle \int_{-\infty}^x \left( 1 + \frac{t^2}{d} \right)^{ - \frac{d+1}{2} } dt \end{array} ")
                st.write("Next, using `incomplete Beta function` and `Hypergeometric function`,")
                st.latex(r" \begin{array}{ccl}  \displaystyle \int_{-\infty}^x \left( 1 + \frac{t^2}{d} \right)^{ - \frac{d+1}{2} } dt &:=& \displaystyle \underbrace{\int_0^x \left( 1 + \frac{t^2}{d} \right)^{ - \frac{d+1}{2} } dt} + \displaystyle \int_{-\infty}^0 \left( 1 + \frac{t^2}{d} \right)^{ - \frac{d+1}{2} } dt \\ &=& x \cdot {}_{2}F_{1} \left( {\frac {1}{2}},{\frac { d + 1 }{2}}; \frac{3}{2}; \frac{-x^2}{d} \right) \quad + \quad \dfrac{1}{2} \dfrac{ \sqrt{\pi d} \Gamma\left( \frac{d}{2} \right) }{ \Gamma\left( \frac{d+1}{2} \right) } \end{array} ")
                st.write("Therefore")
                st.latex(r" P(X < x) = \dfrac{1}{2} + \dfrac{ x \Gamma\left( \frac{d+1}{2} \right) }{ \sqrt{\pi d} \Gamma\left( \frac{d}{2} \right) } \cdot {}_{2}F_{1} \left( {\frac {1}{2}},{\frac { d + 1 }{2}}; \frac{3}{2}; \frac{-x^2}{d} \right) ")
        elif note == "mode":
            with c21:
                st.write("#### proof of mode")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} x_{\text{mode}} &=& \displaystyle \underset{x \in \mathbb{R}}{\text{argmax}} \left[ \underset{\text{constant}} {\underbrace{ \left( \dfrac{\Gamma(\frac{d+1}{2})}{\sqrt{d \pi} \Gamma(\frac{d}{2})}\right)}} \left( 1 + \frac{x^2}{d} \right)^{- \frac{d+1}{2}} \right] \\ &=& \displaystyle \underset{x \in \mathbb{R}}{\text{argmax}} \left( 1 + \frac{x^2}{d} \right)^{- \frac{d+1}{2}} &=& 0 \end{array} ")
        elif note == "median":
            with c21:
                st.write("#### proof of median")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} x_{\text{med}} &=& \Big\lbrace x_m \in \mathbb{R} \Big \vert P(X < x_{m}) = 50 \% \Big \rbrace \\ &=& \Big\lbrace x_m \in \mathbb{R} \Big \vert \frac{1}{2} + \frac{ x \Gamma\left( \frac{d+1}{2} \right) }{ \sqrt{\pi d} \Gamma\left( \frac{d}{2} \right) } \cdot {}_{2}F_{1} \left( {\frac {1}{2}},{\frac { d + 1 }{2}}; \frac{3}{2}; \frac{-x^2}{d} \right) = \frac{1}{2} \Big \rbrace \\ &=& \Big\lbrace x_m \in \mathbb{R} \Big \vert \frac{ x \Gamma\left( \frac{d+1}{2} \right) }{ \sqrt{\pi d} \Gamma\left( \frac{d}{2} \right) } \cdot {}_{2}F_{1} \left( {\frac {1}{2}},{\frac { d + 1 }{2}}; \frac{3}{2}; \frac{-x^2}{d} \right) = 0 \Big \rbrace &=& 0 \end{array} ")
        elif note == "Expectation":
            with c21:
                st.write("#### proof of Expectation")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("For all $d > 1$ and by the symmetric of any odd-function, we have")
                st.latex(r" \int_{\mathbb{R}} x \cdot \left( 1 + \dfrac{x^2}{d} \right)^{ - \frac{1+d}{2}} = 0 ")
                st.write("Otherwise, this integral will be not exists, hence")
                st.latex(r" \mathbb{E} X = \dfrac{ \Gamma\left( \frac{d+1}{2} \right) }{ \sqrt{\pi d} \Gamma\left( \frac{d}{2} \right) } \cdot \int_{\mathbb{R}} x \cdot \left( 1 + \dfrac{x^2}{d} \right)^{ - \frac{1+d}{2}} = 0 , \qquad \forall d > 1")
        elif note == "variance":
            with c21:
                st.write("#### proof of variance")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("Generally, we have")
                st.latex(r" \begin{array}{ccl} \mathbb{E} X^k &=& \left \lbrace \begin{array}{lcl} \qquad 0 & & \text{if } k \in \Big\lbrace 0 < k < d \Big \vert k \text{ is odd} \Big\rbrace \\ \frac{1}{\sqrt{\pi} \Gamma\left(\frac{d}{2}\right)} \left[ \Gamma\left(\frac{k+1}{2}\right) \Gamma\left(\frac{d-k}{2}\right) d^{\frac{k}{2}} \right] & & \text{if } k \in \Big\lbrace 0 < k < d \Big \vert k \text{ is even} \Big\rbrace \end{array} \right. \\ \Gamma(\frac{3}{2}) &=& \left( \dfrac{3}{2} - 1 \right) \Gamma( \frac{3}{2} - 1 ) \quad = \quad \dfrac{\sqrt{\pi}}{2} \\ \Gamma\left( \frac{d}{2} \right) &=& \left( \frac{d}{2} - 1 \right)\Gamma\left( \frac{d-2}{2} \right) \qquad \Leftrightarrow \qquad \dfrac{\Gamma\left( \frac{d-2}{2} \right)}{\Gamma \left( \frac{d}{2} \right)} \quad = \quad \left \lbrace \begin{array}{lcl} \frac{2}{d-2} & & d > 2 \\ \infty & & d \in (1, 2] \end{array} \right. \end{array} ")
                st.write("So for $k = 2$, then")
                st.latex(r" \text{Var} X = \mathbb{E} X^2 = \left \lbrace \begin{array}{lcl} \frac{d}{d - 2} & & d > 2 \\ \infty & & d \in (1, 2] \end{array} \right. ")
                st.write("------------")
                st.write(" To prove this generalized equation, we have a note that")
                st.latex(r" \int_{\mathbb{R}} x^k \cdot \left( 1 + \frac{x^2}{d} \right)^{- \frac{d+1}{2} } dx = \left \lbrace \begin{array}{lcl} \qquad 0 & & k \text{ is odd }, d > 1 \\ \displaystyle 2\int_0^{\infty} x^k \left( 1 + \frac{x^2}{d} \right)^{- \frac{d+1}{2} } dx & & k \text{ is even}, d > 1 \end{array} \right. ")
                st.write(r"and for $k$ is even, using substitution $u = \frac{x^2}{d}$, then")
                st.latex(r" \begin{array}{ccl} \displaystyle \int_0^{\infty} x^k \left( 1 + \frac{x^2}{d} \right)^{- \frac{d+1}{2} } dx &=& \displaystyle  \int_0^{\infty} \left( \sqrt{u \cdot d} \right)^k \left( 1 + u \right)^{- \frac{d+1}{2} } \cdot \left( \frac{\sqrt{d}}{2\sqrt{u}} \cdot du \right) \\ &=&  \dfrac{d^{ \frac{1 +k}{2}}}{2} \cdot \underset{\text{using Beta function}}{\displaystyle \underbrace{\int_0^{\infty} u^{\frac{k-1}{2}} (1+ u)^{-\frac{d+1}{2}} du}} \\ &=& \dfrac{d^{\frac{1 + k}{2}}}{2} \quad \cdot \quad \dfrac{\Gamma\left( \frac{k+1}{2} \right) \cdot \Gamma\left( \frac{d+1}{2} - \frac{k+1}{2} \right)}{\Gamma( \frac{d+1}{2} )} \end{array} ")
                st.write("We obtain (for all $k$ even)")
                st.latex(r" \begin{array}{ccl}  \mathbb{E} X^k &=& \left( \frac{\Gamma \left( \frac{d+1}{2} \right)}{\sqrt{d \pi} \cdot \Gamma \left( \frac{d}{2} \right)} \right) \cdot 2\left[ \dfrac{d^{\frac{k+1}{2}}}{2} \cdot \dfrac{\Gamma\left( \frac{k+1}{2} \right) \cdot \Gamma\left( \frac{d+1}{2} - \frac{k+1}{2} \right)}{\Gamma( \frac{d+1}{2} )}  \right] \\ &=& \dfrac{d^{k/2}}{\sqrt{\pi} \cdot \Gamma(\frac{d}{2})} \cdot \Gamma \left( \frac{k+1}{2} \right) \cdot \Gamma \left( \frac{d-k}{2} \right) \end{array} ")
        elif note == "Skewness":
            with c21:
                st.write("#### proof of Skewness")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("You can back to the results in the `variance` part to refer, we have")
                st.latex(r" \begin{array}{rcl} \mathbb{E} X^3 &=& 0 \\ \\ \Rightarrow \mathbb{E} \left( \frac{X - \mathbb{E}X}{\sqrt{\text{Var}X}} \right)^3 &=& \mathbb{E} \left( \frac{X - 0}{\sqrt{ \frac{d}{d-2} }} \right)^3 &=& 0 \qquad \forall d > 3 \end{array}  ")
        elif note == "Kurtosis":
            with c21:
                st.write("#### proof of Kurtosis")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("You can back to the results in the `variance` part to refer, we have")
                st.latex(r" \begin{array}{rcl}  \mathbb{E} X^4 &=& \dfrac{3d^2}{(d-2)(d-4)} & & \forall d > 4 \\ \\  \Rightarrow \mathbb{E} \left( \frac{X - \mathbb{E}X}{\sqrt{\text{Var}X}} \right)^4 &=& \frac{\mathbb{E}X^4}{\left( \sqrt{ \frac{d}{d-2} } \right)^4} &=& \frac{3(d-2)}{d-4} \end{array} ")
        elif note == "Characteristic func":
            with c21:
                st.write("#### proof of CF")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write(r"We have $e^{itx} = \cos tx + i \sin tx$, therefore")
                st.latex(r" \begin{array}{ccl} \varphi_X(t) &:=& \mathbb{E}e^{itX} &=& \displaystyle \int_{\mathbb{R}} \cos tx \cdot f_X(x) dx &=& \displaystyle 2 \int_0^{\infty} \cos tx \cdot f_X(x) dx \end{array} ")
                st.write("By differentiating under the integral sign and using integration by parts, it is shown that the characteristic function satisfies a second-order linear differential equation with respect to $t$,")
                st.latex(r" (d \cdot z^2 + d^2)\, \varphi_X''(z) + (d + 1)\, t \varphi_X'(z) + \frac{d + 1}{4} \varphi_X(z) = 0 ")
                st.write(r"The general solution involves modified Bessel functions $K_{\alpha}$")
                st.latex(r" \varphi_X(t) = C\, |t|^{d/2} K_{d/2}(\sqrt{d} |t|) ")
                st.write(r" with constant determined by the condition $ \varphi_X(0) = 1.$ Hence")
                st.latex(r" \varphi_X(t) = \frac{2^{1 - d/2}}{\Gamma\left( \frac{d}{2} \right)} \left( \sqrt{d} |t| \right)^{d/2} K_{d/2} \left( \sqrt{d} |t| \right) ")
        elif note == "Moment generating func":
            with c21:
                st.write("#### proof of MGF")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write(r"For all $d > 0$ and for all $x \in \mathbb{R}$, we have")
                st.latex(r" \begin{array}{ccl} e^{tx} \cdot \left( 1 + \frac{x^2}{d} \right)^{- \frac{d+1}{2}} \to \infty \qquad \forall t > 0 \quad \forall x >\in (x_0, \infty) \quad \text{ where } x_0 > 0 \\ e^{tx} \cdot \left( 1 + \frac{x^2}{d} \right)^{- \frac{d+1}{2}} \to \infty \qquad \forall t < 0 \quad \forall x \in (-\infty, x_0) \quad \text{ where } x_0 < 0 \end{array} ")                
                st.write("which implies")
                st.latex(r" \int_{\mathbb{R}} \underset{ > 0}{\underbrace{e^{tx} \left( 1 + \frac{x^2}{d} \right)^{- \frac{d+1}{2}}}} dx \quad \geq \quad \left \lbrace  \begin{array}{ccl} \displaystyle \underset{ > 0}{\underbrace{\int_{(- \infty, x_0)}}} + \underset{\to \infty}{\underbrace{\int_{(x_0, \infty)} ... dx}} \to \infty & & \text{ if } t > 0 \\ \displaystyle \underset{ \to \infty }{\underbrace{\int_{(- \infty, x_0)}}} + \underset{> 0}{\underbrace{\int_{(x_0, \infty)} ... dx}} \to \infty & & \text{ if } t < 0 \\ \end{array} \right. ")
                st.write("Therefore")
                st.latex(r" \begin{array}{ccl} M_X(t) &=& \displaystyle \int_{\mathbb{R}} e^{tx} \cdot \left[ \dfrac{ \Gamma\left( \frac{d+1}{2} \right) }{ \sqrt{\pi d} \cdot \Gamma\left( \frac{d}{2} \right) } \cdot \left( 1 + \frac{x^2}{d} \right)^{ - \frac{d+1}{2} } \right] dx \\ &=& \dfrac{ \Gamma\left( \frac{d+1}{2} \right) }{ \sqrt{\pi d} \cdot \Gamma\left( \frac{d}{2} \right) } \displaystyle \cdot \int_{\mathbb{R}} e^{tx} \cdot \left( 1 + \frac{x^2}{d} \right)^{ - \frac{d+1}{2} } dx & \to & \infty \end{array} ")

def chisq_all_proofs(note):
    from .distr_illus import chisq_show
    c1, _, c2 = st.columns([5, 1, 10])
    with c1:
        st.write("#### illustration")
        deg = st.number_input("Select a value of `deg`", value=2, min_value=2, max_value=20, help="degrees of freedom")
        chisq_show(deg)
    with c2:
        st.write("We have some notes in `Chi-square distribution` (refer `Gamma` and `digamma function` in the `Student distr`)")
        st.write("`Incomplete Gamma function`")
        st.latex(r" \begin{array}{ccl} \gamma (s, x) &:=& \displaystyle  \int_0^x t^{s-1} e^{-t} dt \\ \gamma (s+1, x) &=& s \cdot \gamma(s, x) + x^s e^{-x} \\ \gamma (s, x) + \Gamma (s, x) &=& \Gamma(s) \quad = \quad \displaystyle \lim_{x\to \infty} \gamma(s, x) \end{array} ")
        c21, c22 = st.columns(2)
        if note == "cdf":
            with c21:
                st.write("#### proof of cdf")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} P(X < x) &=& \dfrac{1}{2^{d/2} \Gamma(d/2)} \displaystyle \int_{0}^x t^{(d/2) - 1} \cdot e^{-t/2}  dt \\  &=& \dfrac{1}{2^{d/2} \Gamma(d/2)} \cdot \displaystyle \int_{0}^{x / 2} (2u)^{(d/2) - 1} e^{-u} \cdot (2du) \\ &=& \quad \dfrac{1}{ \Gamma(d/2)} \cdot \displaystyle \underbrace{\int_{0}^{x / 2} u^{ (d/2) - 1} e^{-u} du} \\ &=& \quad \dfrac{1}{\Gamma(d/2)} \quad \cdot \quad \gamma \left( \frac{d}{2}, \frac{x}{2} \right) \end{array} ")
        elif note == "mode":
            with c21:
                st.write("#### proof of mode")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} x_{\text{mode}} &=& \underset{x \geq 0}{\text{argmax}} \left[ \dfrac{1}{2^{d/2} \Gamma(d/2)} x^{(d/2) - 1} e^{-x/2} \right] &=& \underset{x \geq 0}{\text{argmax}} \left[ x^{(d/2) - 1} e^{-x/2} \right] &=& \max \lbrace 0, d-2 \rbrace \end{array} ")
                st.write(r"Indeed, the function $ g(x) = x^{(d/2) - 1} e^{-x/2} $ attains maximum iff")
                st.latex(r" \begin{array}{ccl} \left\lbrace \begin{array}{ccl} g'(x) &=& 0 \\ g''(x) & > & 0 \end{array} \right. & \Rightarrow & \left\lbrace \begin{array}{ccl}  x^{\frac{d}{2} - 2} e^{-\frac{x}{2}} \overset{=\quad -\frac{1}{2}(x-(d-2))}{\overbrace{\left( \frac{d}{2} - 1 - \frac{x}{2} \right)}} &=& 0 \\ x^{\frac{d}{2} - 3} e^{-\frac{x}{2}} \left[ \left( \frac{d-x-2}{2} \right) \left( \frac{d-x-4}{2} \right) - \frac{x}{2} \right] &>& 0 \end{array} \right. \\ & \Rightarrow & \left\lbrace \begin{array}{lcl}  \qquad x & \in & \lbrace 0, d-2 \rbrace \\ x^{\frac{d}{2} - 3} e^{-\frac{x}{2}} \left[ \frac{x^2}{4} - \frac{d-1}{2} x + \left( \frac{d^2}{4} - \frac{3d}{2} + 2 \right) \right] &>& 0 \end{array} \right. \\ & \Rightarrow & x \quad = \quad \max \lbrace 0, d-2 \rbrace \end{array} ")
        elif note == "median":
            with c21:
                st.write("#### proof of median")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} x_{\text{med}} &=& \Big \lbrace x : P(X < x) = 50 \% \Big \rbrace \\ &=& \Big \lbrace x : \dfrac{\gamma \left( \frac{d}{2}, \frac{x}{2} \right)}{\Gamma \left( d/ 2 \right)} = \dfrac{1}{2} \Big \rbrace & \approx & d \left( 1 - \frac{2}{9d} \right)^3 \end{array} ")
                st.write(r"Indeed, denote $Q(x) =  \dfrac{\gamma \left( \frac{d}{2}, \frac{x}{2} \right)}{\Gamma \left( d/ 2 \right)} $, then there exists some $\delta > 0$ such that")
                st.latex(r" Q(d - \delta) \approx \Phi \left( - \frac{\delta}{\sqrt{2d}} \right) + o(\delta) ")
                st.write(r"where $\Phi$ is the `cdf of Normal dist` $\mathcal{N}(0, 1)$")
        elif note == "Expectation":
            with c21:
                st.write("#### proof of Expectation")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("Generally, for all `non-central moment` order $k$, we have")
                st.latex(r" \mathbb{E}X^k \quad = \quad d(d + 2)(d+4)\cdots(d+2k-2) \quad = \quad 2^k \dfrac{\Gamma(k + \frac{d}{2})}{\Gamma(\frac{d}{2})} ")
                st.write("For $k = 1$, we deduce the expectation")
                st.latex(r" \begin{array}{l} \mathbb{E}X &=& 2 \dfrac{\Gamma(1 + \frac{d}{2})}{\Gamma(\frac{d}{2})} &=& 2 \cdot \dfrac{d}{2} &=& d \end{array} ")
                st.write("----------")
                st.write("To prove the generalized statement, we have")
                st.latex(r" \mathbb{E}X^k = \int_0^{\infty} x^k \cdot \left(\dfrac{1}{2^{d/2} \Gamma(d/2)} x^{d/2 - 1} e^{-x/2} \right) dx \quad = \quad \dfrac{1}{2^{d/2} \Gamma(d/2)}\int_0^{\infty} x^{k+\frac{d}{2}-1} e^{-x/2} dx ")
                st.write("and")
                st.latex(r" \begin{array}{ccl} \displaystyle \int_0^{\infty} x^{k+\frac{d}{2}-1} e^{-x/2} dx &=& \displaystyle \int_0^{\infty} (2z)^{k+\frac{d}{2}-1} e^{-z} \cdot (2 dz) \qquad \text{ by letting } z = \frac{x}{2} \\ &=& 2^{k + \frac{d}{2}} \displaystyle \underbrace{\int_0^{\infty} z^{(k + \frac{d}{2}) - 1} e^{-z} dz} \\ &=& 2^{k + \frac{d}{2}} \quad \cdot \quad \Gamma (k + \frac{d}{2}) \end{array} ")
                st.write("Combine all together, we obtain the stament")
        elif note == "variance":
            with c21:
                st.write("#### proof of variance")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("Refer the general result for `non-central moment` stated in `Expectation`, we have")
                st.latex(r" \begin{array}{ccl} \text{Var} X := \mathbb{E}X^2 - \left( \mathbb{E}X \right)^2 &=&\underbrace{ \left[ 2^2 \cdot \dfrac{\Gamma\left( 2+\frac{d}{2} \right)}{\Gamma(\frac{d}{2})} \right]} - d^2 \\ &=& \left[ 4 \cdot \underset{=\frac{d+2}{2}}{\underbrace{\left( 1 + \frac{d}{2} \right)}} \cdot \left( \frac{d}{2} \right) \right] - d^2 &=& 2d \end{array} ") 
        elif note == "Skewness":
            with c21:
                st.write("#### proof of Skewness")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("Refer the general result for `non-central moment` stated in `Expectation`, we have")
                st.latex(r" \begin{array}{ccl} \mathbb{E} X^3 &=& 2^3 \cdot \dfrac{\Gamma(3 + \frac{d}{2})}{\Gamma(\frac{d}{2})} &=& 2^3 \cdot \dfrac{d+4}{2} \cdot \dfrac{d+2}{2} \cdot \dfrac{d}{2} &=& d(d+2)(d+4) \end{array} ")
                st.write("Apply the result found from the `Expectation` and `variance` while finding the `first 2 noncentral-moment`. Then the skewness defined by")
                st.latex(r" \begin{array}{ccl} \mathbb{E} \left( \frac{X - \mathbb{E}X}{\sqrt{\text{Var}X}} \right)^3 &=& \dfrac{\mathbb{E}X^3 - 3\mu \mathbb{E}X^2 +2\mu^3}{\sigma^3} \qquad \text{where} \quad \mu = \mathbb{E}X=d \text{, } \sigma = \sqrt{\text{Var}X} = \sqrt{2d} \\ &=& \dfrac{d(d+2)(d+4) - 3d\cdot \left[ d(d+2) \right] + 2 d^3}{ 2d\sqrt{2d} } \\ &=& \dfrac{(d+2)(d+4) - 3d(d+2) + 2d^2}{2\sqrt{2d}} \\ &=& \dfrac{(d^2+6d+8) - 3(d^2+2d) + 2d^2}{2\sqrt{2d}} \\ &=& \dfrac{8}{2\sqrt{2d}} \qquad = \qquad \sqrt{\dfrac{8}{d}} \end{array} ")
        elif note == "Kurtosis":
            with c21:
                st.write("#### proof of Kurtosis")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("Refer the general result for `non-central moment` stated in `Expectation`, we have")
                st.latex(r" \begin{array}{ccl} \mathbb{E} X^4 &=& 2^4 \cdot \dfrac{\Gamma(4 + \frac{d}{2})}{\Gamma(\frac{d}{2})}  &=& d(d+2)(d+4)(d+6) \end{array} ")
                st.write("Apply the result found from the `Expectation`, `variance` and `Skewness` while finding the `first 3 noncentral-moment`. Then the skewness defined by")
                st.latex(r" \begin{array}{ccl}  \mathbb{E} \left( \frac{X - \mathbb{E}X}{\sqrt{\text{Var}X}} \right)^4 &=& \dfrac{\mathbb{E}X^4 - 4\mu \mathbb{E}X^3 + 6\mu^2 \mathbb{E}X^2 - 3\mu^4}{\sigma^4} \qquad \quad \mu = d \text{, } \sigma = \sqrt{2d} \\  &=& \dfrac{d(d+2)(d+4)(d+6) - 4d^2(d+2)(d+4) + 6d^3(d+2) - 3d^4}{(2d)^2} \\ &=& \dfrac{(d^3 + 12d^2 + 44d + 48) - 4(d^3 + 6d^2+8d)+6(d^3+2d^2)-3d^3}{4d} &=& \dfrac{12}{d} \end{array} ")
        elif note == "Characteristic func":
            with c21:
                st.write("#### proof of CF")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} \varphi_X(t) := \mathbb{E}e^{itX} &=& \displaystyle \dfrac{1}{2^{d/2}\Gamma(\frac{d}{2})} \int_0^{\infty} e^{itx} \cdot \left( x^{\frac{d}{2}-1} e^{-\frac{x}{2}} \right) dx \\ &=& \dfrac{1}{2^{d/2}\Gamma(\frac{d}{2})} \displaystyle \int_0^{\infty} x^{\frac{d}{2}-1} \cdot e^{- \frac{x}{2} \left( 1 - 2it \right) } dx \qquad \qquad \qquad \text{ let } z=\frac{x(1-2it)}{2} \\ &=& \dfrac{1}{2^{d/2}\Gamma(\frac{d}{2})} \displaystyle \int_0^{\infty} \left( \frac{2z}{\left( 1-2it \right)} \right)^{\frac{d}{2}-1} \cdot e^{- z } \cdot \left( \frac{1-2it}{2} dz \right) \\ &=& \dfrac{1}{\Gamma( \frac{d}{2} )} \cdot \left( \dfrac{1}{1-2it} \right)^{\frac{d}{2}} \cdot \displaystyle \underbrace{\int_0^{\infty} z^{\frac{d}{2} - 1} e^{-z} dz} \\ &=& \quad \dfrac{1}{\Gamma( \frac{d}{2} )} \cdot \left( 1 - 2it \right)^{- \frac{d}{2}} \quad \cdot \quad \Gamma \left( \frac{d}{2} \right) \\ &=& \left( 1 - 2it \right)^{- \frac{d}{2}} \end{array} ")                    
        elif note == "Moment generating func":
            with c21:
                st.write("#### proof of MGF")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} M_X(t) := \mathbb{E}e^{tX} &=& \displaystyle \dfrac{1}{2^{d/2}\Gamma(\frac{d}{2})} \int_0^{\infty} e^{tx} \cdot \left( x^{\frac{d}{2}-1} e^{-\frac{x}{2}} \right) dx \\ &=& \dfrac{1}{2^{d/2}\Gamma(\frac{d}{2})} \displaystyle \int_0^{\infty} x^{\frac{d}{2}-1} \cdot e^{- \frac{x}{2} \left( 1 - 2t \right) } dx \qquad \qquad \qquad \text{ let } z=\frac{x(1-2t)}{2} \\ &=& \dfrac{1}{2^{d/2}\Gamma(\frac{d}{2})} \displaystyle \int_0^{\infty} \left( \frac{2z}{\left( 1-2t \right)} \right)^{\frac{d}{2}-1} \cdot e^{- z } \cdot \left( \frac{1-2t}{2} dz \right) \\ &=& \dfrac{1}{\Gamma( \frac{d}{2} )} \cdot \left( \dfrac{1}{1-2t} \right)^{\frac{d}{2}} \cdot \displaystyle \underbrace{\int_0^{\infty} z^{\frac{d}{2} - 1} e^{-z} dz} \\ &=& \quad \dfrac{1}{\Gamma( \frac{d}{2} )} \cdot \left( 1 - 2t \right)^{- \frac{d}{2}} \quad \cdot \quad \Gamma \left( \frac{d}{2} \right) \\ &=& \left( 1 - 2t \right)^{- \frac{d}{2}} \end{array} ")
        elif note == "Entropy":
            with c21:
                st.write("#### proof of Entropy")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl}  H_X(d)  &=&\mathbb{E}\left[ - \ln \left( \dfrac{1}{2^{d/2}\Gamma(\frac{d}{2})} x^{\frac{d}{2}-1} e^{-\frac{x}{2}} \right)  \right] \\ \\ &=& \mathbb{E} \left[- \left( \frac{d}{2}-1 \right) \ln x + \frac{x}{2} + \frac{d}{2} \ln 2 + \ln \left[ \Gamma\left( \frac{d}{2} \right)  \right] \right] \\ \\ &=& \underbrace{\dfrac{\mathbb{E}X}{2}} + \underbrace{\dfrac{d}{2} \ln 2 + \ln \left[ \Gamma\left( \frac{d}{2} \right)  \right]} - \left( \frac{d}{2}-1 \right) \underbrace{\mathbb{E} \left( \ln X \right)} \\ &=& \dfrac{d}{2} \quad + \quad \ln \left[ 2 \Gamma\left( \frac{d}{2} \right)  \right] \quad - \quad \left( \frac{d}{2}-1 \right) \cdot \psi(\frac{d}{2}) \end{array} ")
                st.write(r"where $\psi$ is the `Digamma function` we have introduced in the `Student distribution`")
                st.latex(r" \begin{array}{rccl} & \psi\left( z \right) &=& \displaystyle \dfrac{d}{dz} \ln \Gamma(z) \quad = \quad \dfrac{d}{dz} \left( \int_0^{\infty} t^{z-1} e^{-t} dt \right) \qquad \text{for } z=\frac{d}{2} \text{ and } x = 2t\\ \Rightarrow & \psi( \frac{d}{2} ) &=& \displaystyle \underset{\mathbb{E} \ln X}{\underbrace{\dfrac{1}{2^{d/2} \Gamma(d/2)} \int_0^{\infty} \ln x  \cdot \left( x^{\frac{d}{2}-1} e^{-\frac{x}{2}} \right) dx}} \end{array} ")

def fisher_all_proofs(note):
    from .distr_illus import fisher_show
    c1, _, c2 = st.columns([5, 1, 10])
    with c1:
        st.write("#### illustration")
        deg_num = st.number_input("Select a value of `d1`", value=2, min_value=2, max_value=20, help="degrees of freedom on numerator")
        deg_dem = st.number_input("Select a value of `d2`", value=3, min_value=3, max_value=20, help="degrees of freedom on denominator")
        fisher_show(deg_num, deg_dem)
    with c2:
        st.write("In this disribution, beside the `Gamma` and `Beta function` which introduced in the `Student distr`, we must know `regularized incomplete beta function`,")
        st.latex(r" \begin{array}{l} I_x(a, b) \quad = \quad \dfrac{B(x, a, b)}{B(a, b)} \quad = \quad \dfrac{\displaystyle \int_0^x t^{a-1} (1-t)^{b-1}dt}{\displaystyle \int_0^{1} t^{a-1} (1-t)^{b-1}dt} , \text{ and }\\ B(a, b) \quad = \quad \dfrac{\Gamma(a) \cdot \Gamma(b)}{\Gamma(a+b)} \end{array} ") 
        c21, c22 = st.columns(2)
        if note == "cdf":
            with c21:
                st.write("#### proof of cdf")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} F_X(x) := P(X < x) &=& \displaystyle \dfrac{1}{B\left( \frac{d_1}{2}, \frac{d_2}{2} \right)}  \int_0^{x} t^{-1} \cdot \sqrt{\frac{(d_1 t)^{d_1} d_2^{d_2}}{(d_1 t + d_2)^{d_1 + d_2}}} dt \\ \\ &=& \dfrac{1}{B\left( \frac{d_1}{2}, \frac{d_2}{2} \right)} \cdot \left( \dfrac{d_1}{d_2} \right)^{ \frac{d_1}{2} } \displaystyle \int_0^x t^{\frac{d_1}{2} - 1} \left( 1 + \frac{d_1}{d_2} t \right)^{ - \frac{d_1 + d_2}{2} } dt  \end{array} ")
                st.write(r"Now, let $z = \dfrac{d_1 t}{d_1 t + d_2}$, we have")
                st.latex(r" \left \lbrace \begin{array}{ccl} z &=& 1 - \dfrac{1}{d_2 \cdot \left( \frac{d_1}{d_2} t + 1 \right)} \\ t &=& \dfrac{d_2}{d_1} \cdot \dfrac{z}{1-z}   \end{array} \right. \quad \Rightarrow \quad \left \lbrace \begin{array}{ccl}  \left( \frac{d_1}{d_2} t + 1 \right) &=& \dfrac{1}{1-z} \\ \\ \dfrac{dz}{dt} &=& \dfrac{d_1 d_2}{(d_1 t + d_2)^2} &=& \dfrac{d_1}{d_2} \cdot (1-z)^2  \end{array} \right. ")
                st.write("and then")
                st.latex(r" \begin{array}{ccl} \displaystyle \int_0^x t^{\frac{d_1}{2}-1} \left( 1 + \frac{d_1}{d_2} t \right)^{-\frac{d_1 + d_2}{2}} dt &=& \displaystyle \int_0^{ \frac{d_1 x}{d_1x + d_2} } \left( \frac{d_2}{d_1} \cdot \frac{z}{1-z} \right)^{\frac{d_1}{2}-1} \cdot \underset{=(1-z)^{\frac{d_1+d_2}{2}}}{\underbrace{\left( \dfrac{1}{1-z} \right)^{-\frac{d_1 + d_2}{2}}}} \cdot\left( \frac{d_2}{d_1} (1-z)^2 dz \right) \\ \\ &=& \left( \dfrac{d_2}{d_1} \right)^{\frac{d_1}{2}} \displaystyle \int_0^{ \frac{d_1 x}{d_1x + d_2} } z^{\frac{d_1}{2}-1} \cdot (1-z)^{\frac{d_2}{2} - 1} dz \\ \\ &=& \displaystyle \left( \frac{d_2}{d_1} \right)^{\frac{d_1}{2}} B\left( \frac{d_1 x}{d_1 x + d_2}, \frac{d_1}{2}, \frac{d_2}{2} \right) \\\\ \Rightarrow \qquad F_X (x, d_1, d_2 ) &=& I_{\frac{d_1 x}{d_1 x+ d_2}} \left( \frac{d_1}{2}, \frac{d_2}{2} \right) \end{array} ")
        elif note == "mode":
            with c21:
                st.write("#### proof of mode")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} x_{\text{mode}} &=& \underset{x \geq 0}{\text{argmax}} \left( \dfrac{ (d_1 / d_2)^{d_1 / 2}}{B \left( \frac{d_1}{2}, \frac{d_2}{2} \right)} \cdot x^{\frac{d_1}{2} - 1} \cdot \left( \frac{d_1}{d_2} x + 1 \right)^{- \frac{d_1+d_2}{2}} \right) \\ &=& \underset{x \geq 0}{\text{argmax}} \left( x^{\frac{d_1}{2} - 1} \cdot \left( \frac{d_1}{d_2} x + 1 \right)^{- \frac{d_1+d_2}{2}} \right) \end{array} ")
                st.write(r"Let $w(x) = \dfrac{x^a}{(c x + 1)^b}$, where $ \left \lbrace \begin{array}{ccl} a &=& \frac{d_1}{2} - 1 \\ b &=& \frac{d_1 + d_2}{2} \\ c &=& \frac{d_1}{d_2} \end{array} \right. $ and we have")
                st.latex(r" \begin{array}{ccl} \dfrac{d}{dx} w(x) &=& \dfrac{x^{a - 1} \left[ a(cx + 1) - bcx \right]}{(cx + 1)^{b + 1}} \end{array} ")
                st.write("and we found the maximize of $w$ at")
                st.latex(r" x_m = \dfrac{a}{(b-a)c} = \dfrac{d_1 - 2}{d_2 + 2} \cdot \dfrac{d_2}{d_1} \qquad \text{if } b > a \Leftrightarrow \forall d_1 > 2")
        elif note == "median":
            with c21:
                st.write("#### proof of median")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have nothing now")
        elif note == "Expectation":
            with c21:
                st.write("#### proof of Expectation")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("Generaly, we have")
                st.latex(r" \mathbb{E} X^k = \left( \frac{d_2}{d_1} \right)^k \cdot \dfrac{\Gamma\left(\frac{d_1}{2} + k \right) \cdot \Gamma\left( \frac{d_2}{2} - k \right)}{\Gamma\left( \frac{d_1}{2} \right) \cdot \Gamma\left( \frac{d_2}{2} \right)} ")
                st.write("Hence, for $k = 1$, we obtain")
                st.latex(r" \begin{array}{ccl} \mathbb{E}X &=& \dfrac{d_2}{d_1} \cdot \underbrace{\dfrac{\Gamma\left( \frac{d_1}{2} + 1 \right)}{\Gamma\left( \frac{d_1}{2} \right) }} \cdot \underbrace{\dfrac{\Gamma\left( \frac{d_2}{2} - 1 \right)}{\Gamma\left( \frac{d_2}{2} \right) }} \\ &=& \dfrac{d_2}{d_1} \quad \cdot \quad\dfrac{d_1}{2} \qquad \cdot \quad \dfrac{1}{ \frac{d_2}{2} - 1 } &=& \dfrac{d_2}{d_2 - 2}, \qquad \forall d_2 > 2 \end{array} ")
                st.write("---------")
                st.write("Now, we will prove this general result, we have known")
                st.latex(r" \mathbb{E}X^k = \dfrac{ \left( d_1 / d_2 \right)^{\frac{d_1}{2}} }{B \left( \frac{d_1}{2}, \frac{d_2}{2} \right)} \int_0^{\infty} x^{\left( k + \frac{d_1}{2} - 1 \right)} \cdot \left( 1 + \frac{d_1}{d_2} x \right)^{ - \left( \frac{d_1+d_2}{2} \right)} dx ")
                st.write(r"Next, let $u = \frac{d_1}{d_2} x$, then")
                st.latex(r" \begin{array}{ccl} x = \dfrac{d_2}{d_1} u & , & \dfrac{dx}{du} = \dfrac{d_2}{d_1} \end{array}")
                st.write("and hence")
                st.latex(r" \begin{array}{ccl} \mathbb{E}X^k &=& \displaystyle \dfrac{ \left( d_1 / d_2 \right)^{\frac{d_1}{2}} }{B \left( \frac{d_1}{2}, \frac{d_2}{2} \right)} \int_0^{\infty} \left[ \left( d_2 / d_1 \right)^{k + \frac{d_1}{2} - 1} u^{k + \frac{d_1}{2} - 1} (1 + u)^{ -\frac{d_1 + d_2}{2} } \right] \cdot \left( \frac{d_2}{d_1} du \right) \\ \\ &=& \displaystyle \dfrac{ \left( d_1 / d_2 \right)^{\frac{d_1}{2}} }{B \left( \frac{d_1}{2}, \frac{d_2}{2} \right)} \int_0^{\infty} u^{k + \frac{d_1}{2} - 1} (1 + u)^{-\frac{d_1 + d_2}{2}} du \qquad \text{let } z = u / (1 + u) \\ &=& \displaystyle \quad \dfrac{ \left( d_1 / d_2 \right)^{\frac{d_1}{2}} }{B \left( \frac{d_1}{2}, \frac{d_2}{2} \right)} \quad \int_0^1 z^{k + \frac{d_1}{2} - 1} (1-z)^{\frac{d_1}{2} - k - 1} dz \quad = \quad \left( \dfrac{d_1}{d_2} \right)^k \cdot \dfrac{B \left( \frac{d_1}{2} + k, \frac{d_2} {2} - k \right)}{B \left( \frac{d_1}{2}, \frac{d_2}{2} \right)} \end{array} ")
                st.write("Finally, applying the `2nd note` in this distribution, we obtain the final result")
        elif note == "variance":
            with c21:
                st.write("#### proof of variance")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("In the `expectation` we have had the generalized result of `non-central moment` order $k$ of this distribution, so ")
                st.latex(r" \begin{array}{ccl}  \mathbb{E}X^2 &=& \left( \dfrac{d_2}{d_1} \right)^2 \cdot \underbrace{\dfrac{\Gamma\left( \frac{d_1}{2} + 2 \right)}{\Gamma\left( \frac{d_1}{2} \right) }} \cdot \underbrace{\dfrac{\Gamma\left( \frac{d_2}{2} - 2 \right)}{\Gamma\left( \frac{d_2}{2} \right) }} \\  &=& \left( \dfrac{d_2}{d_1} \right)^2 \cdot \left( \dfrac{d_1}{2} \cdot \dfrac{d_1 - 2}{2} \right) \cdot \left( \dfrac{1}{ \left( \frac{d_2}{2} - 1 \right) \left( \frac{d_2}{2} - 2 \right) } \right) \\ &=& \dfrac{d_2^2 (d_1 - 2)}{d_1(d_2 - 2)(d_2 - 4)}, \qquad \forall d_2 > 4 \end{array} ")
                st.write("Hence")
                st.latex(r" \begin{array}{ccl} \text{Var} X := \mathbb{E} X - \left( \mathbb{E} X \right)^2 &=& \dfrac{d_2^2 (d_1 - 2)}{d_1(d_2 - 2)(d_2 - 4)} - \left( \dfrac{d_2}{d_2 - 2} \right)^2 \\ \\ &=& \dfrac{d_2^2 \cdot \left[ (d_1 - 2)(d_2 - 2) - d_1 (d_2 - 4) \right]}{d_1(d_2 - 2)^2(d_2 - 4)} &=& \dfrac{2d_2^2 (d_1 + d_2 - 2) }{d_1(d_2 - 2)^2(d_2 - 4)} \end{array} ")
        elif note == "Skewness":
            with c21:
                st.write("#### proof of Skewness")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("In the `expectation` we have had the generalized result of `non-central moment` order $k$ of this distribution, so ")
                st.latex(r" \begin{array}{ccl}  \mathbb{E}X^3 &=& \left( \dfrac{d_2}{d_1} \right)^3 \qquad \cdot \qquad \underbrace{ \dfrac{ \Gamma\left( \frac{d_1}{2} + 3 \right)}{ \Gamma\left( \frac{d_1}{2} \right) }} \qquad \cdot \qquad  \underbrace{ \dfrac{\Gamma\left( \frac{d_2}{2} - 3 \right)}{\Gamma\left( \frac{d_2}{2} \right) }} \\   &=& \left( \dfrac{d_2}{d_1} \right)^3 \cdot \left( \dfrac{d_1}{2} \cdot \dfrac{d_1 - 2}{2} \cdot \dfrac{d_1 - 4}{2} \right) \cdot \left( \dfrac{1}{ \left( \frac{d_2}{2} - 1 \right) \left( \frac{d_2}{2} - 2 \right) \left( \frac{d_2}{2} - 3 \right) } \right) \\  &=& \dfrac{d_2^3 (d_1 - 2)(d_1 - 4)}{d_1^2(d_2 - 2)(d_2 - 4)(d_2 - 6)}, \qquad \forall d_2 > 6 \end{array} ")
                st.write("Also, we have known")
                st.latex(r" \begin{array}{l} \begin{array}{l} \mathbb{E}X = \dfrac{d_2}{d_2 - 2} &, & \mathbb{E}X^2 = \dfrac{d_2^2(d_1 - 2)}{d_1(d_2 - 2)(d_2-4)} &,& \text{Var}X = \dfrac{2d_2^2 (d_1 + d_2 - 2) }{d_1(d_2 - 2)^2(d_2 - 4)} \end{array} \\ \\ \Rightarrow \begin{array}{ccl} \mathbb{E} \left( \dfrac{X - \mu}{\sigma} \right)^3 &=& \dfrac{\mathbb{E}X^3 - 3\mu \mathbb{E}X^2 + 2\mu^3}{\sigma^3} &=& \dfrac{ \left(2d_1 + d_2 - 2\right) \sqrt{8(d_2 - 4)} }{ \left(d_2 - 6\right) \sqrt{d_1(d_1 + d_2 - 2)} } \quad \forall d_2 > 6 \end{array} \end{array} ")
        elif note == "Kurtosis":
            with c21:
                st.write("#### proof of Kurtosis")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("In the `expectation` we have had the generalized result of `non-central moment` order $k$ of this distribution, so ")
                st.latex(r" \begin{array}{ccl}  \mathbb{E}X^4 &=& \dfrac{d_2^4 (d_1 - 2)(d_1 - 4)(d_1 - 6)}{d_1^3(d_2 - 2)(d_2 - 4)(d_2 - 6)(d_2 - 8)}, \qquad \forall d_2 > 8 \end{array}  ")
                st.write("Use the result of the 3 first non-central moments which found in `Expectation, variance, skewness`, we obtain")
                st.latex(r" \begin{array}{ccl} \mathbb{E} \left( \dfrac{X - \mu}{\sigma} \right)^4 &=& \dfrac{ \mathbb{E}X^4 -4 \mu \mathbb{E}X^3 + 6 \mu^2 \mathbb{E}X^2 -3 \mu^4 }{\sigma^4} \\ &=& 12 \cdot  \left[ \dfrac{ d_1 (5d_2 - 22)(d_1 + d_2 - 2) + (d_2 - 4)^2 (d_2 - 2) }      { d_1 (d_2 - 6)(d_2 - 8)(d_1 + d_2 - 2) } \right] \quad \text{for } d_2 > 8 \end{array} ")
        elif note == "Characteristic func":
            with c21:
                st.write("#### proof of CF")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} \varphi_X(t, d_1, d_2) := \mathbb{E} e^{itX} &=& \dfrac{(d_1 / d_2)^{\frac{d_1}{2}}}{B \left( \frac{d_1}{2}, \frac{d_2}{2} \right)} \displaystyle \int_0^{\infty} e^{itx} \left( x^{\frac{d_1}{2} - 1} \cdot \left( 1 + \frac{d_1}{d_2} x \right)^{-\frac{d_1+d_2}{2}} \right) dx \\ &=& \dfrac{(d_1 / d_2)^{\frac{d_1}{2}}}{B \left( \frac{d_1}{2}, \frac{d_2}{2} \right)} \displaystyle \int_0^{\infty} e^{ it \left( d_2 / d_1 \right) z } \left[ \left( \frac{d_2}{d_1} z \right)^{\frac{d_1}{2}-1} \cdot (1+z)^{-\frac{d_1+d_2}{2}} \right] \cdot \left( \frac{d_1}{d_2} dz \right) \\ &=& \dfrac{1}{B \left( \frac{d_1}{2}, \frac{d_2}{2} \right)} \displaystyle \int_0^{\infty} e^{ it \left( d_2 / d_1 \right) z } \left[ z^{\frac{d_1}{2}-1} \cdot (1+z)^{-\frac{d_1+d_2}{2}} \right] dz \end{array} ")
                st.write(r"by letting $z = \frac{d_1}{d_2} x$. Next, using the definition of `confluent hypergeometric function`,")
                st.latex(r" U(a, b, \omega) = \dfrac{1}{\Gamma(a)} \int e^{-\omega z} z^{a-1} (1-z)^{b-a-1} dz ")
                st.write("Now, replace")
                st.latex(r" \begin{array}{c} a = \frac{d_1}{2}, & b = 1 - \frac{d_2}{2}, & \omega = -\frac{d_2}{d_1} i t \end{array} ")
                st.write("We obtain")
                st.latex(r" \begin{array}{ccl} \varphi_X(t, d_1, d_2) &=& \dfrac{1}{B\left( \frac{d_1}{2}, \frac{d_2}{2} \right)} \cdot \left[ \Gamma\left( \frac{d_1}{2} \right) \cdot U \left( \frac{d_1}{2}, 1 - \frac{d_2}{2}, -\frac{d_2}{d_1} it \right) \right] \\ \\   &=& \dfrac{\Gamma\left( \frac{d_1 + d_2}{2} \right)}{\Gamma\left( \frac{d_2}{2} \right)} \cdot U \left( \frac{d_1}{2}, 1 - \frac{d_2}{2}, -\frac{d_2}{d_1} it \right) \end{array} ")
                st.write("-----------")
        elif note == "Entropy":
            with c21:
                st.write("#### proof of Entropy")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("Firstly, we have")
                st.latex(r" \begin{array}{rcl}  \ln f_X(x,d_1,d_2) &=& \qquad -\underbrace{\ln B\left( \frac{d_1}{2}, \frac{d_2}{2} \right)} \quad + \dfrac{d_1}{d_2} \ln \left( \frac{d_1}{2} \right) +\left( \frac{d_1}{2} - 1 \right) \ln x - \dfrac{d_1+d_2}{2} \ln\left( 1 + \frac{d_1}{d_2} x \right) \\ &=& -\left[ \ln \Gamma\left( \frac{d_1}{2} \right) + \ln \Gamma\left( \frac{d_2}{2} \right) \right] + \dfrac{d_1}{d_2} \ln \left( \frac{d_1}{2} \right) +\left( \frac{d_1}{2} - 1 \right) \ln x - \dfrac{d_1+d_2}{2} \ln\left( 1 + \frac{d_1}{d_2} x \right) \\ \\ \mathbb{E} \left( \ln X \right) &=& \dfrac{(d_1 / d_2)^{\frac{d_1}{2}}}{B\left( \frac{d_1}{2}, \frac{d_2}{2} \right)} \displaystyle \int_0^{\infty} (\ln x) \cdot x^{\frac{d_1}{2} - 1} \cdot \left( 1+\frac{d_1}{d_2} x \right)^{-\frac{d_1+d_2}{2} } dx \\ &=& \psi\left( \frac{d_1}{2} \right) \quad - \quad \psi\left( \frac{d_1 + d_2}{2} \right) \quad + \quad \ln \left( \frac{d_1}{d_2} \right) \\ \\ \mathbb{E}\left[ \ln \left( 1 + \frac{d_1}{d_2} X \right) \right] &=& \psi\left( \frac{d_1 + d_2}{2} \right) \quad - \quad \psi\left( \frac{d_2}{2} \right) \end{array} ")
                st.write("where")
                st.latex(r" \psi(z) = \dfrac{d}{dz} \Gamma(z) ")
                st.write("Therefore")
                st.latex(r" \begin{array}{ccl} H(X): = \mathbb{E} \left[ -\ln f_X \right] &=& \Gamma\left( \frac{d_1}{2} \right) + \Gamma\left( \frac{d_2}{2} \right) + \left(1 - \frac{d_1}{2}\right) \psi\left( \frac{d_1}{2} \right) \\ & & \qquad + \left(1 + \frac{d_2}{2}\right) \psi\left( \frac{d_2}{2} \right) - \left( \frac{d_1 + d_2}{2} \right) \psi\left( \frac{d_1 + d_2}{2} \right) + \ln\left( \frac{d_1}{d_2} \right) \end{array} ")                                    

def beta_all_proofs(note):
    from .distr_illus import beta_show
    c1, _, c2 = st.columns([5, 1, 10])
    with c1:
        st.write("#### illustration")
        alpha = st.number_input("Select a value of `alpha`", value=2.0, min_value=0.2, max_value=20.0, help="shape [`higher alpha lean towards 1`]]")
        beta = st.number_input("Select a value of `beta`", value=3.0, min_value=0.2, max_value=20.0, help="shape [`higher beta lean towards 0`]")
        beta_show(alpha, beta)
    with c2:
        st.write("In this disribution, beside the `Gamma`, `Beta function` which introduced in the `Student distr`; also `regularized incomplete beta function` in the `Fisher distribution`, we must know these formula and notation")
        st.latex(r" e^{s} = \sum_{n = 0}^{\infty} \dfrac{s^n}{n!} \qquad \forall s \in (0, 1) \qquad \qquad z^{(n)} := \prod_{j=0}^{n-1} (x-j) ")
        st.write("where $z^{(n)}$ is the `rising factorial`, also called the `Pochhammer symbol`.")
        c21, c22 = st.columns(2)
        if note == "cdf":
            with c21:
                st.write("#### proof of cdf")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write(r"For all $x \in (0, 1)$, we have")
                st.latex(r" P(X < x) = \dfrac{1}{B \left( \alpha, \beta \right)} \int_0^x t^{\alpha - 1} (1 - t)^{\beta - 1} dt = \dfrac{B(x, \alpha, \beta)}{B(\alpha, \beta)} = I_x (\alpha, \beta)")
                st.write("-----------")
                st.write("##### Moment methods")
                st.write(r"To estimate these parameters $\alpha, \beta$, we have used the final results from `Expectation` and `variance`, we have")
                st.latex(r" \left \lbrace \begin{array}{ccl} \mu &=& \dfrac{\alpha}{\alpha + \beta}\\ \sigma^2 &=& \dfrac{\alpha \beta}{(\alpha + \beta)^2 (\alpha + \beta + 1)} \end{array} \right. \Rightarrow \left \lbrace \begin{array}{ccr} \alpha &=& \mu \left( \dfrac{\mu(1 - \mu)}{\sigma^2} - 1 \right)\\ \beta &=& (1 - \mu) \left( \dfrac{\mu(1 - \mu)}{\sigma^2} - 1 \right) \end{array} \right. ")
        elif note == "mode":
            with c21:
                st.write("#### proof of mode")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write(r"For all $x \in (0, 1)$, we have")
                st.latex(r" x_{\text{mode}} = \displaystyle \text{argmax}_{x \in (0, 1)} \dfrac{x^{\alpha - 1} (1-x)^{\beta - 1}}{B(\alpha , \beta)} = \text{argmax}_{x \in (0, 1)} \omega(x) ")
                st.write("where ")
                st.latex(r" \omega(x) = x^{\alpha - 1} (1-x)^{\beta - 1}")
                st.write("Next, we will maximize the function above. Firstly, consider the 1st derivative")
                st.latex(r" \begin{array}{ccl} \dfrac{d}{d x} \omega(x) &=& (\alpha-1)x^{\alpha - 2} (1-x)^{\beta-1} - (\beta - 1)x^{\alpha-1}(1-x)^{\beta-2} \\ &=& x^{\alpha - 2}(1 - x)^{\beta - 2} \left[ (\alpha - 1)(1-x) - (\beta - 1)x \right] \\ &=& x^{\alpha - 2}(1 - x)^{\beta - 2} \left[ \alpha - 1 - (\alpha + \beta - 2) x \right] \end{array} ")
                st.write("Therefore, this function attains maximum at")
                st.latex(r" x_{\text{mode}} = \drac{\alpha - 1}{\alpha + \beta - 2} \qquad \forall \alpha, \beta > 1")                 
        elif note == "median":
            with c21:
                st.write("#### proof of median")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write(r"For all $x \in (0, 1)$, we have")
                st.latex(r" \begin{array}{ccl} x_{\text{med}} &=& \Big \lbrace x_m \in (0, 1) \Big \vert P(X < x_m) = 50\% \Big \rbrace \\ &=& \Big \lbrace x_m \in (0, 1) \Big \vert I_{x_m}(\alpha, \beta) = \frac{1}{2} \Big \rbrace &=& I^{-1}_{1/2} \left( \alpha, \beta \right) \end{array} ")
                st.write("Therefore, a reasonable approximation of the value of the `median` of the beta distribution is given by")
                st.latex(r" \dfrac{\alpha - \frac{1}{3}}{ \alpha + \beta - \frac{2}{3} } \qquad \forall \alpha, \beta \geq 1 ")
        elif note == "Expectation":
            with c21:
                st.write("#### proof of expectation")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write(r"For all $x \in (0, 1)$, we have")
                st.latex(r" \begin{array}{ccl} \mathbb{E} X^k &=& \underbrace{\dfrac{1}{B(\alpha, \beta)}} \quad \cdot \quad \displaystyle \underset{B(\alpha + k, \beta)}{\underbrace{\int_0^1 x^{k + \alpha - 1} (1 - x)^{\beta - 1} dx}} \\ \\ &=& \left[ \dfrac{\Gamma(\alpha + \beta)}{\Gamma(\alpha) \cdot \Gamma(\beta)} \right] \quad \cdot \quad \left[ \dfrac{\Gamma(\alpha + k) \cdot \Gamma(\beta)}{\Gamma(\alpha + \beta +k)} \right] \\ &=& \quad \underset{\prod_{j=1}^{k-1} (\alpha + j)}{\underbrace{ \left( \dfrac{\Gamma(\alpha + k)}{\Gamma(\alpha)}\right)}} \quad \cdot \quad \left[ \underset{\prod_{j=1}^{k-1} (\alpha + \beta + j)}{\underbrace{ \left( \dfrac{\Gamma(\alpha + \beta + k)}{\Gamma(\alpha + \beta)}\right)}} \right]^{-1} &=& \displaystyle \prod_{j=1}^{k-1} \dfrac{\alpha + j}{\alpha + \beta + j} \end{array} ")
                st.write("-----------")
                st.write("So for $k = 1$, we obtain")
                st.latex(r" \mathbb{E}X \quad = \quad \dfrac{\alpha}{\alpha + \beta + 1} ")
        elif note == "variance":
            with c21:
                st.write("#### proof of variance")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("In the `Expectation`, we have found the generalized result of this distribution for the `non-central moment` for all order; therefore")
                st.latex(r" \begin{array}{ccl} \mathbb{E}X^2 &=& \dfrac{\alpha (\alpha + 1)}{\left( \alpha + \beta \right)\left( \alpha + \beta +1 \right)} \end{array} ")
                st.write("Hence")
                st.latex(r" \text{Var} X = \left[ \dfrac{\alpha (\alpha + 1)}{(\alpha + \beta) (\alpha + \beta + 1)} \right] - \left( \dfrac{\alpha}{\alpha + \beta} \right)^2 = \dfrac{\alpha \beta}{(\alpha + \beta)^2 (\alpha + \beta + 1)}")
        elif note == "Skewness":
            with c21:
                st.write("#### proof of Skewness")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("In the `Expectation`, we have found the generalized result of this distribution for the `non-central moment` for all order; therefore")
                st.latex(r" \begin{array}{ccl} \mathbb{E}X^3 &=& \dfrac{\alpha (\alpha + 1)(\alpha + 2)}{\left( \alpha + \beta \right)\left( \alpha + \beta +1 \right)\left( \alpha + \beta + 2 \right)} \end{array} ")
                st.write("Hence")
                st.latex(r" \begin{array}{ccl} \mathbb{E} \left( \frac{X - \mu}{\sigma} \right)^3 &=& \dfrac{\mathbb{E}X^3 - 3\mu \mathbb{E}X^2 + 2\mu^3}{\sigma^3} \\ &=& \left( \dfrac{\alpha \beta}{(\alpha + \beta)^2(\alpha + \beta + 1)} \right)^{-3/2} \cdot \left[ \dfrac{\alpha (\alpha + 1) ( \alpha + 2)}{(\alpha + \beta)(\alpha + \beta + 1)(\alpha + \beta + 2)} \right. \\ & & \qquad \qquad \qquad \left. - 3 \dfrac{\alpha}{\alpha + \beta} \cdot \dfrac{\alpha (\alpha + 1)}{(\alpha + \beta)(\alpha + \beta + 1)} + 2 \left( \dfrac{\alpha}{\alpha + \beta} \right)^3 \right] \\ &=& \dfrac{2(\beta - \alpha)\sqrt{\alpha + \beta + 1}}{(\alpha + \beta + 2)\sqrt{\alpha \beta}} \end{array} ")
        elif note == "Kurtosis":
            with c21:
                st.write("#### proof of Kurtosis")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("In the `Expectation`, we have found the generalized result of this distribution for the `non-central moment` for all order; therefore")
                st.latex(r" \begin{array}{ccl} \mathbb{E}X^4 &=& \dfrac{\alpha (\alpha + 1)(\alpha + 2) (\alpha + 3)}{\left( \alpha + \beta \right)\left( \alpha + \beta +1 \right)\left( \alpha + \beta + 2 \right) (\alpha + \beta + 3)} \end{array} ")
                st.write("Hence")
                st.latex(r" \begin{array}{ccl} \mathbb{E} \left( \frac{X - \mu}{\sigma} \right)^4 &=& \dfrac{\mathbb{E}X^4 - 4\mu \mathbb{E}X^3 + 6\mu^2 \mathbb{E}X^2 - 3 \mu^4}{\sigma^4} \\  &=& 3 + \dfrac{6\left[(\alpha - \beta)^2(\alpha + \beta + 1) - \alpha\beta(\alpha + \beta + 2)\right]}{\alpha\beta(\alpha + \beta + 2)(\alpha + \beta + 3)} \end{array} ")
        elif note == "Characteristic func":
            with c21:
                st.write("#### proof of CF")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} \varphi_X(t) &=& \displaystyle \dfrac{1}{B(\alpha, \beta)} \int_0^1 e^{itx} x^{\alpha - 1} (1 - x)^{\beta - 1} dx \\ &=& \displaystyle \sum_{n=0}^{\infty} \dfrac{1}{B(\alpha, \beta)} \int_0^1 \dfrac{(itx)^n}{n!} \cdot x^{\alpha - 1} (1 - x)^{\beta - 1} dx \\ &=& \displaystyle \sum_{n=0}^{\infty} \dfrac{(it)^n}{n!} \cdot \underset{ \mathbb{E} (X^n) }{\underbrace{\left[ \dfrac{1}{B(\alpha, \beta)} \int_0^1 x^{n + \alpha - 1} (1 - x)^{\beta - 1} dx  \right]}} \\ &=& \displaystyle \sum_{n=0}^{\infty} \dfrac{(it)^n}{n!} \prod_{j=1}^{n-1} \dfrac{\alpha + j}{\alpha + \beta + j} &=& 1 + \displaystyle \sum_{n=1}^{\infty} \dfrac{(it)^n}{n!} \prod_{j=1}^{n-1} \dfrac{\alpha + j}{\alpha + \beta + j} \end{array} ")
        elif note == "Moment generating func":
            with c21:
                st.write("#### proof of MGF")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("By the same idea as in `CF`, we have")
                st.latex(r" \begin{array}{ccl} M_X(t) &=& \displaystyle \dfrac{1}{B(\alpha, \beta)} \int_0^1 e^{tx} x^{\alpha - 1} (1 - x)^{\beta - 1} dx \\ &=& \displaystyle \sum_{n=0}^{\infty} \dfrac{1}{B(\alpha, \beta)} \int_0^1 \dfrac{(tx)^n}{n!} \cdot x^{\alpha - 1} (1 - x)^{\beta - 1} dx \\ &=& \displaystyle \sum_{n=0}^{\infty} \dfrac{t^n}{n!} \cdot \underset{ \mathbb{E} (X^n) }{\underbrace{\left[ \dfrac{1}{B(\alpha, \beta)} \int_0^1 x^{n + \alpha - 1} (1 - x)^{\beta - 1} dx  \right]}} &=& 1 + \displaystyle \sum_{n=1}^{\infty} \dfrac{t^n}{n!} \prod_{j=1}^{n-1} \dfrac{\alpha + j}{\alpha + \beta + j} \end{array} ")    
        elif note == "Entropy":
            with c21:
                st.write("#### proof of Entropy")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("Firstly, we have")
                st.latex(r" \begin{array}{rcl} -\ln f_X(x, \alpha, \beta) &=& \ln B(\alpha, \beta) + (\alpha - 1) \ln x + (\beta - 1) \ln (1 - x) \\ \mathbb{E} (\ln X) &=& \displaystyle B^{-1}(\alpha, \beta) \int_0^1 (\ln x) x^{\alpha - 1}(1 - x)^{\beta - 1} dx \\ &=& \displaystyle B^{-1}(\alpha, \beta) \displaystyle \int_0^1 \dfrac{d}{d\alpha} \left( x^{\alpha-1} (1-x)^{\beta-1} \right)dx \\ &=& \displaystyle B^{-1}(\alpha, \beta) \left[ \dfrac{d}{d\alpha} \underset{B(\alpha, \beta)}{\underbrace{\int_0^1 x^{\alpha - 1} (1 - x)^{\beta - 1} dx}} \right] \\ &=& \dfrac{\frac{d}{d\alpha} B(\alpha, \beta)}{B(\alpha, \beta)} \quad = \quad \underset{\frac{d}{d\alpha} \left( \ln \Gamma(\alpha) \quad - \quad \Gamma(\alpha + \beta) \right)}{\underbrace{\dfrac{d}{d\alpha} \ln B(\alpha, \beta)}} \quad = \quad \quad \psi(\alpha) \quad - \quad \psi(\alpha + \beta) \\ \mathbb{E} \left[ \ln (1 - X) \right] &=& B^{-1}(\alpha, \beta) \displaystyle \int_0^1 \ln(1-x) x^{\alpha-1} (1-x)^{\beta - 1} dx \\ &=& B^{-1}(\alpha, \beta) \displaystyle \int_0^1 (\ln u) \cdot (1 - u)^{\alpha-1} u^{\beta - 1} du \\ &=& B^{-1}(\alpha, \beta) \displaystyle \int_0^1 \dfrac{d}{d\beta} \left( u^{\beta - 1} (1- u)^{\alpha - 1} \right) du \\ &=& \dfrac{d}{d\beta} \ln B(\alpha, \beta) \quad = \quad \psi(\beta) \quad - \quad \psi(\alpha + \beta) \end{array} ")
                st.write("Therefore")
                st.latex(r" \begin{array}{ccl} H_X(\alpha, \beta) &=& \mathbb{E} (-\ln f_X) \\ \\ &=& \ln B(\alpha, \beta) - (\alpha - 1) \psi(\alpha) - (\beta-1) \psi(\beta) + (\alpha + \beta - 2) \psi(\alpha + \beta) \end{array} ")
        elif note == "Fisher information":
            with c21:
                st.write("#### proof of Fisher information")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("Firstly, we have")
                st.latex(r" \ln f_X(x, \alpha, \beta) = -\ln B(\alpha, \beta) + (\alpha - 1) \ln x + (\beta - 1) \ln (1-x) ")
                st.write("Therefore")
                st.latex(r" \left \lbrace \begin{array}{ccl} \dfrac{d}{d\alpha} \ln f_X &=& \ln x + \dfrac{d}{d\alpha} \ln B(\alpha, \beta) \\ \\ \dfrac{d}{d\beta} \ln f_X &=& \ln (1-x) + \dfrac{d}{d\beta} \ln B(\alpha, \beta) \\ \\ \dfrac{d^2}{d\alpha d\beta} \ln f_X &=& \left( \ln x + \dfrac{d}{d\alpha} \ln B(\alpha, \beta)\right) \cdot \left( \ln (1-x) + \dfrac{d}{d\beta} \ln B(\alpha, \beta) \right) \\ \end{array} \right. ")
                st.write("Looking back at the tricks in proofs of `Entropy`, we have")
                st.latex(r" \begin{array}{ccl} \dfrac{d}{d\alpha} \ln B(\alpha, \beta) &=& \mathbb{E}_X \ln X &, & \dfrac{d}{d\beta} \ln B(\alpha, \beta) &=& \mathbb{E}_X \ln (1-X) \end{array}  ")
                st.write("Hence, the fisher information defined by")
                st.latex(r" \begin{array}{ccl} I_{X}(\alpha, \beta) &=& \left[ \begin{array}{cc}  \mathbb{E}\left( \frac{d}{d \alpha} \ln f_X \right)^2 & \mathbb{E}\left( \frac{d^2}{d \alpha d\beta} \ln f_X \right) \\ \mathbb{E}\left( \frac{d^2}{d \alpha d\beta} \ln f_X \right) & \mathbb{E}\left( \frac{d}{d \beta} \ln f_X \right)^2 \end{array} \right] \\ \\ &=& \left[ \begin{array}{cc}  \mathbb{E} \left( \ln X - \mathbb{E} \ln X \right)^2 & \mathbb{E} \left[ \left( \ln X - \mathbb{E} \ln X \right)\left( \ln (1-X) - \mathbb{E} \ln (1-X) \right) \right]\\ \mathbb{E} \left[ \left( \ln X - \mathbb{E} \ln X \right)\left( \ln (1-X) - \mathbb{E} \ln (1-X) \right) \right] & \mathbb{E} \left( \ln (1-X) - \mathbb{E} \ln (1-X) \right)^2 \end{array} \right] \\ \\ &=& \left[ \begin{array}{cc}  \text{Var} \ln X & \text{Cov}(\ln X, \ln(1-X)) \\ \text{Cov}(\ln X, \ln(1-X)) & \text{Var} \ln(1-X) \\ \end{array} \right] \end{array} ")

def gamma_all_proofs(note):
    from .distr_illus import gamma_show
    c1, _, c2 = st.columns([5, 1, 10])
    with c1:
        st.write("`Density function`")
        st.latex(r" f_X = \dfrac{\lambda^{\alpha}}{\Gamma(\alpha)} x^{\alpha - 1} e^{-\lambda x}, \qquad x \geq 0 ")
        st.write(r"where $\alpha, \lambda > 0$")        
        st.write("#### illustration") 
        alpha = st.number_input("Select a value of `alpha`", value=2.0, min_value=0.1, max_value=20.0, help="shape")
        theta = st.number_input("Select a value of `lambda`", value=3.0, min_value=0.1, max_value=20.0, help="scale") 
        gamma_show(alpha, theta)
    with c2:
        st.write("In this disribution, we only focus on `Gamma`, `incompleted gamma` and `Digamma` functions which introduced in `Student` and `chi-squared` distributions")
        c21, c22 = st.columns(2)
        if note == "cdf":
            with c21:
                st.write("#### proof of cdf")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("Firstly, we have")
                st.latex(r" \begin{array}{ccl} F_X(x) := P(X < x) &=& \displaystyle \dfrac{\lambda^{\alpha}}{\Gamma(\alpha)} \int_0^x t^{\alpha - 1} e^{-\lambda t} dt & \forall x > 0 \\ &=& \displaystyle \dfrac{1}{\Gamma(\alpha)} \int_0^x (\lambda x)^{\alpha - 1} e^{-\lambda x} \cdot \left( \lambda dx \right) & \text{now let } z = \lambda x \\ &=&  \dfrac{1}{\Gamma(\alpha)} \displaystyle \int_0^{\lambda x} z^{\alpha - 1} e^{-z} dz &=\quad \dfrac{\gamma(\lambda x, \alpha)}{\Gamma(\alpha)} \end{array} ")
                st.write("-----------")
                st.write("##### Moment methods")
                st.write(r"To estimate these parameters $\alpha, \lambda$, we have used the final results from `Expectation` and `variance`, we have")
                st.latex(r" \left \lbrace \begin{array}{ccl} \mu &=& \dfrac{\alpha}{\lambda} \\ \sigma^2 &=& \dfrac{\alpha}{\lambda^2} \end{array} \right. \quad \Rightarrow \quad \left \lbrace \begin{array}{ccl}  \alpha &=& \dfrac{\mu^2}{\sigma^2} \\ \lambda &=& \dfrac{\mu}{\sigma^2} \end{array} \right. ")
        elif note == "mode":
            with c21:
                st.write("#### proof of mode")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} x_{\text{mode}} &=& \underset{x \geq 0}{\text{argmax}} \quad f_X(x, \alpha, \lambda) &=& \underset{x \geq 0}{\text{argmax}} \left( x^{\alpha - 1} e^{-\lambda x} \right) &=& \left\lbrace 0, \dfrac{\alpha - 1}{\lambda} \right\rbrace \end{array} ")
                st.write(r"Indeed, let $\omega(x) := x^{\alpha - 1} e^{-\lambda x}$, then")
                st.latex(r" \begin{array}{crlc} & \omega'(x) &=& 0 \\ \Rightarrow & \left[ (\alpha - 1) x^{\alpha - 2} \cdot e^{-\lambda x} \right] + \left[ - \lambda e^{-\lambda x} \cdot x^{\alpha - 1} \right] &=& 0 \\ \Rightarrow & \left( x^{\alpha - 2} e^{-\lambda x} \right) \cdot\left[  \left( \alpha - 1 \right) - \lambda x \right] &=& 0 \\ \Rightarrow & x &=& \left\lbrace 0, \dfrac{\alpha - 1}{\lambda} \right\rbrace \end{array} ")
                st.write("Therefore")
                st.latex(r" x_{\text{mode}} = \left \lbrace \begin{array}{ccl} \dfrac{\alpha-1}{\lambda} &, & \alpha \geq 1 \\ \\ 0 &, & \alpha < 1 \end{array} \right. ")
        elif note == "median":
            with c21:
                st.write("#### proof of median")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("Until now, we dont have the simple form of median for this distribution")
        elif note == "Expectation":
            with c21:
                st.write("#### proof of Expectation")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("Generally, we have")
                st.latex(r" \mathbb{E} X^k =\prod_{j=1}^{k} \dfrac{\alpha + i - 1}{\lambda} ")
                st.write(r"So for $k=1$, we obtain")
                st.latex(r" \mathbb{E}X = \frac{\alpha}{\lambda} ")
                st.write("----------")
                st.write("Indeed,")
                st.latex(r" \begin{array}{ccl} \mathbb{E} X^k &=& \displaystyle \dfrac{\lambda^{\alpha}}{\Gamma(\alpha)} \int_0^{\infty} x^{k + (\alpha - 1)} \cdot e^{-\lambda x} dx \\ \\ &=& \displaystyle \dfrac{\lambda^{\alpha}}{\Gamma(\alpha)} \int_0^{\infty} x^{(k + \alpha) - 1} \cdot e^{-\lambda x} dx \\ \\ &=& \displaystyle \dfrac{\lambda^{\alpha}}{\Gamma(\alpha)} \cdot \left[ \dfrac{1}{\lambda^{k+\alpha}} \int_0^{\infty} (\lambda x)^{(k + \alpha) - 1} \cdot e^{-\lambda x} \lambda dx \right] & \text{let } z = \lambda x \\ \\ &=& \displaystyle \dfrac{\lambda^{\alpha}}{\Gamma(\alpha)} \cdot \dfrac{1}{\lambda^{k+\alpha}} \cdot \underset{\Gamma(\alpha + k)}{\underbrace{\left[ \int_0^{\infty} z^{(k + \alpha) - 1} \cdot e^{-z} dz \right]}} \\ &=& \quad \lambda^{-k} \cdot \dfrac{\Gamma(\alpha + k)}{\Gamma (\alpha)} \qquad = \qquad \displaystyle \prod_{j=1}^{k} \dfrac{\alpha + j - 1}{\lambda} \end{array} ")
        elif note == "variance":
            with c21:
                st.write("#### proof of Expectation")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write(r"In the `Expectation`, we have found the general formula for the `non-central moment` order $k$, hence for $k=2$, we obtain")
                st.latex(r" \mathbb{E}X^2 = \prod_{j=1}^{2} \dfrac{\alpha + j - 1}{\lambda} = \dfrac{\alpha(\alpha + 1)}{\lambda^2} ")
                st.write("Therefore")
                st.latex(r" \text{Var} X = \mathbb{E}X^2 - \left( \mathbb{E} X \right)^2 = \dfrac{\alpha (\alpha + 1)}{\lambda^2} - \left( \dfrac{\alpha}{\lambda} \right)^2 = \dfrac{\alpha}{\lambda^2} ")
        elif note == "Skewness":
            with c21:
                st.write("#### proof of Skewness")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write(r"In the `Expectation`, we have found the general formula for the `non-central moment` order $k$, hence for $k=3$, we obtain")
                st.latex(r" \mathbb{E}X^3 = \prod_{j=1}^{3} \dfrac{\alpha + j - 1}{\lambda} = \dfrac{\alpha(\alpha + 1)(\alpha + 2)}{\lambda^3} ")
                st.write("Also, we will apply the results of the first 2 `noncentral moments` order which found from `Expectation` and `variance`. Therefore")
                st.latex(r" \begin{array}{ccl} \mathbb{E} \left( \dfrac{X - \mu}{\sigma} \right)^3 &=& \dfrac{\mathbb{E}X^3 - 3\mu \mathbb{E}X^2 + 2\mu^3}{\sigma^3} \\ \\ &=& \dfrac{\frac{\alpha (\alpha +1) (\alpha + 2)}{\lambda^3} - 3 \frac{\alpha}{\lambda} \cdot \frac{\alpha (\alpha+1)}{\lambda^2} + 2 \frac{\alpha^3}{\lambda^3} }{ \alpha^{3/2} \cdot {\lambda^{-3}} } \\ \\ &=& \dfrac{\alpha \left[ (\alpha^2 + 3 \alpha + 2) - 3(\alpha^2 + \alpha) + 2\alpha^2 \right]}{\alpha \sqrt{\alpha}} &=& \dfrac{2}{\sqrt{\alpha}} \end{array} ")
        elif note == "Kurtosis":
            with c21:
                st.write("#### proof of Kurtosis")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write(r"In the `Expectation`, we have found the general formula for the `non-central moment` order $k$, hence for $k=3$, we obtain")
                st.latex(r" \mathbb{E}X^4 = \prod_{j=1}^{4} \dfrac{\alpha + j - 1}{\lambda} = \dfrac{\alpha(\alpha + 1)(\alpha + 2)(\alpha + 3)}{\lambda^4} ")
                st.write("Also, we will apply the results of the first 3 `noncentral moments` order which found from `Expectation`, `variance`. Therefore")
                st.latex(r" \begin{array}{ccl}  \mathbb{E} \left( \dfrac{X - \mu}{\sigma} \right)^4 &=& \dfrac{\mathbb{E}X^4 - 4\mu \mathbb{E}X^2 + 6 \mu^2 \mathbb{E}X^2 -3\mu^4 }{\sigma^4} \\ \\  &=& \dfrac{ \frac{\alpha(\alpha+1)(\alpha+2)(\alpha+3)}{\lambda^4} - 4\frac{\alpha}{\lambda} \cdot \frac{\alpha (\alpha +1) (\alpha + 2)}{\lambda^3} - 6 \frac{\alpha^2}{\lambda^2} \cdot \frac{\alpha (\alpha+1)}{\lambda^2} - 3 \frac{\alpha^4}{\lambda^4} }{ \alpha^{2} \cdot {\lambda^{-4}} } \\ \\  &=& \dfrac{\alpha \left[ (\alpha^3 + 6 \alpha^2 + 11\alpha + 6) - 4(\alpha^3 + 3\alpha^2 +2\alpha) + 6(\alpha^3 + \alpha^2) - 3\alpha^3 \right]}{\alpha^2} &=& \dfrac{6}{{\alpha}} \end{array} ")
        elif note == "Characteristic func":
            with c21:
                st.write("#### proof of CF")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} \varphi_X (t) &=& \displaystyle \frac{\lambda^{\alpha}}{\Gamma(\alpha)} \int_0^{\infty} e^{itx} \cdot \left( x^{\alpha - 1} e^{-\lambda x} \right) dx \\ \\ &=& \displaystyle \frac{\lambda^{\alpha}}{\Gamma(\alpha)} \cdot \underbrace{\int_0^{\infty} x^{\alpha - 1} e^{-(\lambda -it)x} dx} & , & z=(\lambda - it)x \\ \\ &=& \displaystyle \frac{\lambda^{\alpha}}{\Gamma(\alpha)} \cdot \left[ \int_0^{\infty} \left( \frac{z}{\lambda - it} \right)^{\alpha - 1} e^{-z} \cdot \left( (\lambda - it)^{-1}dz \right) \right] \\ \\ &=& \displaystyle \frac{\lambda^{\alpha}}{\Gamma(\alpha)} \cdot \left( \dfrac{1}{\lambda - it} \right)^{\alpha} \underset{\Gamma(\alpha)}{\underbrace{\int_0^{\infty} z^{\alpha - 1} e^{-z} dz }} \\ &=& \qquad \left( \dfrac{\lambda - it}{\lambda} \right)^{-\alpha} &=& \left( 1 - \dfrac{it}{\lambda} \right)^{-\alpha} \end{array} ")
        elif note == "Moment generating func":
            with c21:
                st.write("#### proof of MGF")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \begin{array}{ccl} M_X (t) &=& \displaystyle \frac{\lambda^{\alpha}}{\Gamma(\alpha)} \int_0^{\infty} e^{tx} \cdot \left( x^{\alpha - 1} e^{-\lambda x} \right) dx \\ \\  &=& \displaystyle \frac{\lambda^{\alpha}}{\Gamma(\alpha)} \cdot \underbrace{\int_0^{\infty} x^{\alpha - 1} e^{-(\lambda - t)x} dx} & , & z=(\lambda - t)x \\ \\  &=& \displaystyle \frac{\lambda^{\alpha}}{\Gamma(\alpha)} \cdot \left[ \int_0^{\infty} \left( \frac{z}{\lambda - t} \right)^{\alpha - 1} e^{-z} \cdot \left( (\lambda - t)^{-1}dz \right) \right] \\ \\  &=& \displaystyle \frac{\lambda^{\alpha}}{\Gamma(\alpha)} \cdot \left( \dfrac{1}{\lambda - t} \right)^{\alpha} \underset{\Gamma(\alpha), \quad \forall (\lambda - t) > 0 }{\underbrace{\int_0^{\infty} z^{\alpha - 1} e^{-z} dz }} \\  &=& \qquad \quad \left( \dfrac{\lambda - t}{\lambda} \right)^{-\alpha} \qquad \qquad \forall t \in (0, \lambda) &=& \left( 1 - \dfrac{t}{\lambda} \right)^{-\alpha} \end{array} ")
                st.write("-----------")
                st.write(r"Sometime, the MGF wont be existed if the term $e^{tx}$ is not bounded in the domain of support of the considered distribution.")
        elif note == "Entropy":
            with c21:
                st.write("#### proof of Entropy")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \ln f_X (\alpha, \lambda) = \ln \left( \dfrac{\lambda^{\alpha}}{\Gamma (\alpha) } \right) + (\alpha - 1) \ln x - \lambda x ")
                st.write("and")
                st.latex(r" \begin{array}{ccl} \mathbb{E} \ln X &=& \displaystyle \dfrac{\lambda^{\alpha}}{\Gamma(\alpha)} \cdot \int_0^{\infty} (\ln x) \cdot \left( x^{\alpha - 1} e^{-\lambda x} \right) dx \\ \\ &=& \displaystyle \dfrac{\lambda^{\alpha}}{\Gamma(\alpha)} \cdot \int_0^{\infty} \left[ \dfrac{d}{d \alpha} \left( x^{\alpha - 1} e^{-\lambda x} \right) \right] dx \\ \\ &=& \displaystyle \dfrac{\lambda^{\alpha}}{\Gamma(\alpha)} \cdot \left[ \dfrac{d}{d \alpha} \left( \int_0^{\infty} \lambda^{-\alpha} \cdot z^{\alpha - 1} e^{-z} dz \right) \right] \\ \\ &=& \displaystyle \dfrac{\lambda^{\alpha}}{\Gamma(\alpha)} \quad \cdot \quad \dfrac{d}{d\alpha} \left( \lambda^{-\alpha} \Gamma (\alpha) \right) \\ \\ &=& \displaystyle \dfrac{\lambda^{\alpha}}{\Gamma(\alpha)} \cdot \left[ -\ln \lambda \cdot \lambda^{-\alpha} \Gamma(\alpha) + \lambda^{-\alpha} \cdot \Gamma'(\alpha) \right] &=&-\ln \lambda+\dfrac{\Gamma'(\alpha)}{\Gamma(\alpha)} &=& -\ln \lambda + \psi(\alpha) \end{array} ")
                st.write("Therefore")
                st.latex(r" \begin{array}{ccl} H_X(\alpha, \lambda) := \mathbb{E} \left[ - \ln f_X \right] &=& \lambda (\mathbb{E}X) + (\alpha - 1) (\mathbb{E} \ln X) - \ln \left( \dfrac{\lambda^{\alpha}}{\Gamma(\alpha)} \right) \\ \\ &=& \lambda \cdot \dfrac{\alpha}{\lambda} + (\alpha - 1) \cdot \left[ \psi(\alpha) - \ln \lambda \right] - \left( \alpha \ln \lambda - \ln \Gamma(\alpha) \right) \\ \\ &=& \quad \alpha \quad + \quad (\alpha - 1) \psi(\alpha) \quad - \quad \ln \lambda \quad + \quad \ln \Gamma(\alpha) \end{array} ")
        elif note == "Fisher information":
            with c21:
                st.write("#### proof of Fisher information")
            with c22:
                button_trig = st.button("Show the proof")
            if button_trig:
                st.write("We have")
                st.latex(r" \ln f_X (\alpha, \lambda) = \alpha \ln \lambda - \ln \Gamma(\alpha) + (\alpha - 1) \ln x - \lambda x ")
                st.latex(r" \Rightarrow \left \lbrace \begin{array}{ccl} \dfrac{d}{d\alpha} \ln f_X &=& \ln x + \ln \lambda - \dfrac{d}{d \alpha} \left( \ln \Gamma(\alpha) \right) \quad = \quad \ln x - \left( \psi(\alpha) - \ln \lambda \right) \\ \\ \dfrac{d}{d\lambda} \ln f_X &=& \dfrac{\alpha} {\lambda} - X \\  \\ \dfrac{d^2}{d\alpha d\lambda} \ln f_X &=& \dfrac{d}{d\alpha} \left( \dfrac{d}{d\lambda} \ln f_X \right) \quad = \quad \dfrac{1}{\lambda} \\ \end{array} \right. ")
                st.write("Look at the proofs of `expectation`, `variance` and `entropy`, we have found that")
                st.latex(r" \mathbb{E} X = \dfrac{\alpha}{\lambda} \qquad \text{Var} X = \alpha \lambda^{-2} \qquad \mathbb{E} \ln X = \psi(\alpha) - \ln \lambda")
                st.write("Therefore")
                st.latex(r" \begin{array}{ccl} I_X (\alpha, \lambda) &=& \mathbb{E} \left[ \begin{array}{ccl}  \left( \frac{d}{d \alpha} \ln f_X \right)^2 & \left( \frac{d^2}{d \alpha d\lambda} \ln f_X \right)\\  \left( \frac{d^2}{d \alpha d\lambda} \ln f_X \right) & \left( \frac{d}{d \lambda} \ln f_X \right)^2 \end{array} \right] \\ \\ &=& \left[ \begin{array}{ccl} \mathbb{E}\left( \ln X - \mathbb{E} \ln X \right)^2 & \mathbb{E} \left( \lambda^{-1} \right) \\ \mathbb{E} \left( \lambda^{-1} \right) & \mathbb{E}\left( X - \mathbb{E}X \right)^2 \end{array} \right] &=& \left[ \begin{array}{ccl} \Psi^{(1)} (\alpha) & \lambda^{-1} \\ \lambda^{-1} & \alpha \lambda^{-2} \end{array} \right] \end{array} ")
                st.write(r"where $\Psi^{(1)} (\alpha)$ is the `trigamma function`")
                st.latex(r" \Psi^{(1)}(\alpha) := \text{Var}( \ln X ) := \dfrac{d^2}{d\alpha^2} \Gamma(\alpha)")
                                
def distr_show(distr_name, note): 
    if distr_name == "Bernoulli":
        bernoulli_all_proofs(note)
    elif distr_name == "Binomial":
        binomial_all_proofs(note)
    elif distr_name == "Poisson":
        poisson_all_proofs(note) 
    elif distr_name == "Geometry":
        geometry_all_proofs(note)
    elif distr_name == "HyperGeometry":
        hypergeometry_all_proofs(note)
    elif distr_name == "Negative Binomial":
        nega_binom_all_proofs(note)
    elif distr_name == "Negative HyperGeometry":
        nega_hypergeo_all_proofs(note)
    elif distr_name == "Uniform (descrete type)":
        unif_descrete_all_proofs(note)
    elif distr_name == "Uniform (continuous type)":
        unif_cts_all_proofs(note)
    elif distr_name == "Normal":
        normal_all_proofs(note)
    elif distr_name == "Exponential":
        expo_all_proofs(note)
    elif distr_name == "Cauchy":
        cauchy_all_proofs(note)
    elif distr_name == "Student":
        student_all_proofs(note)
    elif distr_name == "Chi-squared":
        chisq_all_proofs(note)
    elif distr_name == "Fisher":
        fisher_all_proofs(note)
    elif distr_name == "Beta":
        beta_all_proofs(note)
    elif distr_name == "Gamma":
        gamma_all_proofs(note)

def display_proofs(topic, branch_1, branch_2):
    if topic == "Distribution's properties":
        distr_show(branch_1, branch_2)
    elif topic == "Confidence interval of estimators":
        return 1
    
proof_dict = {
    "Distribution's properties": 
        {
            "Bernoulli": ["cdf", "Expectation", "mode", "median", "variance", "Kurtosis", "Skewness", "Characteristic func", "Moment generating func", "Proba generating func", "Fisher information", "Entropy"], 
            "Binomial": ["cdf", "Expectation", "mode", "median", "variance", "Kurtosis", "Skewness", "Characteristic func", "Moment generating func", "Proba generating func", "Fisher information", "Entropy"], 
            "Poisson": ["cdf", "Expectation", "mode", "median", "variance", "Kurtosis", "Skewness", "Characteristic func", "Moment generating func", "Proba generating func", "Fisher information", "Entropy"], 
            "Geometry": ["cdf", "Expectation", "mode", "median", "variance", "Kurtosis", "Skewness", "Characteristic func", "Moment generating func", "Proba generating func", "Fisher information", "Entropy"], 
            "HyperGeometry": ["cdf", "Expectation", "mode", "median", "variance", "Kurtosis", "Skewness", "Characteristic func", "Moment generating func", "Proba generating func", "Fisher information", "Entropy"], 
            "Negative Binomial": ["cdf", "Expectation", "mode", "median", "variance", "Kurtosis", "Skewness", "Characteristic func", "Moment generating func", "Proba generating func", "Fisher information", "Entropy"], 
            "Negative HyperGeometry": ["cdf", "Expectation", "mode", "median", "variance", "Kurtosis", "Skewness", "Characteristic func", "Moment generating func", "Proba generating func", "Fisher information", "Entropy"], 
            "Uniform (descrete type)": ["cdf", "Expectation", "mode", "median", "variance", "Kurtosis", "Skewness", "Characteristic func", "Moment generating func", "Proba generating func", "Fisher information", "Entropy"], 
            "Uniform (continuous type)": ["cdf", "Expectation", "mode", "median", "variance", "Kurtosis", "Skewness", "Characteristic func", "Moment generating func", "Fisher information", "Entropy"], 
            "Normal": ["cdf", "Expectation", "mode", "median", "variance", "Kurtosis", "Skewness", "Characteristic func", "Moment generating func", "Fisher information", "Entropy"], 
            "Exponential": ["cdf", "Expectation", "mode", "median", "variance", "Kurtosis", "Skewness", "Characteristic func", "Moment generating func", "Fisher information", "Entropy"], 
            "Student": ["cdf", "Expectation", "mode", "median", "variance", "Kurtosis", "Skewness", "Characteristic func", "Moment generating func", "Fisher information", "Entropy"], 
            "Chi-squared": ["cdf", "Expectation", "mode", "median", "variance", "Kurtosis", "Skewness", "Characteristic func", "Moment generating func", "Fisher information", "Entropy"], 
            "Fisher": ["cdf", "Expectation", "mode", "median", "variance", "Kurtosis", "Skewness", "Characteristic func", "Moment generating func", "Fisher information", "Entropy"], 
            "Beta": ["cdf", "Expectation", "mode", "median", "variance", "Kurtosis", "Skewness", "Characteristic func", "Moment generating func", "Fisher information", "Entropy"], 
            "Gamma": ["cdf", "Expectation", "mode", "median", "variance", "Kurtosis", "Skewness", "Characteristic func", "Moment generating func", "Fisher information", "Entropy"], 
            "Cauchy": ["cdf", "Expectation", "mode", "median", "variance", "Kurtosis", "Skewness", "Characteristic func", "Moment generating func", "Fisher information", "Entropy"]
        },
    "Confidence interval of estimators": 
        {
            "Simple Linear Regression": ["slope", "intercept"],
            "Multiple Linear Regression": ["coefficients"],             
        },
    "Convergence Theorem":
        {
            "Distribution inference": ["Student", "Fisher", "Chi-squared", "Erlang", "Wilshart"]
        }
}