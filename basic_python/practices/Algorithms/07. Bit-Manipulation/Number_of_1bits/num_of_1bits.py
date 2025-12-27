class num_of_1bit:
    def count_on_string_of_bin(self, n: int) -> int:
        bin_num = bin(n)[2:]
        return sum( [(d == "1") for d in bin_num] )
    
    def bit_mask_v1(self, n: int) -> int:
        cnt = 0
        for idx in range(32):
            # check if both n and 2^idx both contains 1
            if (1 << idx) & n:
                print(f"idx: {idx}, 2^idx = {1 << idx}  \t{n}")
                cnt += 1
        return cnt
    
    def bit_mask_v2(self, n: int) -> int:
        cnt = 0
        while n != 0:
            n &= n - 1
            cnt += 1
        return cnt