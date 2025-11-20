class WordBreak:
    def using_replace(self, s: str, wordDict: list[str]) -> bool:
        """
            Not True if wordDict contains multiple sliding-subsets of string s
            ..........................................
            Exception cases: 
                s = "cars" and wordDict = ["car", "ca", "rs"]
        """
        for word in wordDict:
            if word in s:
                s = s.replace(word, '')
        return len(s) == 0

    def recursive_without_hash(self, s: str, wordDict: list[str]) -> bool:
        def recursive(s):
            pass


    def using_hash(self, s: str, wordDict: list[str]) -> bool:
        wordSet = set(wordDict)
        def recursion(idx):
            if idx == len(s):
                return True
            for j in range(idx, len(s)):
                print(j, s[idx : j + 1])
                if (s[idx : j + 1] in wordSet) and recursion(j + 1):
                        return True
            return False
        
        return recursion(0)

    def using_DP(self, s: str, wordDict: list[str]) -> bool:
        pass