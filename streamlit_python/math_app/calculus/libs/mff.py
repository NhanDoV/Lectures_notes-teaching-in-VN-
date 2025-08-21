import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go

topic_dict = {
    "Calculus": ["Convergence", "Limitation", "Integration", "Differential equation"],
    "Transforms": ["Fourier transform", "Laplace transform", "Polar coordinate"],
    "Series & Identities": ["Series identity", "Most famous inequalities"],
    "Applications & Fun": ["Famous paradoxes", "Real-life math tricks"]
}

def convergence():
    def get_sims():
        st.write("Here I will give you some examples to understand the epsilon-delta concept just for `sequence`, for `series` you can refer in topic `Series & identities`")
        series_form = st.selectbox("Select the `form`", ["simple", "fractional", "trigeometric"])
        if series_form == "simple":
            st.write(r"- Here we will consider a very simple case")
            st.latex(r" \begin{array}{ccl} x_n = 2 + \frac{1}{n} & & x_0 = 2 \\ y_n = (-1)^n & & z_n = 2^n \end{array}")
            st.write(r"- Then $x_n$ converges to $x_0$ but $(y_n)$ and $(z_n)$ is `diverge`")
            fig, ax = plt.subplots(3, 1, figsize=(6, 6))
            n = list(range(2, 150))
            xn = [(2 + 1 / t) for t in n]
            epsilons = [10, 100]
            ax[0].plot(n, xn, label="$x_n$", color = "green")
            ax[0].plot([0, 150], [2, 2], label='$x_0$', color="blue")
            for idx, eps in enumerate(epsilons):
                ax[0].plot( [eps, eps] , [1.8, 2 + (1/eps)], '--', color='red', alpha=0.75 / (idx+1) )
                ax[0].plot(eps, 2 + (1/eps), 's', markersize=3, color='red')
                ax[0].plot( [0, eps] , [2 + (1/eps), 2 + (1/eps)], '--', color="red", alpha=0.75 / (idx+1) )
                ax[0].text(eps, 2 + 1/eps + 0.05, r"$\epsilon$"+f"={1 /eps} , " + r"$n_{\epsilon}$"+f"={1+eps}")
            ax[0].set_ylim([1.8, 3])
            ax[0].plot([0, 110], [0, 0], color='black')
            ax[0].legend()
            ax[1].plot(range(10, 100), [(-1)**t for t in range(10, 100)], label="$y_n$", color='green')
            ax[1].plot([10, 100], [-1, -1], label = 'y=-1', color='blue')
            ax[1].plot([10, 100], [1, 1], label = 'y=1', color='cyan')
            ax[1].legend(loc="lower left")
            ax[2].plot(range(1, 101), [2**t for t in range(1, 101)], label=r"$z_n$", color='green')
            ax[2].plot([1, 100], [1.1*2**100, 1.1*2**100], label = r'$\infty$', color='blue')
            ax[2].legend(loc="center left")
            plt.tight_layout()
            st.pyplot(fig)
        elif series_form == "fractional":
            st.write(r"- Here we will consider a more complexity case")
            st.latex(r" x_n = \dfrac{n + 5}{n^2 + 1} \qquad x_0 = 0 ")
            st.write(r"- And this is easy to see that $x_n$ converges to $x_0$, now, please select $\epsilon$ to find the $n_{\epsilon}$")
            eps = st.number_input("Select your `epsilon`", value=0.5, min_value=0.001, max_value=2.0)
            n_eps = int( (1 + (1 - 4*eps*(eps - 5))**0.5) / (2*eps) ) + 1
            fig, ax = plt.subplots(1, 1, figsize=(6, 3))
            ax.plot(range(50), [(n + 5)/(n**2 + 1) for n in range(50)], label="$x_n$")
            ax.plot([0, 50], [0, 0], label="$x_0$")
            ax.plot( (1 + (1 - 4*eps*(eps - 5))**0.5) / (2*eps), eps, 'o', markersize=3, color='red')
            ax.plot([0, n_eps], [eps, eps], '--', color='red', alpha=0.7)
            ax.plot([ (1 + (1 - 4*eps*(eps - 5))**0.5) / (2*eps),  (1 + (1 - 4*eps*(eps - 5))**0.5) / (2*eps)], [0, eps], '--', color='red', alpha=0.7)
            ax.text( n_eps, 0.5 + eps, r"$n_{\epsilon} =$" + f"{n_eps}" )
            plt.legend()
            st.pyplot(fig)
        else:
            st.write("Let's consider")
            st.latex(r" x_n = \cos \left( \frac{1}{n} \right) ")
            eps = st.number_input("Select your `epsilon`", value=0.5, min_value=0.001, max_value=0.6)
            n_eps = 1 / np.arccos(1 - eps)
            fig, ax = plt.subplots(1, 1, figsize=(6, 3))
            ax.plot(np.linspace(0.1, 100, 200), np.cos(1/ np.linspace(0.1, 100, 200)) , label=r"$x_n$", color='green')
            ax.plot([1, 100], [1, 1], label=r"$x_0 = 1$", color='blue')
            ax.plot(n_eps, 1-eps, 'o', color='green', markersize=3, alpha=0.5)
            ax.plot([n_eps, n_eps], [0, 1-eps], '--', color='red', alpha=0.6)
            ax.text(n_eps + 1, 0.6, r'$n_{\epsilon}=$' + f"{int(1+n_eps)}")
            ax.set_ylim([0, 1.1])
            plt.legend()
            st.pyplot(fig)

    c1, c2 = st.columns([3, 2])
    with c1:
        st.write("#### Definition")
        st.write(r"Firstly, we introduce the **epsilon–delta** definition for convergence. A sequence $\lbrace x_n \rbrace$ is said to **converge** to $x_0$ if:")
        st.latex(r"\forall \epsilon > 0, \exists n_{\epsilon} \in \mathbb{N} \text{ such that } \vert x_n - x_0 \vert < \epsilon, \qquad \forall n > n_{\epsilon}")
        st.write("This means:")
        st.latex(r"\lim_{n \to \infty} x_n = x_0")

        st.write("#### 📌 Properties of Convergent Sequences")
        st.write(r"If sequences $(a_n), (b_n), (c_n)$ converge to $a, b, c$ respectively, then:")

        st.markdown("- 📎 **Sum and Difference**:")
        st.latex(r"\lim_{n \to \infty} (a_n \pm b_n) = a \pm b")

        st.markdown("- 📎 **Product**:")
        st.latex(r"\lim_{n \to \infty} (a_n \cdot b_n) = a \cdot b")

        st.write(r"- 📎 **Quotient**")
        st.latex(r"\lim_{n \to \infty} \left( \frac{a_n}{b_n} \right) = \frac{a}{b} \qquad \text{if } b \neq 0 ")

        st.markdown("- 📎 **Inequality Preservation**:")
        st.latex(r" (a_n \leq b_n \qquad \forall n) \quad \Rightarrow \quad a \leq b")

        st.markdown("""
        - 📎 **Squeeze (Sandwich) Theorem**:
        """)
        st.latex(r"\text{If } a_n \leq b_n \leq c_n \text{ and } \lim a_n = \lim c_n = L, \text{ then } \lim b_n = L") 
    with c2:
        get_sims()

