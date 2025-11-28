class intervalIntersection:
    def brute_force_naive(self, firstList: list[list[int]], 
                          secondList: list[list[int]]) -> list[list[int]]:
        res = []
        if len(firstList) == 0 or len(secondList) == 0:
            return []

        for A in firstList:
            for B in secondList:
                if max(A[0], B[0]) <= min(A[1], B[1]):
                    itv = [max(A[0], B[0]), min(A[1], B[1])]
                    res.append(itv)

        res = [list(x) for x in set(tuple(x) for x in res)]
        res = sorted(res)

        return res # 