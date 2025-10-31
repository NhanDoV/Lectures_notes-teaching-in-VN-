class topKFrequent:
    def hashmap_sorting(self, nums: list[int], k: int) -> list[int]:
        hashmap = {}
        for num in nums:
            cnt = 0
            if num in hashmap:
                cnt = cnt + 1
            hashmap[num] = hashmap.get(num, 0) + 1
        res = sorted(hashmap,
                    key = hashmap.get,
                    reverse = True
                    )[:k]
        return res
    
    # Approach 2:
    def min_heap(self, nums: list[int], k: int) -> list[int]:
        import heapq

        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res