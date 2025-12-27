class Multiply_nums:
    def naive_approach(self, num1: int, num2: int) -> int:
        return num1 * num2

    def using_bit_manipulation(self, num1: int, num2: int) -> int:
        """
            Multiply two integers using only bitwise operations:
                - Uses shifts (<<, >>)
                - Uses bitwise AND (&)
                - Uses addition (+)
        """
        # Handle negative values manually
        sign = -1 if (num1 < 0) ^ (num2 < 0) else 1
        num1, num2 = abs(num1), abs(num2)
        
        result = 0
        while num2 > 0:
            # Check if the lowest bit of num2 is set
            if num2 & 1:
                result += num1
            
            # Shift left num1 (multiply by 2)
            num1 <<= 1
            # Shift right num2 (divide by 2)
            num2 >>= 1
        
        return result * sign

    #======================= Clarify how this work by these examples ==================================
    def multiply_7_using_bit(self, num: int) -> int:
        """
            TRICK:
                    7*n = 8*n - n
                    8*n = n << 3                LEFT SHIFT by 3
        """
        return (num << 3) - num

    def multiply_13_using_bit(self, num: int) -> int:
        """
            TRICK:
                    13*n = 8*n + 4*n + n
                     8*n = n << 3                LEFT SHIFT by 3
                     4*n = n << 2                LEFT SHIFT by 2
        """
        return (num << 3) + (num << 2) + num

    def num_decay_by_power_of_2(self, num: int) -> list[int]:
        """
            Description:
                Decomposite list of signs and degrees (w.r.t. power of base 2); which formed the original numbers
            -----------------------------------------------------------------------------------------------------
            Illustration:
                ................................................................................................
                EX 1. num = 11
                    Then
                        11  =   pow(2, 3)   +   pow(2, 1)   +   pow(2, 0)

                            i.e      8       +       2       +       1
                        
                        degs    =     [3, 2, 1, 0]
                        signs   =     [1, 0, 1, 1]  
                ................................................................................................
                EX 2. num = 13, Then
                        degs    =     [3, 2, 1, 0]
                        signs   =     [1, 1, 0, 1]              
                    
                    since   13  =   8   +   4   +   1
        """
        # Find maximum of floor of degrees power of base 2 from the given number
        max_floor_deg = 0
        temp_num = num
        while temp_num > 1:
            temp_num = temp_num >> 1
            max_floor_deg += 1

        # Ordered the number descendingly
        degs = [ (max_floor_deg - d) for d in range(max_floor_deg)] + [0]
        
        # Iterate in degree to find the signs of each corresponding value
        signs = []
        for deg in degs:
            diff = num - (1 << deg)                 # diff      =    num     -     pow(2, deg)
            # print(f"diff = {num} - 2^{deg} = {diff}")
            if diff >= 0:
                num = diff
                signs.append(1)
            else:
                num = num
                signs.append(0)

        return signs, degs
    
    def using_bit_manipulation_v1(self, num1: int, num2: int) -> int:
        """
            Find the product of 2 integer without using multiply directly
            Here we use + operators and LEFT - RIGHT shift ONLY
        """
        # You can also use math.log2(num2) here instead
        max_floor_deg = 0
        temp_num = num2
        while temp_num > 1:
            temp_num = temp_num >> 1
            max_floor_deg += 1

        # Ordered the number descendingly
        degs = [ (max_floor_deg - d) for d in range(max_floor_deg)] + [0]

        # Iterate in degree to find the signs of each corresponding value
        prod = 0
        for deg in degs:
            diff = num2 - (1 << deg)            # diff  =   num     -     pow(2, deg)
            if diff >= 0:
                num2 = diff
                sign = 1
            else:
                num2 = num2
                sign = 0
            prod += sign * (num1 << deg)        
        
        return prod    