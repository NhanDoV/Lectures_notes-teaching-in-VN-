## Description
### Problem

This demonstrates different methods to **swap two numbers** in Python **without using a temporary variable**.  
It includes three approaches: the naïve approach (Pythonic), arithmetic operations, and bitwise XOR.

---

## 📘 Overview

The script defines a class `swap_number` containing three methods:

| Method | Description | Uses Temporary Variable? | Safe for Negative Numbers? |
|:--------|:-------------|:--------------------------|:-----------------------------|
| `navie_approach(a, b)` | Swaps values using Python’s tuple unpacking. | ✅ Yes (implicitly) | ✅ Yes |
| `basic_method(a, b)` | Swaps using addition and subtraction. | ❌ No | ⚠️ Works but may overflow in other languages |
| `using_XOR(a, b)` | Swaps using bitwise XOR operation. | ❌ No | ✅ Yes |