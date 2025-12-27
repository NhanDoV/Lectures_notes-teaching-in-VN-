class Permute:
    def using_itertools(self, nums: list[int]) -> list[list[int]]:
        from itertools import permutations as perm        
        return [list(perm_case) for perm_case in perm(nums)]

    # ============================ ITERATION ==================================
    def using_iteration(self, nums: list[int]) -> list[list[int]]:
        all_perms = [[]]

        for n in nums:
            new_perms = []
            for perm in all_perms:
                for i in range(len(perm) + 1):
                    new_perms.append(perm[:i] + [n] + perm[i:])
            all_perms.append(new_perms)
        return all_perms

    # ========================== RECURSIVE ====================================
    def using_recursion(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 0:
            return [[]]

        perms = self.using_recursion(nums[1:])
        all_perms = []

        for p in perms:
            for i in range(len(p) + 1):
                perm_copy = p.copy()
                perm_copy.insert(i, nums[0])
                all_perms.append(perm_copy)
        return all_perms

    # ============================ BACKTRACKING ==============================
    def using_backtracking(self, nums: list[int]) -> list[list[int]]:
        self.res = []

        # Select backtracking method
        self.backtrack_basic([], nums, [False] * len(nums))
        # you can also use other of:
        # self.backtracking_bitmask([], nums, 0) or
        # self.backtrack_opt(nums, 0)
        
        return self.res

    # ========================= BACK-TRACKING methods ==========================
    def backtrack_basic(self, perm: list[int], nums: list[int], pick: list[bool]):
        if len(perm) == len(nums):
            self.res.append(perm[:])
            return
        for i in range(len(nums)):
            if not pick[i]:
                perm.append(nums[i])
                pick[i] = True
                self.backtrack(perm, nums, pick)
                perm.pop()
                pick[i] = False

    def backtracking_bitmask(self, perm: list[int], nums: list[int], pick: list[bool], mask: int):
        if len(perm) == len(nums):
            self.res.append(perm[:])
            return
        for i in range(len(nums)):
            if not (mask & (1 << i)):
                perm.append(nums[i])
                self.backtrack(perm, nums, mask | (1 << i))
                perm.pop()
                
    def backtrack_opt(self, nums: list[int], idx: int):
        if idx == len(nums):
            self.res.append(nums[:])
            return
        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            self.backtrack(nums, idx + 1)
            nums[idx], nums[i] = nums[i], nums[idx]