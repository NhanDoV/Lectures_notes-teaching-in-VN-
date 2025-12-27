class Fibonacci:
    # Time Complexity: O(2^n)      Space Complexity: O(n)
    def recursive_approach(self, n: int) -> int:
        if n < 0:
            raise ValueError("n must be non-negative")
        if n in [0, 1]:
            return n
        else:
            return self.recursive_approach(n - 1) + self.recursive_approach(n - 2)
    
    # Time Complexity: O(n)        Space Complexity: O(n)
    def dynamic_programming(self, n: int) -> int:
        dp = [1, 1]
        for idx in range(n):
            new_val = dp[idx - 1] + dp[idx - 2]
            dp.append(new_val)
        return dp[-1]

    # Time Complexity: O(n)        Space Complexity: O(1)
    def DP_no_memo(self, n: int) -> int:
        if n <= 0:
            raise ValueError("n must be greater than 0")
        if n == 1:
            return 1
        if n == 2:
            return 1
        prev, curr = 1, 1
        for i in range(3, n + 1):
            prev, curr = curr, prev + curr
        return curr