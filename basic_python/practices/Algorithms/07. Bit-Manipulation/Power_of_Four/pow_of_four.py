import math

class isPowerOfFour:
    """
        Exception cases:
            * Some even numbers like n = 0,2,6,8, (which not is power of 4) --> False
            * Except 1; other odd (n = 1,3,5, etc)                          --> False
            * All negative numbers will be rejected
    """
    def using_log(self, num : int) -> bool:
        if num <= 0:
            return False
        log_val = math.log(num, 4)
        return log_val == int(log_val)

    def using_log_opt(self, num: int) -> bool:
        return (num > 0) and (math.log(num, 4) % 1 == 0)

    def using_iter(self, num: int) -> bool:
        if num <= 0:
            return False
        while num > 1:
            if num % 4 > 0:
                return False
            num = num // 4
        return num == 1

    def using_recursive(self, num: int) -> bool:
        if num == 1:
            return True
        if (num < 0) or num % 4:
            return False
        return self.using_recursive(num // 4)

    def using_loop(self, num: int) -> bool:
        if num == 0:
            return False
        while (num > 0):
            if (num <= 0) | ( (num > 1) & (num % 2 == 1) ) | (num % 4 == 2):
                return False
            num = num // 4
        return num == 0

    def using_bit_manipulation(self, num: int) -> bool:
        if num <= 0:
            return False
        # consider only the digit at the even-index    
        for digit in range(0, 32, 2):
            # at these index; if num is equal to power of even-number
            if num == (1 << digit):
                return True
        return False

    def using_bit_mask_and_position(self, num: int) -> bool:
        positive_flag = (num > 0)
        # ensures n has exactly one '1' bit (power of two)
        flag2 = (num & (num - 1)) == 0
        # ensures that '1' bit appears in an even bit position (0, 2, 4, ...)
        flag3 = (num & 0x55555555) == num
        return positive_flag and flag2 and flag3

    def using_bit_mask_and_mod3(self, num: int) -> bool:
        positive_flag = (num > 0)
        flag2 = (num & (num - 1)) == 0
        # check if the reminder in modulo by 3 of num is 1
        flag3 = (num % 3) == 1
        return positive_flag and flag2 and flag3