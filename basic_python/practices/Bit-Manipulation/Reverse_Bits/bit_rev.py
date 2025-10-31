class reverseBits:

    def using_bin_and_reverse(self, n: int) -> int:
        # E.g. bin(11) will return '0b1011' and we just ignore the first 2 idx
        bin_num = bin(n)[2:]
        bin_num = f'{(32 - len(bin_num))*"0"}{bin_num}'
        bin_num_rev = bin_num[::-1]
        
        # convert binary into decimal
        n = int(bin_num_rev)
        res = 0
        deg = 0
        while n > 0:
            reminder = n % 10
            n //= 10
            res += reminder * (2 ** deg)
            deg += 1
        
        return res

    # Time complexity O(1) - Space complexity: O(1)    
    def brute_force(self, n: int) -> int:
        bin_str = ""
        for i in range(32):
            if n & (1 << i):
                bin_str += "1"
            else:
                bin_str += "0"

        res = 0
        for i, bit in enumerate(bin_str[::-1]):
            if bit == "1":
                res |= (1 << i)

        return res