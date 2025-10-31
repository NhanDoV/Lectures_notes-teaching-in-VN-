# Multiply Two Integers Using Bitwise Operations

This repository demonstrates **different ways to multiply two positive integers** in Python — from the simplest built-in operator to **pure bit manipulation techniques**.  
The script includes various approaches to help understand how multiplication works at the **bitwise level**.

---

## 📘 Overview

The class `Multiply_nums` implements multiple methods to compute the product of two integers, including illustrative examples for decomposing numbers into powers of 2.

| Method | Description | Uses Multiplication Symbol `*`? | Concept Used |
|:--------|:-------------|:--------------------------------:|:--------------|
| `naive_approach(num1, num2)` | Standard built-in multiplication. | ✅ Yes | Direct arithmetic |
| `using_bit_manipulation(num1, num2)` | Pure bitwise method using shifts and addition only. | ❌ No | Bit manipulation |
| `using_bit_manipulation_v1(num1, num2)` | Step-by-step decomposition method using powers of 2. | ❌ No | Binary decomposition |
| `multiply_7_using_bit(num)` | Optimized trick for multiplying by 7. | ❌ No | Shift and subtract |
| `multiply_13_using_bit(num)` | Optimized trick for multiplying by 13. | ❌ No | Multiple shifts and additions |
| `num_decay_by_power_of_2(num)` | Decomposes a number into powers of 2 with binary indicator list. | ❌ No | Bit decomposition |

---

## 🧩 Code Example

```python
from multiply_nums import Multiply_nums

obj = Multiply_nums()

# 1️⃣ Standard multiplication
print(obj.naive_approach(7, 13))                 # Output: 91

# 2️⃣ Bitwise multiplication
print(obj.using_bit_manipulation(7, 13))         # Output: 91

# 3️⃣ Decomposition method
print(obj.using_bit_manipulation_v1(7, 13))      # Output: 91

# 4️⃣ Multiplying by constants using bit tricks
print(obj.multiply_7_using_bit(9))               # Output: 63
print(obj.multiply_13_using_bit(5))              # Output: 65

# 5️⃣ Decompose number into powers of 2
signs, degs = obj.num_decay_by_power_of_2(13)
print(signs)    # [1, 1, 0, 1]
print(degs)     # [3, 2, 1, 0]