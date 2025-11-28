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
        def DFS(i):
            if i == len(s):
                return True

            for w in wordDict:
                if ((i + len(w)) <= len(s) and
                     s[i : i + len(w)] == w
                ):
                    if DFS(i + len(w)):
                        return True
            return False
        return DFS(0)

    def using_hash(self, s: str, wordDict: list[str]) -> bool:
        wordSet = set(wordDict)
        def DFS(idx):
            if idx == len(s):
                return True
            for j in range(idx, len(s)):
                if (s[idx : j + 1] in wordSet) and DFS(j + 1):
                        return True
            return False
        
        return DFS(0)

    def using_DP_hash(self, s: str, wordDict: list[str]) -> bool:
        wordSet = set(wordDict)
        t = 0
        for w in wordDict:
            t = max(t, len(w))

        memo = {}
        def DFS(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return True
            for j in range(i, min(len(s), i + t)):
                if s[i : j + 1] in wordSet:
                    if DFS(j + 1):
                        memo[i] = True
                        return True
            memo[i] = False
            return False

        return DFS(0)
    
    def DP_TopDown(self, s: str, wordDict: list[str]) -> bool:
        memo = {len(s) : True}
        def DFS(i):
            if i in memo:
                return memo[i]

            for w in wordDict:
                if ((i + len(w)) <= len(s) and
                     s[i : i + len(w)] == w
                ):
                    if DFS(i + len(w)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False

        return DFS(0)
    
    def DP_BottomUp(self, s: str, wordDict: list[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]    