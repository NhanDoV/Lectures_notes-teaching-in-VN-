class ThreeSum:
    def brute_force(self, nums: list[int]) -> list[list[int]]:
        mytriplet = set()
        nums.sort()
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        mytriplet.add( tuple( [nums[i], nums[j], nums[k] ] ) )
        return [list(elm) for elm in mytriplet]
    
    def using_hashmap(self, nums: list[int]) -> list[list[int]]:
        pass

    def using_2pointers(self, nums: list[int]) -> list[list[int]]:
        pass