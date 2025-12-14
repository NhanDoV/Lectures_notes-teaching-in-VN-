from collections import defaultdict

class groupAnagrams:
    def using_sort(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for s in strs:
            sorted_str = ''.join(sorted(s))
            res[sorted_str].append(s)
        return list(res.values())
    
    def using_hash(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

if __name__ == "__main__":
    print("Enter your list of strings (type one word per line):")
    n_words = int(input("Number of words: "))
    
    raw = []
    for _ in range(n_words):
        vocab = input(f"\t {1 + _}: \t")
        raw.append(vocab)

    method = input("Choose method: 'sort' or 'hash': ").strip().lower()

    solver = groupAnagrams()

    if method == "hash":
        result = solver.using_hash(raw)
    else:
        result = solver.using_sort(raw)

    print("Grouped anagrams:", result)