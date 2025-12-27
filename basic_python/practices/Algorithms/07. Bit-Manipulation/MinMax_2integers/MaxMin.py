class MaxMin_2num:
    """
        Return respectively maximum and minimum of 2 positive integers
    """
    def using_comparisons(self, num1: int, num2: int):
        return (num1, num2) if num1 > num2 else (num2, num1)
            
    def using_maxmin_directly(self, num1: int, num2: int):
        return max(num1, num2), min(num1, num2)

    def using_abs_and_plus(self, num1: int, num2: int):
        max_val = (num1 + num2) + abs(num1 - num2) 
        min_val = (num1 + num2) - abs(num1 - num2)
        return max_val // 2, min_val // 2

    def using_bit_manipulation(self, num1: int, num2: int):
        max_val = num1 ^ ((num1 ^ num2) & -(num1 < num2))
        min_val = num2 ^ ((num1 ^ num2) & -(num1 < num2))
        return max_val, min_val