import numpy as np

def find_integer_a_plus_b(sum_denom: int) -> list[int]:
    """
    Args:
        sum_denom (int): the target in the problem 
                1       1          1
               ---  +  ---  =  ----------
                a       b      sum_denom 
    Returns:
        list[int]: All unique solutions of a + b
    """
    res = []
    for a in range(1, sum_denom + 1):
        for b in range(1, sum_denom + 1):
            if (1 / a) + (1 / b) == (1 / sum_denom):
                print(f"a: {a} \t b: {b} \t a + b = {a + b}")
                res.append(a + b)
    return list(set(res))

def k_th_digit_from_the_right_a_power(a_base: int, k_index: int, k_th_digit: int) -> int:
    """
    Args: Find the minimal n such that a^n has the k-th digit from the right is a certain number
        a_base (int): base of the power in a^n
        k_index (int): index at k-th position
        k_th_digit (int): value at k-th digit 
    Returns:
        int: the minimum of n such that the description         
    """
    for n in range(22):
        A = a_base ** n
        digit = (A // 10**(k_index - 1)) % 10
        if digit == k_th_digit:
            return n
    return -1  # not found

if __name__ == "__main__":
    print("1. Find integers a, b such that 1/a + 1/b = 1/denom")
    denom = int(input("Input your denominator"))
    result1 = find_integer_a_plus_b(denom)
    print("Unique values of a + b:", result1)
    
    print("2. Find the minimal value of n such that a^n has the k-th digit from the right is K")
    a = int(input(""))
    result2 = k_th_digit_from_the_right_a_power(2, 3, 5)
    print("Smallest n such that 2^n has 3rd digit from right = 5:", result2)