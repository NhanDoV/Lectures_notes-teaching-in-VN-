class adding_nums:
    def naive_approach(self, num1: int, num2: int) -> int:
        return num1 + num2

    def plus_by_bitwise(num1 :int, num2: int) -> int:
        """
            Only work for positive integers
        """
        while num2 != 0:
            carry = (num1 & num2) << 1  # carry:
            num1  =  num1 ^ num2         # XOR
            num2  =  carry               #

        return num1

    def using_bit_manipulation(self, num1: int, num2: int) -> int:
        """
            we use bit-mask in this case for the negative integers
        """
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        while num2 != 0:
            num1, num2 = (num1 ^ num2) & MASK, ((num1 & num2) << 1) & MASK
        return num1 if num1 <= MAX_INT else ~(num1 ^ MASK)