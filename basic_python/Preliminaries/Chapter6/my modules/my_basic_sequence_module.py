## 1. Cap so cong! [Arithmetic_progression]
def arith_progr(x0, d, n): 
    """
        This function generate an arithmetic progression with
            =============================================================   
            Inputs:
                x0 (numeric): an initial values in the sequence
                d (numeric): the common difference in the sequence
                n (int) : the sequence_length or the numbers of elements in the sequence
            ---------------------------------------------------------------
            Output / returns:
                a sequence of the arithmetic sequence with initial value (x0) and a common difference (d)
    """
    seq = []
    while(len(seq) < n):
        seq.append(x0)
        x0 = x0 + d;
    return seq

## 2. Harmonic sequence
def harmc_seq(x0, d, n):
    """
        This function generate a harmonic progression with an initial denominator (x0 : a non-zero) and a common diff (d)
        ==========================================================
        Inputs args:
            defined similarly in the function arith_progr in this module
        ----------------------------------------------------------
        Output / returns:
            A harmonic sequence
    """
    seq = []
    if x0 != 0:
        while(len(seq) < n):
            seq.append(1/x0)
            x0 = x0 + d
    else:
        raise ZeroDivisionError("The initial denominator x0 must not be zero")
    return seq

## 3. Cap so nhan [Geometric progression]
def geom_seq(x0, r, n):
    """
        This function is used to generate a geometric series / sequence
        ======================================================
        Input args:
            x0 (numeric): initial value
            r (numeric) : common ratio
            n (int) : length of the sequence
        -----------------------------------------------------
        Output / returns:
            The geometric progression with: length (n), initial value (x0) and common ratio (r)
    """
    seq = []
    while(len(seq) < n):
        seq.append(x0)
        x0 = r*x0
    return seq

## 4. Fibonacci sequence
def fibo_seq(n, x0, x1):
    """
        This function generate a Fibonacci sequences length n.
        ===============================================================
        Input: 
            n (int) is the length of sequence
            x0, x1 (int): the first 2 initial values in the sequence
        --------------------------------------------------------------------------
        Output: a Fibonacci sequence of length n and the first 2 initial value x0, x1
    """
    seq = [x0]
    a, b = x0, x1
    while(len(seq) < n):
        seq.append(b)
        a, b = b, a+b
    return seq

## 5. Syaracuse sequence
def syracuse(n):
    """
        This sequences is generated from the Collatz conjecture problem; or Syracuse problem
        ------------------------------------------
        Input parameters:
            n (int) : length of the sequence
        ==========================================
        Output / returns:
            a Syracuse sequence
    """
    seq = []
    u = n
    while u != 1:
        seq.append(u)
        u = u // 2 if u % 2 == 0 else 3*u+1
    seq.append(1)
    return seq
syracuse(10)