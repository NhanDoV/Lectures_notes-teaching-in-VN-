class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.validate = start > end

class min_day_canAttendMeeting:
    def brute_force(self, intervals: list[list]) -> bool:
        intervals.sort(key=lambda x: x.start)
        n = len(intervals)
        best = n                                    # worst case: one room per interval
        rooms = []                                  # list of rooms, each room = list of intervals

        # stack-based manual brute-force (no recursion): (index_of_interval, current_rooms)
        stack = [(0, rooms)]                        

        while stack:
            i, cur_rooms = stack.pop()            
            if i == n:                           # all intervals assigned → update best
                best = min(best, len(cur_rooms))
                continue
            
            if len(cur_rooms) >= best:           # prune: already worse than best
                continue

            A = intervals[i]

            for r in range(len(cur_rooms)):     # Try putting interval A in every possible existing room
                room = cur_rooms[r]
                last = room[-1]
                
                if A.start >= last.end:         # conflict check: only need to check last because room sorted 
                    # place A into this room
                    new_rooms = [list(x) for x in cur_rooms]
                    new_rooms[r].append(A)
                    stack.append((i+1, new_rooms))

            # Try to open a new room
            new_rooms = [list(x) for x in cur_rooms]
            new_rooms.append([A])
            stack.append((i+1, new_rooms))

        return best

    def using_heap(self, intervals: list[list]) -> bool:
        import heapq

        intervals.sort(key=lambda x: x.start)
        min_heap = []

        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)

        return len(min_heap)
    
    def using_2pointers(self, intervals: list[list]) -> bool:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res = count = 0
        s = e = 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res