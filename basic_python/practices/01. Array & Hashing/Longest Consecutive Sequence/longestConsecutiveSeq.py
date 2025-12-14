class longestConsecutive:
    def brute_force(self, nums: list[int]) -> int:
        res = 0
        unique_num = set(nums)

        for num in nums:
            streak, curr = 0, num
            while curr in unique_num:
                streak += 1
                curr += 1
            print(num, curr, streak)
            res = max(res, streak)
        return res

    def using_hash(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest