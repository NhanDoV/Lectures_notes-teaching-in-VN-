class swap_number:
    def navie_approach(self, a: int, b: int):
        a, b = b, a
        return a, b
    
    def basic_method(self, a: int, b: int):
        a = a + b
        b = a - b
        a = a - b

        return a, b

    def using_XOR(self, a: int, b: int):
        a = a^b   # a = XOR(a, b)
        b = b^a   # b = XOR(b, XOR(a, b)) = a
        a = a^b   # a = XOR(XOR(a, b), b) = b

        return a, b