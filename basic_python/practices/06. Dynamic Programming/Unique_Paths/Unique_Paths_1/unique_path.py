class uniquePaths:
    def factorial(self, n: int) -> int:
        res = 1
        while n > 0:
            res *= n
            n = n - 1
        return res
    
    def using_combination(self, m: int, n: int) -> int:
        return (self.factorial(m + n - 2) // (self.factorial(n - 1) * self.factorial(m - 1)))
        
    def using_DP(self, m: int, n: int) -> int:
        dp = [ [1]*m for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]