def integration():
    #=======================================================================
    def curves_and_y_axes_plot():
        st.write("Let's consider")
        st.latex(r" A = \left\lbrace (x, y): e^{-x} \leq y < 1 \qquad \forall x \in \left[ 0, 1 \right] \right\rbrace ")        
        # Generate chart
        x = np.linspace(0, 1, 400)
        # Define curves
        y_lower = np.exp(-x)  # e^{-x}
        y_upper = np.ones_like(x)  # y = 1
        # Create the plot
        fig = plt.figure(figsize=(5, 5), dpi=80)
        plt.plot(x, y_lower, label=r"$y = e^{-x}$", color="blue")
        plt.plot(x, y_upper, label=r"$y = 1$", color="red")
        plt.fill_between(x, y_lower, y_upper, where=(y_lower < y_upper), color="skyblue", alpha=0.5)
        plt.legend(fontsize=16)
        plt.grid(True)
        _, c, _ = st.columns([1,3,1])
        with c: st.pyplot(fig, clear_figure=False)
        st.write("----------")
        st.write("#### Proof")
        st.write("We have")
        st.latex(r" \begin{array}{ccl} S_A = \displaystyle \iint_A dx dy &=& \displaystyle \int_0^1 \int_{e^{-x}}^1 dy dx \\ &=& \displaystyle \int_0^1 (1 - e^{-x}) dx \\  &=& 1 - \left( 1-e^{-1} \right) &=& e^{-1} \end{array} ")

    def curves_and_x_axes_plot():
        st.write("Let's consider")
        st.latex(r" A = \left\lbrace (x, y): 0 < x < \sqrt{y} \qquad \forall y \in \left[ 0, 1 \right] \right\rbrace ")
        y = np.linspace(0, 1, 500)
        # Define x bounds for the region
        x_lower = np.zeros_like(y)
        x_upper = np.sqrt(y)
        # Create the plot
        fig = plt.figure(figsize=(6, 6))
        plt.plot([0,0], [0, 1], label=r"$x=0$", color="blue")
        plt.plot(x_upper, y, label=r"$x=\sqrt{y}$", color="darkblue")
        plt.plot([0,1], [1, 1], label=r"$y=1$", color="cyan")
        plt.fill_betweenx(y, x_lower, x_upper, color="skyblue", alpha=0.5)
        # Axes settings
        plt.xlim(-0.1, 1.1)
        plt.ylim(-0.1, 1.1)
        plt.legend(loc='lower right', fontsize=12)
        plt.grid(True)
        _, c, _ = st.columns([1,3,1])
        with c: st.pyplot(fig)
        st.write("-----------")
        st.write("We have")
        st.latex(r" \begin{array}{ccl} S_A &=& \displaystyle \int_0^1 \int_{0}^{\sqrt{y}} dx dy &=& \displaystyle \int_0^1 \sqrt{y} dy &=& \dfrac{2}{3} \end{array} ")

    def deux_curves_plot():
        st.write("Let's consider")
        st.latex(r" A = \left\lbrace (x, y): x^2 < y < \dfrac{1}{x} \qquad \forall x \in \left[ \frac{1}{2}, 1 \right] \right\rbrace ")
        x = np.linspace(0.5, 1, 500)
        y_lower = x**2
        y_upper = 1/x
        fig = plt.figure(figsize=(6, 6))
        plt.fill_between(x, y_lower, y_upper, color='skyblue', alpha=0.5)
        plt.plot(x, y_lower, 'b', label=r'$y = x^2$')
        plt.plot(x, y_upper, 'r', label=r'$y = 1/x$')
        plt.legend()
        plt.grid(True)
        plt.axis('equal')
        _, c, _ = st.columns([1,3,1])
        with c: st.pyplot(fig)
        st.write("--------")
        st.write("We have")
        st.latex(r" \begin{array}{ccl}  S_A &=& \displaystyle \int_{1/2}^1 \int_{x^2}^{1/x} dydx &=& \displaystyle \int_{1/2}^1 \left( \dfrac{1}{x} - x^2 \right) dx &=& \ln 2 - \dfrac{7}{24} \end{array}")

    def triangle_plot():
        st.write("Let's consider")
        st.latex(r" A = \left\lbrace (x, y): x - 2y \leq 0 \, ; \, 2x + y \leq 5 \, ; \, y - 3x \geq 0 \right\rbrace ")
        triangle_vertices = [(2, 1), (0, 0), (1, 3)]
        x_coords, y_coords = zip(*triangle_vertices)
        x_coords += (x_coords[0],)
        y_coords += (y_coords[0],)
        fig = plt.figure(figsize=(6, 6))
        plt.fill(x_coords, y_coords, color='skyblue', alpha=0.5, label='Triangle region')
        x_line = range(-1, 4)
        plt.plot(x_line, [xi/2 for xi in x_line], 'g--', label='x - 2y = 0')
        plt.plot(x_line, [5 - 2*xi for xi in x_line], 'r--', label='2x + y = 5')
        plt.plot(x_line, [3*xi for xi in x_line], 'b--', label='y - 3x = 0')
        for (xv, yv) in triangle_vertices:
            plt.plot(xv, yv, 'ko')
            plt.text(xv + 0.1, yv + 0.1, f'({xv}, {yv})')
        plt.grid(True)
        plt.legend()
        plt.axis('equal')
        _, c, _ = st.columns([1,3,1])
        with c: st.pyplot(fig)
        st.write("--------------")
        st.write(r"The area $A$ can be rewritten as $B \backslash C$, where")
        st.latex(r" \begin{array}{ccl} B &=& \left\lbrace (x, y): \frac{x}{2} \leq y \leq 5-2x, \, \forall x \in [0, 2] \right\rbrace \\ C &=& \left\lbrace (x, y): \frac{y}{3} \leq x \leq \frac{5-y}{2}, \, \forall y \in [0, 5] \right\rbrace \end{array} ")
        st.write("Therefore,")
        st.latex(r" \begin{array}{ccl} S_A &=& S_B - S_C \\ &=& \displaystyle \int_0^2 \left( 5-2x-\frac{x}{2} \right)dx - \int_0^5 \left( \frac{5-y}{2} - \frac{y}{3} \right) dy \\  &=& \quad \left. \left( 5x - \dfrac{5x^2}{4} \right)\right\vert_0^2 \quad - \quad \left. \left( \dfrac{5y}{2} - \dfrac{5x^2}{6} \right)\right\vert_0^5 &=& \dfrac{35}{12} \end{array} ")

    def parallelogram_plot():
        st.write("Let's consider")
        st.latex(r" A = \left\lbrace (x, y): 1 \leq 2x + y \leq 3 \, ; \, -1 \leq x + y \leq 1 \right\rbrace ")
        vertices = [(2, -3), (0, 1), (-1, 2), (1, -2)]
        polygon = vertices + [vertices[0]]
        x_coords, y_coords = zip(*polygon)
        fig = plt.figure(figsize=(6, 6))
        plt.plot(x_coords, y_coords, 'b-o', label='Parallelogram')
        x_vals = range(-2, 3)
        plt.plot(x_vals, [1 - 2*x for x in x_vals], 'g--', label=r'$2x + y = 1$')
        plt.plot(x_vals, [3 - 2*x for x in x_vals], 'g--', label=r'$2x + y = 3$')
        plt.plot(x_vals, [-1 - x for x in x_vals], 'r--', label=r'$x + y = -1$')
        plt.plot(x_vals, [1 - x for x in x_vals], 'r--', label=r'$x + y = 1$')
        plt.grid(True)
        plt.axis('equal')
        plt.legend()
        _, c, _ = st.columns([1,3,1])
        with c: st.pyplot(fig)
        st.write("---------")
        st.write("By transformation")
        st.latex(r" u = 2x + y \qquad v = x + y \quad \Rightarrow \quad \left( \begin{array}{c} u \\ v \end{array} \right) = T \left( \begin{array}{c} x \\ y \end{array} \right) ")
        st.write(r"where $ T = \left[ \begin{array}{cc} 2 & 1 \\ 1 & 1 \end{array} \right] $. Then")
        st.latex(r" 1 \leq u \leq 3 \qquad -1 \leq v \leq 1 ")
        st.write("and")
        st.latex(r"\begin{array}{ccl} S_A = \displaystyle \iint_{A} dx dy &=& \displaystyle \dfrac{1}{\det T} \int_1^3 \int_{-1}^1 dv du &=& 4 \end{array}")        

    def parabolla_plot():
        st.write("Compute the volumn bounded by")
        st.latex(r" \left\lbrace (x,y,z) : \frac{1}{2} \leq z \leq x^2 + y^2, \, x^2 + y^2 \leq 1 \right\rbrace ")
        # Domain
        theta = np.linspace(0, 2 * np.pi, 70)
        r = np.linspace(0, 1, 50)
        R, T = np.meshgrid(r, theta)
        X = R * np.cos(T)
        Y = R * np.sin(T)
        # Upper surface (paraboloid)
        Z_upper = X**2 + Y**2
        # Base plane
        Z_base = np.full_like(Z_upper, 0.5)
        fig = go.Figure()
        # Base surface, blue, semi-transparent
        fig.add_surface(x=X, y=Y, z=Z_base, showscale=False, opacity=0.5, surfacecolor=np.zeros_like(Z_base), 
                        colorscale=[[0, '#1FB8CD'],[1, '#1FB8CD']])
        # Upper surface, red, semi-transparent
        fig.add_surface(x=X, y=Y, z=Z_upper, showscale=False, opacity=0.5, surfacecolor=np.ones_like(Z_upper), 
                        colorscale=[[0, '#DB4545'],[1, '#DB4545']])
        st.plotly_chart(fig)
        st.write("-----------")
        st.write("By `polar coordinate`, we have")
        st.latex(r" \begin{array}{ccl} V_A &=& \displaystyle \iint_{ \frac{1}{2} \leq x^2 + y^2 \leq 1 } \int_{1/2}^{x^2+y^2} dz \, dy \, dx \\ &=& \displaystyle \iint_{(r,\phi)}\int_{1/2}^{r^2} r dz \, dr \, d\phi \\ &=& \displaystyle \int_0^{2\pi} \int_{1/\sqrt{2}}^1 \left( r^2 - \frac{1}{2} \right)r \, dr \, d\phi &=& \dfrac{\pi}{8} \end{array} ")

    def hyperbolla_plot():
        st.write("Compute the volumn bounded by")
        st.latex(r" \left\lbrace (x,y,z) : \sqrt{1 + x^2 + y^2} \leq z \leq 2, \, 0 \leq x^2 + y^2 \leq 1 \right\rbrace ")
        # Create grid in xy-plane over the unit disk
        n = 200
        x = np.linspace(-1, 1, n)
        y = np.linspace(-1, 1, n)
        X, Y = np.meshgrid(x, y)
        R = np.sqrt(X**2 + Y**2)
        # Mask to keep points inside the unit disk
        mask = R <= 1 
        # Lower surface: z = sqrt(1 + x^2 + y^2)
        Z_lower = np.sqrt(1 + X**2 + Y**2)
        Z_lower[~mask] = np.nan  # Mask outside disk for plotting 
        # Upper surface: z = 2 (constant)
        Z_upper = np.full_like(X, 2)
        Z_upper[~mask] = np.nan  # Mask outside disk 
        # Create surface trace for lower surface
        surface_lower = go.Surface(
            x=X, y=Y, z=Z_lower,
            colorscale='Viridis',
            opacity=0.9,
            name='Lower Surface',
            showscale=False
        )

        # Create surface trace for upper surface
        surface_upper = go.Surface(
            x=X, y=Y, z=Z_upper,
            colorscale='Reds',
            opacity=0.5,
            name='Upper Surface',
            showscale=False
        )
        fig = go.Figure(data=[surface_lower, surface_upper])
        st.plotly_chart(fig)
        st.write("By `polar coordinate`, we have")
        st.latex(r" \begin{array}{ccl}  V &=& \displaystyle \int_{0}^{2\pi} \int_0^1 \int_{\sqrt{1 + r^2}}^2 r \, dz \, dr \, d \phi \\  &=& \displaystyle 2 \pi \cdot \int_0^1 \left( 2-\sqrt{1+r^2} \right)\cdot rdr \qquad u:=1+r^2 \\ &=& \displaystyle 2 \pi \cdot \int_1^2 \left( 2-\sqrt{u} \right) \cdot \left( \frac{1}{2}du \right) \\ &=& \dfrac{2\pi}{3} \left( 4 - 2\sqrt{2} \right) \end{array} ")

    def elliptic_plot():
        st.write("Compute the volumn bounded by")
        st.latex(r" \left\lbrace (x,y,z) : 0 \leq z \leq 5 \sqrt{1 - \frac{x^2}{9} - \frac{y^2}{16}} \right\rbrace ")
        
    def simulate_integ(app, example):
        if app == "Area bounded by curves":
            if example == "curves and y-axes":
                curves_and_y_axes_plot()
            elif example == "curves and x-axes":
                curves_and_x_axes_plot()
            elif example == "2 curves": 
                deux_curves_plot()
            elif example == "parallelogram":
                parallelogram_plot()
            elif example == "triangle":
                triangle_plot()

        elif app == "Volume bounded by surfaces":
            if example == "parabolla":
                parabolla_plot()
            elif example == "hyperbolla":
                hyperbolla_plot()
            elif example == "elliptic": 
                elliptic_plot()
            elif example == "semispheres":
                st.write("Compute the volumn bounded by")
                st.latex(r" \left\lbrace (x,y,z) : 0 \leq z \leq \sqrt{1 - x^2 + y^2} \right\rbrace ")
                
        elif app == "Moments and Centroid":
            if example == "circle-shape 2D":
                pass
            elif example == "circle-shape 3D":
                pass
            elif example == "more complexity":
                pass
    # =======================================================================
    def general_latex():
        st.markdown("#### Fubini's theorem")
        st.latex(r"\iint_{[a,b]\times[c,d]} f(x,y)\,dx\,dy = \int_a^b\Big(\int_c^d f(x,y)\,dy\Big)dx = \int_c^d\Big(\int_a^b f(x,y)\,dx\Big)dy ")
        st.markdown("#### Leibniz rule")
        st.latex(r"\frac{d}{dx}\int_{u(x)}^{v(x)} f(x,t)\,dt = \int_{u(x)}^{v(x)} \frac{\partial f}{\partial x}(x,t)\,dt + f(x,v(x))v'(x)-f(x,u(x))u'(x) ")
        st.markdown("#### Other application")        
    def integ_app_latex(app):
        if app == "Area bounded by curves":
            st.write("#### Between two curves")
            st.write(r"For $y=f(x)$ `upper curve` and $y=g(x)$ (`lower curve`), over $x \in [a, b]$, then")
            st.latex(r"\text{Area} = \int_a^b |f(x) - g(x)|\, dx")
        elif app == "Volume bounded by surfaces":
            st.write("#### Between two surfaces")
            st.write(r"For $z=f(x, y)$ `upper surface` and $z=g(x, y)$ (`lower surface`), over $(x, y) \in [a, b] \times [c, d]$, then")
            st.latex(r"\text{Area} = \iint_{[a, b] \times [c, d]} \left( f(x, y) - g(x, y) \right) dx dy ")
        else:
            st.write("#### Centroids")
            st.write("This is also the first moment of an object, which defined by")
            st.latex(r" \left( \frac{ \displaystyle \int_A x dA }{V_A}, \dfrac{ \displaystyle \int_A y dA }{V_A}, \dfrac{ \displaystyle \int_A z dA }{V_A} \right) ")
            st.write(r"#### Moment order $k$")
            st.latex(r" \left( \frac{ \displaystyle \int_A x^k dA }{V_A}, \dfrac{ \displaystyle \int_A y^k dA }{V_A}, \dfrac{ \displaystyle \int_A z^k dA }{V_A} \right) ")             
    # ========================= MAIN ==========================================
    c1, c2 = st.columns([3, 2])
    app_dict = {
        "Area bounded by curves": ["curves and y-axes", "curves and x-axes", "2 curves", "parallelogram", "triangle"],
        "Volume bounded by surfaces": ["parabolla", "hyperbolla", "elliptic", "semispheres"],
        "Moments and Centroid": ["circle-shape 2D", "circle-shape 3D", "more complexity"]
    }
    with c1:
        general_latex()
        app = st.selectbox("Select the `application`", list(app_dict.keys()))
        integ_app_latex(app)
    with c2:
        st.write(f"#### Simulation for {app}")
        c21, c22 = st.columns(2)
        with c21: 
            wanna_sim = st.selectbox("Wanna simulations?", ["Yes", "No"], key="sim_toggle_limit")
        if wanna_sim == "Yes":
            with c22: example = st.selectbox("Select examples", app_dict[app])            
            simulate_integ(app, example)

