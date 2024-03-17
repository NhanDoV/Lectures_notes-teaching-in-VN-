import numpy as np
import scipy.linalg as la
import sympy as sy
    
A = sy.Matrix([[1, 0, 1], [2, 1, 1], [-1, 1, -2]])

# spanning vectors of the kernel of A 
def ker_im(mat):
    print("# spanning vectors of the kernel of matrix ")
    display(mat.nullspace())

    print("# spanning vectors of the image of matrix")
    display(mat.columnspace())

    print("Rank of your matrix")
    display(mat.rank())

# To be continued soon!