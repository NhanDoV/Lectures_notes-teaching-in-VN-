from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        n_half = n // 2
        
        max_sum = 0
        for i in range(n_half):
            sum = nums[i] + nums[n - i - 1]
            if sum > max_sum:
                max_sum = sum

        return max_sum