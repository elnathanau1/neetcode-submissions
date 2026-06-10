import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        freq = [[] for _ in range(len(nums))]
        for key, count in counts.items():
            freq[count - 1].append(key)
        
        ret_list = []
        for i in range(len(nums)):
            index = len(nums) - i - 1
            for num in freq[index]:
                ret_list.append(num)
                if len(ret_list) == k:
                    return ret_list
        return ret_list
"""
[1,2,2,3,3,3], k = 2

(1,1)
(2,2)
(3,3)

n log n + n

"""