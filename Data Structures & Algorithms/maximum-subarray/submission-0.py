import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cum_sum = -math.inf
        max_sum = -math.inf

        for num in nums:
            cum_sum = max(cum_sum + num, num)
            max_sum = max(cum_sum, max_sum)
        
        return max_sum
