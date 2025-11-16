class twoSum:
    # Approach 1.
    def brute_force(self, nums: list[int], target: int) -> list[int]:
        # Time Complexity O(n^2)       -     Space O(1)
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
    # Approach 2.
    def sorting(self, nums: list[int], target: int) -> list[int]:
        # Time Complexity O(n * log n)       -     Space O(n)
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])

        A.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            cur = A[i][0] + A[j][0]
            if cur == target:
                return [min(A[i][1], A[j][1]),
                        max(A[i][1], A[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1
        return []
    
    # Approach 3:
    def hashmap_one_pass(self, nums: list[int], target: int) -> list[int]:
        # Time Complexity O(n)       -     Space O(n)
        indices = {}  # val -> index

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
            
    # Approach 4:
    def hashmap_two_pass(self, nums: list[int], target: int) -> list[int]:
        # Time Complexity O(n)       -     Space O(n)
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i