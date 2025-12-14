class EncDecodeStrings:     
    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res
    
if __name__ == "__main__":
    n_vocab = int(input("Number of words: \t"))
    raw = []
    for idx in range(n_vocab):
        vocab = input(f"\t {1 + idx}: \t")
        raw.append(vocab)

    solver = EncDecodeStrings()
    encoded = solver.encode(raw)
    print("Encoded string: \t", encoded)
    print("Decoded list: \t", solver.decode(encoded))

    # Bonus: verify decode == original
    print("Match original list?", solver.decode(encoded) == raw)