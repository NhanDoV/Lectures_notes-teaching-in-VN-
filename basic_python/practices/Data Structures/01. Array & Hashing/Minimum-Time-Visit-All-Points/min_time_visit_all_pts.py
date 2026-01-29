class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        # note, n_seconds = max( |x[i] - x[i + 1]|, |y[i] - y[i + 1]| )
        n = len(points)
        
        if n == 1:
            return 0

        total = 0

        for idx in range(1, n):
            x_curr, y_curr = points[idx - 1]
            x_next, y_next = points[idx]
            n_sec = max( abs(x_curr - x_next), abs(y_curr - y_next) )
            total += n_sec

        return total