class convert:
    def bin2dec(self, num: int) -> int:
        dec_num = 0
        deg = 0
        while num > 0:
            reminder = num % 10
            num = num // 10
            dec_num += reminder * (2**deg)
            deg += 1
        return dec_num

    def dec2bin(self, num: int) -> int:
        bin_num = 0
        deg = 0
        while num > 0:
            reminder = num % 2
            num = num // 2
            bin_num += reminder * (10**deg)
            deg += 1
        return bin_num