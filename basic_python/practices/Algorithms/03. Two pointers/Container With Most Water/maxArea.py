class max_area:
    def brute_force(self, heights: list[int]) -> int:
        n = len(heights)
        S = []
        for i in range(n):
            for j in range(i+1, n):
                min_h = min( heights[i], heights[j] )
                width = j - i
                S.append(min_h * width)
        return max(S)
    
    def two_pointers(self, heights: list[int]) -> int:
        left, right = 0, len(heights)
        