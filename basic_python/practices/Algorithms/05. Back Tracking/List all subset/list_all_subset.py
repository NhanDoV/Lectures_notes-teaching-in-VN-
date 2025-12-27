class list_all_subsets:
    def use_itertools(self, nums: list[int]) -> list[list[int]]:
        from itertools import combinations as comb
        myls = []
        for n_elm in range(len(nums) + 1):
            for ls in comb(nums, n_elm):
                myls.append(list(ls))
        return myls
    
    def using_iterate(self, nums: list[int]) -> list[list[int]]:
        all_subsets = []        
        # For each elements
        for num in nums:
            for subset in all_subsets:
                all_subsets += [ subset + [num] ]

        return all_subsets

    def backtracking_subsets(self, nums: list[int]) -> list[list[int]]: # backtracking
        myls = []
        # define backtrack 
        def backtrack(cur, pos):
            myls.append(cur.copy())
            for i in range(pos, len(nums)):
                cur.append(nums[i])
                backtrack(cur, i + 1)
                cur.pop()

        backtrack([], 0)
        return myls