class contain_duplicate:
    # Approach 1: brute force
    # Time complexity: O(n^2)  -  Space complexity: O(1)
    def brute_force(self, arr: list[int]) -> bool:
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] == arr[j]:
                    return True
        return False
    
    # Approach 2: sorting and then compare if next element is concided
    # Time complexity : O(n log n)  -  
    # Space complexity: O(1) if in-place; O(n) if using sorted()
    def sorting(self, arr: list[int]) -> bool:
        arr.sort()
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                return True
        return False
    
    # Approach 3:
    # Time complexity O(n)  -  Space complexity: O(n)
    def hash_count(self, arr: list[int]) -> bool:
        hashmap = {}
        if len(arr) == 0:
            return False
        for elm in arr:
            cnt = 1
            if elm in hashmap:
                cnt += 1
            hashmap[elm] = cnt

        return True if max(v for _, v in hashmap.items()) > 1 else False
    
    # Approach 4:
    # Time complexity: O(n)  -  Space complexity: O(n)
    def hash_set(self, arr: list[int]) -> bool:
        seen = set()
        for num in arr:
            if num in seen:
                return True
            seen.add(num)
        return False
    
    # Approach 5:
    # Time complexity: O(n)  -  Space complexity: O(n)
    def hash_set_length(self, arr: list[int]) -> bool:
        return len(set(arr)) < len(arr)