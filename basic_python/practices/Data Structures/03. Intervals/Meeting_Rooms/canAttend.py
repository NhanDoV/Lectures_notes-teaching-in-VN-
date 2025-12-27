class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.validate = start > end

class canAttendMeetings:
    """
        Examples:
            >>> intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
            >>> sol = canAttendMeetings()
            >>> sol.brute_force(intervals)
                False

            >>> intervals = [Interval(3, 8), Interval(9, 15)]
            >>> sol.brute_force(intervals)
                True

        Suppose that all the intervals are valid (start[i] < end[i] for each i)
    """
    def brute_force(self, intervals: list[Interval]) -> bool:
        n = len(intervals)
        for idx_A in range(n):
            per_A = intervals[idx_A]
            for idx_B in range(idx_A + 1, n):
                per_B = intervals[idx_B]
                if min(per_A.end, per_B.end) > max(per_A.start, per_B.start):
                    return False
        return True
    
    def sorting(self, intervals: list[Interval]) -> bool:
        intervals.sort(key = lambda i: i.start)
        for idx in range(1, len(intervals)):
            A = intervals[idx - 1]
            B = intervals[idx]
            if A.end > B.start:
                return False
        return True 