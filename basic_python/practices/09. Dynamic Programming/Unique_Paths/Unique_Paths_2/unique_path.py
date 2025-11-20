class Unique_paths:

    def using_recursive(self, m: int, n: int) -> int:
        def dfs(i, j):
            if i == (m - 1) and j == (n - 1):
                return 1
            if i >= m or j >= n:
                return 0
            return dfs(i, j + 1) + dfs(i + 1, j)

        return dfs(0, 0)
    
    def DP_TopDown(self, m: int, n: int) -> int:
        memo = [[-1] * n for _ in range(m)]
        def dfs(i, j):
            if i == (m - 1) and j == (n - 1):
                return 1
            if i >= m or j >= n:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]

            memo[i][j] =  dfs(i, j + 1) + dfs(i + 1, j)
            return memo[i][j]

        return dfs(0, 0)