"""
        The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
        By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

                    1. "123"                4. "231"
                    2. "132"                5. "312"
                    3. "213"                6. "321"
        Given n and k, return the kth permutation sequence.
"""

import itertools
from math import factorial

class getPermutation:
    def using_permutation(self, n: int, k: int) -> str:
        idx = 0
        rng = range(1, n + 1)
        for num in itertools.permutations(rng, n):
            idx += 1
            if idx == k:
                break
        
        return "".join([str(i) for i in num])

    def using_factorial(self, n: int, k: int) -> str:
        nums = list(range(1, n + 1))
        fact = factorial(n) // n
        k -= 1
        res = []

        while nums:
            res.append(str(nums[k // fact]))
            nums.pop(k // fact)
            if not nums:
                break
            k %= fact
            fact //= len(nums)

        return "".join(res)