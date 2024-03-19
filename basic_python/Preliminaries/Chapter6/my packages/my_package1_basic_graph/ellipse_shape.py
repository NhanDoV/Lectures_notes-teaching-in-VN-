import matplotlib.pyplot as plt
import numpy as np

def ellips_2d(radius, centers, style = '-', col = 'red'):
    """
        This function used to draw an ellipse with 2 input arguments:
            ========================================================
            radius (list) = [r1, r2] : radius of your ellipse
            centers = (x0, y0) : center coordinates of the ellipse
    """
    pi = np.pi
    t = np.linspace(-pi, pi, 100)
    x0, y0 = centers
    r1, r2 = radius
    x = x0 + r1*np.cos(t)
    y = y0 + r2*np.sin(t)
    plt.plot(x0, y0, 'ok')
    plt.plot(x, y, linestyle = style, color = 'blue')

def cir_in_cir(R, r, centers, n, style = '-', col = 'blue'):
    """
    =================================================
        input arguments:
            R (list of float) : radius of the outside circle
            r (float) : radius of the satellite circle
            n (int) : numbers of the satellite in the orbit
            centers (list of numbers): center coordinate
   =================================================
       This function is used to simulate the orbit which many circles lies on another circle on the same ellipse 
    """
    pi = np.pi
    t = np.linspace(0, 2*pi, n)
    R1, R2 = R
    a, b = centers
    x = a + R1*np.cos(t)
    y = b + R2*np.sin(t)
    plt.figure(figsize = (int(0.5*n), n))
    for k in range(n):
        ellips_2d( [r, r], (x[k], y[k]) , style = style, col = col)
    ellips_2d(R, centers, style = '--', col = col)
    plt.axis("off")
    
def solar_systems(N, R, centers = [0, 0], n=1, style = '-', col = 'blue'):
    """
        This function simulate the Solar systems
    """
    pi = np.pi
    r = abs(N - 3)/(3*N)
    t = np.linspace(0, 2*pi, 100)
    x = np.cos(t); y = np.sin(t) 
    plt.figure(figsize = (R[0], R[1]))
    plt.axis([-R[0]-3, R[0]+3, -R[1]-3, R[1]+3])
    plt.plot(x, y, color = "red")
    plt.fill_between(x, y, color="red")
    for k in range(1, N + 1):
        R1 = R[0]/N*(k+1)
        R2 = R[1]/N*(k+1)
        rs = np.random.uniform(r, 3*r)
        ys = (-1)**k*(N + 2 - k)
        ts = np.linspace(0, 2*pi, 100)
        xss = rs*np.cos(ts)
        yss = ys + rs*np.sin(ts)
        plt.plot(0, ys, '*k')
        plt.plot(xss, yss)
        ellips_2d([R1, R2], centers, style = '--', col = 'red')
    plt.plot(centers, "ro")

def vector_plot(x0, y0, x1, y1, clv, hL = 0.2, hW = 0.04):
    """
    This function is used to plot the vector/arrow though 2 points
    Args: 
        - (x0, y0) and (x1, y1) : coordinates of arrow base
        - clv (str): color of vector
        - HL, HW: head_length & head_width of vector/ arrow
    """
    ## length of arrow along x & y direction
    dx = x1 - x0
    dy = y1 - y0
    # plot the starting_point of vector
    plt.plot(x0, y0, clv, marker = 'o', label = 'from (%s, %s) to (%s, %s)'%(x0, y0, x1, y1))
    # plot the vector / arrow
    plt.arrow(x0, y0, dx, dy, color = clv, 
              head_length = hL, head_width = hW, 
              length_includes_head = False)