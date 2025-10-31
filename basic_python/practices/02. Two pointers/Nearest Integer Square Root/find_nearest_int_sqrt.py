class Find_Nearest_sqrt_integer:
    # Approach 1
    # Time complexity: O( sqrt n )         Space complexity: O( sqrt n )
    def brute_force(self, num: int):
        hashmap = {}
        for digit in range(1, num // 2 + 1):
            num_sq = digit*digit
            diff = abs(num - num_sq)
            hashmap[diff] = digit
        # return the digit has the minimum difference : argmin( digit*digit - num )
        return hashmap[min(hashmap.keys())]
    
    # Approach 2
    # Time complexity: O(log n)         Space complexity: O(1)
    def using_2pointers(self, num: int):
        left, right = 1, num // 2
        while left < right:
            mid = (left + right) // 2
            num_sq = mid * mid
            if num_sq == num:
                return num
            elif num_sq < num:
                left = mid + 1
            else:
                right = mid - 1
        # When loop ends, right < left and x in (mid, right)
        return left, mid, right