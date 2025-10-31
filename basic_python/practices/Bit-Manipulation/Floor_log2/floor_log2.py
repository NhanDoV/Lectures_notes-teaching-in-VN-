class find_floor_log2:
    def naive_method(self, num: int) -> int:
        import math
        return int(math.log2(num))

    def without_using_log_directly(self, num: int) -> int:
        deg = 0
        while num > 1:
            num = num // 2
            deg += 1
        return deg
        
    def using_bit_RightShift(self, num: int) -> int:
        deg = 0
        while num > 1:
            num = num >> 1
            deg += 1
        return deg