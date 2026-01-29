from typing import List

class maxSubArray:
    def brute_Force(self, nums: List[int]) -> int:
        ans = -inf
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                ans = max(ans, cur_sum)
        return ans        
    
    def divide_conquer(self, nums: List[int]) -> int:
        def max_crossing_subarray(left, mid, right):
            # Left half: tìm max sum từ mid về trái
            left_sum = float('-inf')
            curr = 0
            for i in range(mid, left-1, -1):
                curr += nums[i]
                left_sum = max(left_sum, curr)
            
            # Right half: từ mid+1 về phải  
            right_sum = float('-inf')
            curr = 0
            for i in range(mid+1, right+1):
                curr += nums[i]
                right_sum = max(right_sum, curr)
            
            return left_sum + right_sum
        
        def dac(left, right):
            if left == right:
                return nums[left]
            
            mid = (left + right) // 2
            
            # 3 cases
            left_max = dac(left, mid)
            right_max = dac(mid+1, right)
            cross_max = max_crossing_subarray(left, mid, right)
            
            return max(left_max, right_max, cross_max)
        
        return dac(0, len(nums)-1)

    def Kadane_algo(self, nums: List[int]) -> int:
        current_sum = nums[0]  # Tổng của subarray hiện tại
        max_sum = nums[0]      # Tổng lớn nhất tìm được    

        for i in range(1, len(nums)):
            # Lựa chọn giữa: bắt đầu subarray mới hoặc tiếp tục subarray cũ
            current_sum = max(nums[i], current_sum + nums[i])
            # Cập nhật tổng lớn nhất
            max_sum = max(max_sum, current_sum)    

        return max_sum