from typing import List

class triangleNumber:
    def brute_force(self, nums: List[int]) -> int:
        n = len(nums)

        def valid_triag(a, b, c):
            return (a + b > c) & (b + c > a) & (a + c > b)        
        if n < 3:
            return 0
        cnt = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if valid_triag(nums[i], nums[j], nums[k]):
                        cnt += 1

        return cnt

    def greedy(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        for k in range(n-1, 1, -1):  # Fix largest side FIRST
            i = 0
            j = k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += j - i  # Greedy count all i to j
                    j -= 1
                else:
                    i += 1
        return count
