import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        heap = []
        for key, value in counts.items():
            heapq.heappush(heap, (value, key))

        while len(heap) > k:
            heapq.heappop(heap)
        
        return [key for (_, key) in heap]

"""
[1,2,2,3,3,3], k = 2

(1,1)
(2,2)
(3,3)

n log n + n

"""