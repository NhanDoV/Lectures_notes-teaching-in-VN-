import numpy as np
import scipy.linalg as LA
import sympy as sy

#=============================================================================
# spanning vectors of the kernel of A
def ker_im(mat):
    """
        ======================================================
        Example:
        >> import sympy as sy
        >> A = [[1, 0, 1], [2, 1, 1], [-1, 1, -2]]
        >> ker_im(A)
            * spanning vectors of the kernel of matrix 
            [Matrix([
                    [-1],
                    [ 1],
                    [ 1]])]
            * spanning vectors of the image of matrix
            [Matrix([
                    [ 1],
                    [ 2],
                    [-1]]),
            Matrix([
                    [0],
                    [1],
                    [1]])]
            * Rank of your matrix:
            2
    """
    mat = sy.Matrix(mat)
    print("* spanning vectors of the kernel of matrix ")
    display(mat.nullspace())

    print("* spanning vectors of the image of matrix")
    display(mat.columnspace())

    print("* Rank of your matrix")
    display(mat.rank())

#=============================================================================
## Ma trận lũy linh
def check_nilpotent(matrix):
    """
        Một ma trận lũy linh M phải thỏa
            - ma trận vuông 
            - tồn tại một số nguyên N sao cho M^n = 0_{n x n} (0_{n x n} tức là ma trận 0 cấp n)
        Ví dụ
            A = [[0, 1], [0, 0]] là lũy linh vì A^2 = 0
        ====================================================================
        Tuy nhiên đôi lúc chúng ta không thể sử dụng
            while n > 0:
                if M^n == 0_{n x n}
        vì nó đéo tối ưu!
        ===================================================================
        Ta có một hệ quả từ ma trận lũy linh M 
            - giả sử n là cấp của ma trận vuông M
            - khi đó tất cả các trị riêng (eigenvalue) của nó đều bằng 0 (tức là 0 là nghiệm bội n) 
        ======================================================================
        >> res=check_nilpotent([[0, 1], [0, 0]])
            lũy linh
        >> res=check_nilpotent([[2, -1], [4, -2]])
            lũy linh
        >> res=check_nilpotent([[2, 4], [-1, -2]])
            lũy linh
        >> res=check_nilpotent([[2, 4], [0, -2]])
            vuông nhưng đéo lũy linh
        >> res=check_nilpotent([[2, 4, 0], [0, -2, 1]])
            đéo vuông nên đéo care
    """    
    M = np.array(matrix)
    n_col, n_row = M.shape
    if n_col == n_row:
        eigenvalues, eigenvectors = LA.eig(M)
        # Loại trừ trường hợp các giá trị được hiển thị dưới dạng 0.000000000002
        count_zeros = [x for x in eigenvalues if np.abs(x) < 1e-9]
        if len(count_zeros) == n_col:
            print("Lũy linh")
            return 1
        else:
            print("vuông nhưng đéo lũy linh")
            return 0
    else:
        print("đéo vuông nên đéo care")
        return 0
        
#=============================================================================
# Ma trận gọi là lũy đẳng
def check_idempotent(matrix):
    """
        Một ma trận gọi là lũy đẳng (idempotent) nếu
            - nó là ma trận vuông
            - khi nhân với chính nó, sẽ cho ra chính nó
        =====================================================================
        Example
        >> res=check_idempotent([[1,0],[0,1]]) 
            Lũy đẳng
        >> res=check_idempotent([[1,2], [2,1]])
            vuông nhưng đéo lũy đẳng
        >> res=check_idempotent([[3,-6], [1,-2]])
            Lũy đẳng
        >> res=check_idempotent([[3,1], [-6,-2]])
            Lũy đẳng
        >> res=check_idempotent([[1,2,1], [0,1,-2]])
            đéo vuông nên đéo care
    """
    M = np.array(matrix)
    n_col, n_row = M.shape
    if n_col == n_row:
        mat_2 = np.matmul(matrix, matrix)
        res = (mat_2 - matrix)
        if (np.abs(res) < 1e-9).all():
            print("Lũy đẳng")
            return 1
        else:
            print("vuông nhưng đéo lũy đẳng")
            return 0
    else:
        print("đéo vuông nên đéo care")
        return 0

#=============================================================================
# Check if a matrix is Orthogonal
def check_orthogonal(matrix, tol=1e-9):
    """
        Check whether a matrix is orthogonal.

        A matrix Q is orthogonal if Q^T Q = I.

        Example:
            >> check_orthogonal([[0, 1], [1, 0]])
                Orthogonal
            >> check_orthogonal([[1, 2], [3, 4]])
                Not orthogonal
    """
    M = np.array(matrix, dtype=float)
    if M.shape[0] != M.shape[1]:
        print("Not square → cannot be orthogonal")
        return 0

    I = np.eye(M.shape[0])
    diff = M.T @ M - I

    if np.all(np.abs(diff) < tol):
        print("Orthogonal")
        return 1
    else:
        print("Not orthogonal")
        return 0

#=============================================================================
# Check if a matrix is Positive Definite
def check_positive_definite(matrix):
    """
        Check if a matrix is symmetric positive definite (SPD).

        Methods:
            A matrix is SPD if:
                - It is symmetric
                - All eigenvalues > 0

        Example:
            >> check_positive_definite([[2, -1], [-1, 2]])
                Positive definite
            >> check_positive_definite([[0, 1], [1, 0]])
                Not positive definite
    """
    M = np.array(matrix, dtype=float)

    if not np.allclose(M, M.T):
        print("Not symmetric → cannot be positive definite")
        return 0

    eigvals = np.linalg.eigvals(M)
    if np.all(eigvals > 1e-12):
        print("Positive definite")
        return 1
    else:
        print("Not positive definite")
        return 0

#=============================================================================
# Compute the Rank of a Matrix
def matrix_rank(matrix):
    """
        Compute the rank of a matrix using SVD.

        Example:
            >> matrix_rank([[1, 2], [2, 4]])
                1
    """
    M = np.array(matrix, dtype=float)
    r = np.linalg.matrix_rank(M)
    print(f"Rank = {r}")
    return r

#=============================================================================
# Projection Matrix onto Column Space
def projection_matrix(A):
    """
        Compute the projection matrix onto the column space of A.

        Example:
            >> projection_matrix([[1,0],[1,1]])
    """
    A = np.array(A, dtype=float)
    P = A @ np.linalg.inv(A.T @ A) @ A.T
    return P
