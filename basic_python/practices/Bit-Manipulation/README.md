# 1. Bitwise Operators

#### Check in python
From terminal, active `python`
```bash
python
```
Then, type
```python
import description as d
d.bitwise_description()
```
You will receive sth like

    *---------*---------*-------------------*----------------------*-------------------*
    |    a    |    b    |     OR (a | b)    |      AND (a & b)     |     XOR (a ^ b)   | 
    *---------*---------*-------------------*----------------------*-------------------*   
    |    0    |    0    |         0         |           0          |         0         | 
    |    0    |    1    |         1         |           0          |         1         | 
    |    1    |    0    |         1         |           0          |         1         | 
    |    1    |    1    |         1         |           1          |         0         |
    *---------*---------*-------------------*----------------------*-------------------*

#### Example 1.1
Input: `a = 3, b = 5`
```shell
Output:
        (AND) a & b = 1
        (OR)  a | b = 7
        (XOR) a ^ b = 6
```

**Explaination**
##### Convert to binary

            5       -->     101
            3       -->     011
##### Bit-wise operators & convert to decimal

        (5 AND 3)   -->     001   -->     1
        (5 OR  3)   -->     111   -->     7
        (5 XOR 3)   -->     110   -->     6

#### Example 1.2.
Input: `a = 6, b = 4`
```shell
Output:
        (AND) a & b = 4
        (OR)  a | b = 6
        (XOR) a ^ b = 2
```

**Explaination**
##### Convert to binary

            6       -->     110
            4       -->     100
##### Bit-wise operators & convert to decimal

        (6 AND 4)   -->     100   -->     4
        (6 OR  4)   -->     110   -->     6
        (6 XOR 4)   -->     010   -->     2

# 2. Shift [left / right]

| Operators | Description |
|:---------:|:------------|
| LEFT SHIFT| Adding more 2 zero digits to the tail of the binary form; this equivalent to `a << b = a * pow(2, b)`
|RIGHT SHIFT| Shifts all bits of a to the right by b positions, discarding the rightmost bits. The leftmost bits depend on whether a is signed or unsigned. `a >> b = floor(a / pow(2, b) )` |

#### Example
- Input: `a = 7, b = 2`
```bash
Output:
        [LEFT SHIFT]       a << b = 28
        [RIGHT SHIFT]      a >> b =  1
```
**Explaination**

We have

           to binary            Left shift 2             to dec 
        7  --------->  111    ---------------> 111(00)  ------->  28  
                                               adding 00            

                                Right shift 2
                              ----------------> 001[11] ------->  1

# 3. Well-known usage
- Check if a number is even/odd: n & 1

- Multiply/divide by powers of 2: n << k (×2^k), n >> k (÷2^k)

- Check if a number is power of 2: (n & (n - 1)) == 0

- Count set bits (popcount), reverse bits, etc.