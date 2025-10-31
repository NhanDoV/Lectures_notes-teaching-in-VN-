## Description
### Problem 
Given two integers num1 and num2, return the sum of the two integers.

------

#### Example 1:
- Input: `num1 = 12, num2 = 5`
- Output: `17`
- Explanation: num1 is 12, num2 is 5, and their sum is 12 + 5 = 17, so 17 is returned.

#### Example 2:
- Input: `num1 = -10, num2 = 4`
- Output: `-6`
- Explanation: num1 + num2 = -6, so -6 is returned.

------

### Behind the scence (for positive integers)
#### EX 1. 
- Input `a = 5,     b = 2`

        Initially,
                    a   :=     101  ,         b   :=     010 

        iter 1. (b = 2 != 0)    
                    a  &  b     =      000
                    carry       =      (a & b)  <<  1     =     0
                    a           =      XOR(a , b)         =    111  (7) 
                    b           =       carry             =    000  
        
        iter 2. break since b == 0
        
now `a = 111` meant `sum = 7`

#### EX 2. 
- Input `a = 5,     b = 3`

        Initially,
                    a   :=     101  ,         b   :=     011

        iter 1. (b = 3 != 0)
                    a  &  b     =      001
                    carry       =      (a & b)  <<  1     =    010  (2) 
                    a           =      XOR(a , b)         =    110  (6) 
                    b           =       carry             =    010  (2)

        iter 2. (b = 2 != 0)
                    a  &  b     =      010
                    carry       =      (a & b)  <<  1     =    100  (4) 
                    a           =      XOR(a , b)         =    100  (4) 
                    b           =       carry             =    100  (4)

        iter 3. (b = 4 != 0)
                    a  &  b     =      100
                    carry       =      (a & b)  <<  1     =   1000  (8) 
                    a           =      XOR(a , b)         =    000  (0) 
                    b           =       carry             =   1000  (8)

        iter 4. (b = 8 != 0)
                    a  &  b     =      0000
                    carry       =      (a & b)  <<  1     =   0000  (0) 
                    a           =      XOR(a , b)         =   1000  (8) 
                    b           =       carry             =   0000  (0)

Hence, `sum = 8`