def limitation():
    def opening_text():
        st.markdown("### 🔍 Key Concepts in Limitation")    
        st.markdown("**1. Definitions:**")
        st.latex(r"\lim_{x \to a} f(x) = L")
        st.write("--------")        
    # =================== SIMULATIONS =============================
    def theorem_simulate(theo):
        def get_sandwich_sims():
            c1, c2 = st.columns(2)
            with c1: n_min = st.number_input("n_min", value=30, min_value=10, max_value=100)
            with c2: n_max = st.number_input("n_max", value=n_min + 50, min_value=n_min + 1, max_value=int(1e6))
            
            st.write("In this example, we have")
            st.latex(r"x_n = \dfrac{\sin n}{n^2} \qquad y_n = \dfrac{1}{n}")
            st.latex(r"0 \leq \vert x_n \vert \leq y_n \qquad \forall n \in \mathbb{N}")            
            serial_df = pd.DataFrame({
                "n": list(range(n_min, n_max + 1)),
                "x_n": [np.sin(t) / t**2 for t in range(n_min, n_max + 1)],
                "y_n": [1 / t for t in range(n_min, n_max + 1)],
                "z_n": [0 for _ in range(n_min, n_max + 1)]
            })
            fig = px.line(serial_df, x="n", y=["x_n", "y_n", "z_n"])
            st.plotly_chart(fig)
        def get_LHopital_sims():
            st.write("In this example, we consider")
            st.latex(r" c = 0 \qquad f(x) = \sin x \qquad \ g(x) = 0 ")
            st.write("By L'Hopital, we have")
            st.latex(r" \lim_{x \to c} \dfrac{\sin x}{x} = \lim_{x \to 0} \dfrac{\cos x}{1} = 1 ")
            n_peaks = st.selectbox("Select number of `n-pi`", [3, 6, 9])
            x = np.arange(-n_peaks*np.pi, n_peaks*np.pi, 0.1)
            y = np.sin(x) / x
            lim_df = pd.DataFrame({
                'x': x,
                'y': y
            })
            fig = px.line(lim_df, x="x", y=y)
            st.plotly_chart(fig)
        # ======================================================================================= 
        if theo == "Sandwich Theorem":
            get_sandwich_sims()
        elif theo == "L'Hôpital's Rule":
            get_LHopital_sims()
    def get_latex(theo):
        def get_sandwich_text():
            st.write(r"For 3 sequences $a_n, b_n, c_n$, if there exists $n_0$ such that")
            st.latex(r"a_n \leq b_n \leq c_n \qquad \forall n \geq n_0")
            st.write("and")
            st.latex(r"\lim_{n \to \infty} a_n = \lim_{n \to \infty} c_n = 0")
            st.write("Then")
            st.latex(r"\lim_{n \to \infty} b_n = 0") 
        def get_LHopital_text():
            st.write(r"Let $f, g: \mathbb{R} \to \mathbb{R}$ be differentiable functions. Suppose there exists $c \in \mathbb{R}$ such that")
            st.latex(r"f(c) = g(c) = 0 \quad \text{or} \quad f(c) = g(c) = \pm\infty.")
            st.write("Then")
            st.latex(r"\lim_{x \to c} \frac{f(x)}{g(x)} = \frac{f'(c)}{g'(c)}")
        if theo == "Sandwich Theorem":
            get_sandwich_text()
        elif theo == "L'Hôpital's Rule": 
            get_LHopital_text()
    # ======================================  main  ===========================================
    c1, c2 = st.columns([3, 2])
    with c1:
        opening_text()
        # Select theorem once
        theo = st.selectbox("Select a theorem", ["Sandwich Theorem", "L'Hôpital's Rule"])
        st.markdown("**2. Theorem Explanation:**") 
        get_latex(theo)
    # Simulation toggle
    with c2:
        wanna_sim = st.selectbox("Wanna simulations?", ["Yes", "No"], key="sim_toggle_limit")
        if wanna_sim == "Yes":
            theorem_simulate(theo)
                
def show_hand(category):
    if category == "Convergence":
        convergence()
    elif category == "Limitation":
        limitation()
    elif category == "Integration":
        integration()