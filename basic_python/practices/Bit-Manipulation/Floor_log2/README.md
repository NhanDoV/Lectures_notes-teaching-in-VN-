## Find Floor of log₂(n) in Python

This repository demonstrates different methods to compute the **floor value of log base 2** of a positive integer.  
That is, for a given number `n`, find the largest integer `k` such that `2^k ≤ n`.

---

## 📘 Overview

The script defines a class `find_floor_log2` containing three methods:

| Method | Description | Uses Built-in `math.log2`? | Concept Used |
|:--------|:-------------|:--------------------------:|:--------------|
| `naive_method(num)` | Uses Python’s built-in `math.log2()` function. | ✅ Yes | Logarithmic function |
| `without_using_log_directly(num)` | Computes by dividing the number by 2 iteratively. | ❌ No | Integer division |
| `using_bit_RightShift(num)` | Uses bitwise right shift operation to count powers of 2. | ❌ No | Bit manipulation |

---