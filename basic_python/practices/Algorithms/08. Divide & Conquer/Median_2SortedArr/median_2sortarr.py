class findMedianSortedArrays:
    def simple(self, nums1: list[int], nums2: list[int]):
        merged = sorted(nums1 + nums2)
        length = len(merged)

        if length % 2 == 0:
            return (merged[length // 2 - 1] + merged[length // 2]) / 2
        else:
            return merged[length // 2]

    def divide_and_conquer(self, nums1: list[int], nums2: list[int]):
        def kth(A, B, k):
            # ensure A is the shorter array
            if len(A) > len(B):
                return kth(B, A, k)

            if not A:
                return B[k - 1]

            if k == 1:
                return min(A[0], B[0])

            i = min(len(A), k // 2)
            j = k - i

            if A[i - 1] <= B[j - 1]:
                return kth(A[i:], B, k - i)
            else:
                return kth(A, B[j:], k - j)

        total = len(nums1) + len(nums2)

        if total % 2 == 1:
            return kth(nums1, nums2, total // 2 + 1)
        else:
            left = kth(nums1, nums2, total // 2)
            right = kth(nums1, nums2, total // 2 + 1)
            return (left + right) / 2

    def Binary_Search(self, nums1: list[int], nums2: list[int]):
        A, B = nums1, nums2
        n, m = len(A), len(B)
        if n > m: # suppose B has more element than in A, otherwise swap
            A, B, n, m = B, A, m, n            
        total = n + m
        half = (total + 1) // 2        
        left, right = 0, n
        while left <= right:
            cen = (left + right) // 2
            adj = half - cen         
            Aleft = A[cen-1] if cen > 0 else float('-inf')
            Aright = A[cen] if cen < n else float('inf')
            Bleft = B[adj-1] if adj > 0 else float('-inf')
            Bright = B[adj] if adj < m else float('inf')
            
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:  # odd
                    return max(Aleft, Bleft)
                else:  # even
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                right = cen - 1
            else:
                left = cen + 1