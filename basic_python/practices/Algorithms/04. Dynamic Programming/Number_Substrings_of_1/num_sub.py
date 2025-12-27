class numSub:
    def brute_force(self, s: str) -> int:
        cnt = 0
        for idx in range(len(s)):
            for width in range(1, len(s) + 1 ):
                if s[idx : idx + width] == '1' * width:
                    # print(idx, idx + width, s[idx : idx + width])
                    cnt += 1
        return cnt
    
    def math_trick(self, s: str) -> int:
        """
            Noting that every consecutive 1's form a block, and from a block of length k, 
            the number of valid substrings is: 
                                                k * (k + 1) / 2
        
            Return 
                        sum(accumulate(map(int, s), lambda q,v : -~ q * v))
        """
        ans = 0
        count = 0
        for i in range(len(s)):
            if(s[i] == "1"):
                count += 1
            else:
                ans += ((count * (count + 1)) // 2)     # in case exceed 32-bit % int(10**9 + 7)
                count = 0
        ans += ((count * (count + 1)) // 2)             # % int(10**9 + 7)

        return ans

    def dp(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        for idx in range(len(s)):
            if s[idx] == "1":
                dp[idx + 1] = dp[idx] + 1
            else:
                dp[idx + 1] = 0
        return sum(dp)