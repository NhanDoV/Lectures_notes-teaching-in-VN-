class singleNumber:
    """
        Reference: https://neetcode.io/problems/single-number?list=neetcode150
        Every integer appears twice except for one.
    """
    # Time complexity: O(n^2)       Space complexity: O(1)
    def brute_force(self, nums: list[int]) -> int :
        n = len(nums)
        for i in range(n):
            if_exist = True
            # we need to check pair-of-twice; so we can not started j = i + 1
            for j in range(n):
                if (i != j)*(nums[i] == nums[j]):
                    if_exist = False
                    break
            if if_exist:
                return nums[i]

    # Time complexity: O(n)       Space complexity: O(n)
    def using_HashSet(self, nums: list[int]) -> int :
        """
            remove any element if it already existed in the set; otherwise append it
        """
        hashset = set()
        for num in nums:
            if num in hashset:
                hashset.remove(num)
            else:
                hashset.add(num)
        return hashset
    
    # Time complexity: O(n log n)       Space complexity: O(n)
    def using_sort(self, nums: list[int]) -> int :
        """
            Sorting arr; since "every integer appears twice except for one"; so we will get sth like

                    1       1       2       2       x       7       7   ...
            
            the index of single will be skiped by 2 until we meet
        """
        nums.sort()
        idx = 0
        n = len(nums)
        while idx < n - 1:
            if nums[idx] == nums[idx + 1]:
                idx += 2
            else:
                return nums[idx]
        return nums[idx]

    # Time complexity: O(n)       Space complexity: O(1)
    def using_bit_XOR(self, nums: list[int]) -> int :
        """
            TRICK: 
                    * For each pair of twice-interger, then 
                    
                                        a XOR a     =   0
                                        
                    * For any integer, we have
                    
                                        0 XOR a     =   a
        """
        check = 0
        for num in nums:
            # XOR return 0 if both element is the same
            check = num ^ check
        return check